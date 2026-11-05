from database import data_akun, status
from fungsi_dan_library import cetak_pesan

def proses_login():
    print("\n--- MENU LOGIN ---")
    username_input = input("Username: ").strip()
    password_input = input("Password: ").strip()

    try:
        if not username_input or not password_input:
            raise ValueError("Username dan Password tidak boleh kosong!")
        if username_input not in data_akun:
            raise KeyError("Username tidak ditemukan!")
        if data_akun[username_input]["password"] != password_input:
            raise ValueError("Password yang dimasukkan salah!")
    except (ValueError, KeyError) as e:
        cetak_pesan(str(e), "error")
    else:
        status["status_login"] = True
        status["user_aktif"] = username_input
        status["role_login"] = data_akun[username_input]["role"]
        cetak_pesan(
            f"Selamat datang, {status['user_aktif']} (Role: {status['role_login'].upper()})!",
            "sukses"
        )
    finally:
        input("\nTekan Enter untuk melanjutkan...")

def proses_register():
    print("\n--- MENU REGISTER ---")
    try:
        u_baru = input("Buat Username baru: ").strip()
        if not u_baru:
            raise ValueError("Username baru tidak boleh kosong!")
        if u_baru in data_akun:
            raise KeyError("Username sudah digunakan oleh akun lain!")
        
        p_baru = input("Buat Password baru: ").strip()
        if len(p_baru) < 4:
            raise ValueError("Password minimal terdiri dari 4 karakter!")
            
    except (ValueError, KeyError) as e:
        cetak_pesan(str(e), "error")
    else:
        data_akun[u_baru] = {"password": p_baru, "role": "user"}
        cetak_pesan("Registrasi akun baru berhasil! Silakan login.", "sukses")
    finally:
        input("\nTekan Enter untuk melanjutkan...")

def proses_logout():
    status["status_login"] = False
    status["role_login"] = ""
    status["user_aktif"] = ""
    cetak_pesan("Berhasil logout dari sistem.", "info")