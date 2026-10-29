import os

data_akun = {
    "admin": {"password": "1234", "role": "admin"},
    "isna": {"password": "2808", "role": "user"}
}

data_pet = {
    "P001": {
        "nama": "Abas",
        "jenis": "Kucing Persia",
        "pemilik": "Jasmine",
        "layanan": "Grooming & Penitipan",
        "status": "Belum Dimandikan"
    },
    "P002": {
        "nama": "Aren",
        "jenis": "Kucing Domestik",
        "pemilik": "Rani",
        "layanan": "Vaksinasi & Check-up",
        "status": "Menunggu Vaksin"
    }
}

status_login = False
role_login = ""
user_aktif = ""

def main():
    global status_login, role_login, user_aktif
    
    while True:
        bersihkan_layar()
        tampilkan_header("APLIKASI PENGELOLAAN PET CARE & PENITIPAN HEWAN")
        
        if not status_login:
            print("1. Login")
            print("2. Register (Pengguna Baru)")
            print("3. Keluar Program")
            
            pilihan_awal = input("\nPilih menu (1-3): ").strip()
            
            if pilihan_awal == "1":
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
                    print(f"\n[LOGIN GAGAL]: {e}")
                else:
                    status_login = True
                    user_aktif = username_input
                    role_login = data_akun[username_input]["role"]
                    print(f"\n[LOGIN SUKSES]: Selamat datang, {user_aktif} (Role: {role_login.upper()})!")
                finally:
                    input("\nTekan Enter untuk melanjutkan...")

            elif pilihan_awal == "2":
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
                    print(f"\n[REGISTRASI GAGAL]: {e}")
                else:
                    data_akun[u_baru] = {
                        "password": p_baru,
                        "role": "user"
                    }
                    print("\n[SUKSES]: Registrasi akun baru berhasil! Silakan login.")
                finally:
                    input("\nTekan Enter untuk melanjutkan...")

            elif pilihan_awal == "3":
                print("\nTerima kasih telah menggunakan sistem Pet Care!")
                break
            else:
                print("\nPilihan menu tidak valid!")
                input("\nTekan Enter untuk melanjutkan...")

        else:
            print(f"Status Sesi : Login sebagai [{role_login.upper()}] ({user_aktif})")
            print("=" * 60)
            print("1. Lihat Data Hewan & Status (Read)")
            print("2. Tambah Data Hewan (Create)")
            print("3. Perbarui Status Perawatan (Update)")
            print("4. Hapus Data Hewan (Delete - Khusus Admin)")
            print("5. Logout")
            
            pilihan_menu = input("\nPilih menu (1-5): ").strip()
            
            if pilihan_menu == "1":
                lihat_data_pet()
            elif pilihan_menu == "2":
                tambah_data_pet()
            elif pilihan_menu == "3":
                perbarui_status_pet()
            elif pilihan_menu == "4":
                hapus_data_pet()
            elif pilihan_menu == "5":
                status_login = False
                role_login = ""
                user_aktif = ""
                print("\nBerhasil logout dari sistem.")
            else:
                print("\nPilihan menu tidak valid!")
                
            input("\nTekan Enter untuk kembali ke menu...")

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header(judul):
    print("=" * 60)
    print(f"{judul:^60}")
    print("=" * 60)

def dapatkan_status_satuans():
    return {
        "1": "Sudah Grooming",
        "2": "Sudah Diberi Makan",
        "3": "Selesai Vaksin / Check-up"
    }

def hitung_total_hewan():
    return len(data_pet)

def validasi_id_pet(id_input):
    if not id_input.isalnum():
        return False, "ID Hewan hanya boleh berisi kombinasi huruf dan angka!"
    if id_input in data_pet:
        return False, "ID Hewan sudah terdaftar di sistem!"
    return True, "Valid"

def cari_pet_by_id(id_target):
    if id_target in data_pet:
        return data_pet[id_target]
    return None

def hitung_hewan_by_status_rekursif(keys_list, status_target, index=0):
    if index >= len(keys_list):
        return 0
    key_saat_ini = keys_list[index]
    is_match = 1 if data_pet[key_saat_ini]["status"] == status_target else 0
    return is_match + hitung_hewan_by_status_rekursif(keys_list, status_target, index + 1)

def lihat_data_pet():
    tampilkan_header("DAFTAR HEWAN & STATUS PERAWATAN")
    total = hitung_total_hewan()
    if total == 0:
        print("Belum ada data hewan terdaftar.")
    else:
        print(f"{'No':<4} | {'ID':<6} | {'Nama Hewan':<12} | {'Jenis':<15} | {'Pemilik':<10} | {'Layanan':<20} | {'Status'}")
        print("-" * 90)
        no = 1
        for id_pet, info in data_pet.items():
            print(f"{no:<4} | {id_pet:<6} | {info['nama']:<12} | {info['jenis']:<15} | {info['pemilik']:<10} | {info['layanan']:<20} | {info['status']}")
            no += 1
        print("-" * 90)
        keys = list(data_pet.keys())
        jumlah_grooming = hitung_hewan_by_status_rekursif(keys, "Sudah Grooming")
        print(f"Total Hewan Terdaftar    : {total}")
        print(f"Status 'Sudah Grooming' : {jumlah_grooming} ekor (dihitung via Fungsi Rekursif)")
    print("=" * 90)

def tambah_data_pet():
    tampilkan_header("TAMBAH DATA HEWAN BARU (CREATE)")
    try:
        id_pet = input("Masukkan ID Hewan (Contoh: P003): ").strip().upper()
        if not id_pet:
            raise ValueError("ID Hewan tidak boleh kosong!")
        valid, pesan = validasi_id_pet(id_pet)
        if not valid:
            raise ValueError(pesan)
        nama_pet = input("Masukkan Nama Hewan: ").strip()
        if not nama_pet:
            raise ValueError("Nama hewan tidak boleh kosong!")
        jenis_pet = input("Masukkan Jenis/Ras Hewan: ").strip()
        pemilik_pet = input("Masukkan Nama Pemilik: ").strip()
        layanan_pet = input("Masukkan Jenis Layanan: ").strip()
        if not jenis_pet or not pemilik_pet or not layanan_pet:
            raise ValueError("Semua atribut data hewan wajib diisi secara lengkap!")
    except ValueError as e:
        print(f"\n[ERROR/GAGAL]: {e}")
    else:
        status_awal = "Belum Dirawat / Masuk Penitipan"
        data_pet[id_pet] = {
            "nama": nama_pet, "jenis": jenis_pet, "pemilik": pemilik_pet,
            "layanan": layanan_pet, "status": status_awal
        }
        print(f"\n[SUKSES]: Data hewan '{nama_pet}' (ID: {id_pet}) berhasil ditambahkan!")
    finally:
        print("Proses penambahan data selesai.")

def perbarui_status_pet():
    tampilkan_header("PERBARUI STATUS PERAWATAN HEWAN (UPDATE)")
    if hitung_total_hewan() == 0:
        print("Data kosong, tidak ada data hewan yang bisa diubah.")
        return

    keys_pet = list(data_pet.keys())
    for index, k in enumerate(keys_pet):
        print(f"[{index}] ID: {k} | Nama: {data_pet[k]['nama']} | Pemilik: {data_pet[k]['pemilik']} | Status: {data_pet[k]['status']}")

    try:
        input_idx = input("\nPilih nomor indeks data hewan yang ingin diperbarui: ").strip()
        if not input_idx.isdigit():
            raise TypeError("Indeks pilihan harus berupa angka bulat positif!")
        idx = int(input_idx)
        if idx < 0 or idx >= len(keys_pet):
            raise IndexError("Indeks yang dimasukkan di luar jangkauan daftar data!")
        target_id = keys_pet[idx]
        pet_info = cari_pet_by_id(target_id)
        
        print(f"\nHewan Terpilih: {pet_info['nama']} (Milik {pet_info['pemilik']})")
        print("Pilihan Status Perawatan:")
        print("1. Sudah Grooming\n2. Sudah Diberi Makan\n3. Selesai Vaksin / Check-up\n4. Input Status Kustom")
        
        opsi_status = dapatkan_status_satuans()
        pilihan = input("Masukkan pilihan (1-4): ").strip()
        
        if pilihan in opsi_status:
            status_baru = opsi_status[pilihan]
        elif pilihan == "4":
            status_baru = input("Ketik status perawatan baru: ").strip()
            if not status_baru:
                raise ValueError("Status kustom tidak boleh kosong!")
        else:
            raise KeyError("Pilihan status tidak ada dalam menu pilihan!")
    except (TypeError, IndexError, ValueError, KeyError) as e:
        print(f"\n[ERROR/GAGAL]: {e}")
    else:
        data_pet[target_id]['status'] = status_baru
        print(f"\n[SUKSES]: Status perawatan untuk {pet_info['nama']} berhasil diperbarui menjadi '{status_baru}'!")
    finally:
        print("Proses pembaruan status selesai.")

def hapus_data_pet():
    tampilkan_header("HAPUS DATA HEWAN (DELETE - KHUSUS ADMIN)")
    if role_login != "admin":
        print("[AKSES DITOLAK]: Maaf, hanya pengguna dengan role 'ADMIN' yang diizinkan menghapus data!")
        return
    if hitung_total_hewan() == 0:
        print("Data kosong, tidak ada data hewan yang bisa dihapus.")
        return

    keys_pet = list(data_pet.keys())
    for index, k in enumerate(keys_pet):
        print(f"[{index}] ID: {k} | Nama: {data_pet[k]['nama']} | Pemilik: {data_pet[k]['pemilik']}")

    try:
        input_idx = input("\nMasukkan indeks data yang ingin dihapus: ").strip()
        if not input_idx.isdigit():
            raise TypeError("Indeks harus berupa angka integer!")
        idx = int(input_idx)
        if idx < 0 or idx >= len(keys_pet):
            raise IndexError("Indeks tidak terdaftar dalam pilihan data!")
    except (TypeError, IndexError) as e:
        print(f"\n[ERROR/GAGAL]: {e}")
    else:
        target_id = keys_pet[idx]
        nama_dihapus = data_pet[target_id]['nama']
        del data_pet[target_id]
        print(f"\n[SUKSES]: Data hewan '{nama_dihapus}' (ID: {target_id}) berhasil dihapus dari sistem!")
    finally:
        print("Proses penghapusan data selesai.")

if __name__ == "__main__":
    main()