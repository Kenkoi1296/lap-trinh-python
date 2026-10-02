danh_sach_sinh_vien = [
    {"ma_sv": "SV01", "ten_sv": "Nguyen Trung Kien", "nganh": "CNTT", "diem_tb": 8.5, "trang_thai": "Dang hoc"},
    {"ma_sv": "SV02", "ten_sv": "Tran Van Huy", "nganh": "Kinh Te", "diem_tb": 6.0, "trang_thai": "Dang hoc"},
    {"ma_sv": "SV03", "ten_sv": "Dang Quang Hung", "nganh": "CNTT", "diem_tb": 3.5, "trang_thai": "Canh cao"},
    {"ma_sv": "SV04", "ten_sv": "Dinh Dang Hai Anh", "nganh": "CNTT", "diem_tb": 9.2, "trang_thai": "Dang hoc"}, 
    {"ma_sv": "SV05", "ten_sv": "Pham Duong", "nganh": "CNTT", "diem_tb": 5.0, "trang_thai": "Dang hoc"}, #[cite: 3]
    {"ma_sv": "SV06", "ten_sv": "Hoang Ngoc Huyen", "nganh": "Kinh Te", "diem_tb": 4.5, "trang_thai": "Dang hoc"}, #[cite: 2]
    {"ma_sv": "SV07", "ten_sv": "Chinh", "nganh": "Luat", "diem_tb": 4.9, "trang_thai": "Dang hoc"}, #[cite: 3]
    {"ma_sv": "SV08", "ten_sv": "Aly", "nganh": "Ngon Ngu", "diem_tb": 2.5, "trang_thai": "Canh cao"}, #[cite: 2]
]
danh_sach_tot_nghiep = []

def hien_thi_danh_sach_sv():
    print("\n" + "=" * 65)
    print(f"{'Ma SV':<10}{'Ho va Ten':<20}{'Nganh':<15}{'Diem TB':<10}{'Trang thai':<15}")
    print("-" * 65)
    for sv in danh_sach_sinh_vien:
        print(f"{sv['ma_sv']:<10}{sv['ten_sv']:<20}{sv['nganh']:<15}{sv['diem_tb']:<10.1f}{sv['trang_thai']:<15}")
    print("=" * 65)

def tim_sv_theo_ma(ma_sv):
    for sv in danh_sach_sinh_vien:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None

def xem_sv_canh_cao():
    sv_canh_cao = [sv for sv in danh_sach_sinh_vien if sv["trang_thai"] == "Canh cao"]
    if len(sv_canh_cao) == 0:
        print("-> Khong co sinh vien nao bi canh cao hoc tap.")
        return
    
    print("\nDANH SACH SINH VIEN BI CANH CAO HOC TAP:")
    for sv in sv_canh_cao:
        print(f"  {sv['ma_sv']} - {sv['ten_sv']} - Diem: {sv['diem_tb']}")

def them_sinh_vien(ma_sv, ten_sv, nganh, diem_tb):
    if tim_sv_theo_ma(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai, khong the them.")
        return
    
    trang_thai = "Canh cao" if diem_tb < 4.0 else "Dang hoc"
    
    danh_sach_sinh_vien.append({
        "ma_sv": ma_sv, 
        "ten_sv": ten_sv, 
        "nganh": nganh, 
        "diem_tb": diem_tb, 
        "trang_thai": trang_thai
    })
    print(f"-> Da them sinh vien {ten_sv} ({ma_sv}) thanh cong.")

def cap_nhat_diem(ma_sv, diem_moi):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien ma {ma_sv}.")
        return
    
    if sv["trang_thai"] == "Tot nghiep":
         print(f"-> Sinh vien {ma_sv} da tot nghiep, khong the sua diem.")
         return

    sv["diem_tb"] = diem_moi
    sv["trang_thai"] = "Canh cao" if diem_moi < 4.0 else "Dang hoc"
    print(f"-> Cap nhat diem cho sinh vien {sv['ten_sv']} thanh cong.")

def xet_tot_nghiep(ma_sv):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien ma {ma_sv}.")
        return
    
    if sv["trang_thai"] == "Tot nghiep":
        print(f"-> Sinh vien {ma_sv} da tot nghiep tu truoc.")
        return
        
    if sv["diem_tb"] < 5.0:
        print(f"-> Sinh vien {sv['ten_sv']} chua du dieu kien tot nghiep (Diem < 5.0).")
        return
        
    sv["trang_thai"] = "Tot nghiep"
    danh_sach_tot_nghiep.append({
        "ma_sv": ma_sv,
        "ten_sv": sv["ten_sv"],
        "nganh": sv["nganh"],
        "diem_tb": sv["diem_tb"]
    })
    print(f"-> Xet duyet thanh cong! Sinh vien {sv['ten_sv']} da tot nghiep.")

def thong_ke_tot_nghiep():
    if len(danh_sach_tot_nghiep) == 0:
        print("-> Chua co sinh vien nao tot nghiep.")
        return
    
    print("\nDANH SACH SINH VIEN DA TOT NGHIEP:")
    for sv in danh_sach_tot_nghiep:
         print(f"  {sv['ma_sv']} - {sv['ten_sv']} - {sv['nganh']} - Diem: {sv['diem_tb']}")
    print(f"\n>>> TONG SO SINH VIEN TOT NGHIEP: {len(danh_sach_tot_nghiep)} sinh vien")

def nhap_diem(loi_nhac):
    while True:
        try:
            diem = float(input(loi_nhac))
            if 0 <= diem <= 10:
                return diem
            else:
                print("-> Diem phai tu 0 den 10. Vui long nhap lai.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap mot so (vi du: 8.5).")

def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach tat ca sinh vien")
    print("2. Xem sinh vien bi canh cao hoc tap")
    print("3. Them sinh vien moi")
    print("4. Cap nhat diem sinh vien")
    print("5. Xet tot nghiep")
    print("6. Thong ke danh sach da tot nghiep")
    print("0. Thoat chuong trinh")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        
        if lua_chon == "1":
            hien_thi_danh_sach_sv()
        elif lua_chon == "2":
            xem_sv_canh_cao()
        elif lua_chon == "3":
            ma_sv = input("Nhap ma SV moi: ").strip().upper()
            ten_sv = input("Nhap ten sinh vien: ").strip().title()
            nganh = input("Nhap nganh hoc: ").strip().upper()
            diem_tb = nhap_diem("Nhap diem trung binh: ")
            them_sinh_vien(ma_sv, ten_sv, nganh, diem_tb)
        elif lua_chon == "4":
            ma_sv = input("Nhap ma SV can cap nhat: ").strip().upper()
            diem_moi = nhap_diem("Nhap diem moi: ")
            cap_nhat_diem(ma_sv, diem_moi)
        elif lua_chon == "5":
            ma_sv = input("Nhap ma SV can xet tot nghiep: ").strip().upper()
            xet_tot_nghiep(ma_sv)
        elif lua_chon == "6":
            thong_ke_tot_nghiep()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    chay_chuong_trinh()