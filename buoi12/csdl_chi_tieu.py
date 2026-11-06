# -*- coding: utf-8 -*-
"""
Module: csdl_chi_tieu.py
Mô tả: Quản lý cơ sở dữ liệu SQLite cho Ứng dụng Quản lý Chi tiêu Cá nhân.
Tách biệt hoàn toàn tầng dữ liệu (Database layer) với giao diện (GUI).
"""

import sqlite3

TEN_FILE_CSDL = "chi_tieu.db"

def ket_noi_csdl():
    """Tạo và trả về đối tượng kết nối đến CSDL SQLite."""
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    """Tạo bảng chi_tieu nếu bảng chưa tồn tại."""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS chi_tieu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ngay TEXT NOT NULL,
            danh_muc TEXT NOT NULL,
            so_tien REAL NOT NULL,
            ghi_chu TEXT
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_chi_tieu(ngay: str, danh_muc: str, so_tien: float, ghi_chu: str = "") -> int:
    """
    Thêm một khoản chi tiêu mới vào cơ sở dữ liệu.
    Trả về id của bản ghi vừa thêm.
    """
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        INSERT INTO chi_tieu (ngay, danh_muc, so_tien, ghi_chu)
        VALUES (?, ?, ?, ?)
    """, (ngay, danh_muc, so_tien, ghi_chu))
    id_moi = con_tro.lastrowid
    ket_noi.commit()
    ket_noi.close()
    return id_moi

def lay_toan_bo_chi_tieu():
    """
    Lấy toàn bộ danh sách các khoản chi tiêu, sắp xếp ngày mới nhất lên đầu.
    Trả về danh sách tuple: [(id, ngay, danh_muc, so_tien, ghi_chu), ...]
    """
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        SELECT id, ngay, danh_muc, so_tien, ghi_chu 
        FROM chi_tieu 
        ORDER BY ngay DESC, id DESC
    """)
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_chi_tieu(id_chi_tieu: int):
    """Xóa một khoản chi tiêu dựa vào ID."""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM chi_tieu WHERE id = ?", (id_chi_tieu,))
    ket_noi.commit()
    ket_noi.close()

def tinh_tong_chi_tieu() -> float:
    """Tính tổng số tiền đã chi tiêu."""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT SUM(so_tien) FROM chi_tieu")
    tong = con_tro.fetchone()[0]
    ket_noi.close()
    return tong if tong is not None else 0.0

def thong_ke_theo_danh_muc():
    """
    Thống kê tổng số tiền chi tiêu nhóm theo từng danh mục.
    Trả về danh sách tuple: [(danh_muc, tong_tien), ...]
    """
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        SELECT danh_muc, SUM(so_tien) 
        FROM chi_tieu 
        GROUP BY danh_muc
        ORDER BY SUM(so_tien) DESC
    """)
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

if __name__ == "__main__":
    # Khối kiểm thử độc lập cho module CSDL
    print("--- Kiểm thử module csdl_chi_tieu.py ---")
    tao_bang_neu_chua_co()
    print("1. Đã tạo bảng thành công.")
    
    # Thử thêm dữ liệu
    them_chi_tieu("2026-11-01", "Ăn uống", 45000, "Ăn sáng phở bò")
    them_chi_tieu("2026-11-02", "Đi lại", 100000, "Đổ xăng xe máy")
    them_chi_tieu("2026-11-03", "Mua sắm", 350000, "Mua áo thun mới")
    print("2. Đã thêm 3 bản ghi mẫu.")

    # Lấy danh sách
    danh_sach = lay_toan_bo_chi_tieu()
    print("3. Danh sách hiện có:")
    for row in danh_sach:
        print("  ", row)

    # Thống kê
    print(f"4. Tổng chi tiêu: {tinh_tong_chi_tieu():,.0f} VNĐ")
    print("5. Thống kê theo danh mục:")
    for dm, tien in thong_ke_theo_danh_muc():
        print(f"   - {dm}: {tien:,.0f} VNĐ")

