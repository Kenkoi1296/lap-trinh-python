import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("May tinh bo tui")
        self.resize(300, 350)
        self.bieu_thuc = ""
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        layout_chinh = QVBoxLayout()
        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setStyleSheet("font-size: 20px; padding: 5px;")
        layout_chinh.addWidget(self.man_hinh)

        layout_phim = QGridLayout()
        danh_sach_phim = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), ("C", 3, 1), ("=", 3, 2), ("+", 3, 3),
        ]

        for ky_tu, hang, cot in danh_sach_phim:
            nut = QPushButton(ky_tu)
            nut.setStyleSheet("font-size: 16px; padding: 10px;")
            nut.clicked.connect(lambda checked, k=ky_tu: self.bam_nut(k))
            layout_phim.addWidget(nut, hang, cot)

        layout_chinh.addLayout(layout_phim)
        self.setLayout(layout_chinh)

    def bam_nut(self, ky_tu):
        if ky_tu == "C":
            self.bieu_thuc = ""
            self.man_hinh.setText("")
        elif ky_tu == "=":
            try:
                ket_qua = str(eval(self.bieu_thuc))
                self.man_hinh.setText(ket_qua)
                self.bieu_thuc = ket_qua
            except Exception:
                self.man_hinh.setText("Loi")
                self.bieu_thuc = ""
        else:
            self.bieu_thuc += ky_tu
            self.man_hinh.setText(self.bieu_thuc)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())
