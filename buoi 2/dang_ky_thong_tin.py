ho_ten = input("Nhap ho ten: ")
ho_ten_chuan = " ".join(ho_ten.split()).title()

while True:
    sdt = input("Nhap so dien thoai (10 ky tu): ")
    if len(sdt) == 10:
        break
    print("=> Sai định dạng! Số điện thoại phải có đúng 10 ký tự.")

while True:
    email = input("Nhap email: ")
    if "@" in email:
        break
    print("=> Sai định dạng! Email phải chứa ký tự '@'.")

print("\n--- THÔNG TIN ĐÃ ĐĂNG KÝ ---")
print(f"Ho ten: {ho_ten_chuan}")
print(f"So dien thoai: {sdt}")
print(f"Email: {email}")