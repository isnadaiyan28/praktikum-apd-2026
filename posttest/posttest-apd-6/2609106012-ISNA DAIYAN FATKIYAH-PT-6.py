import os 

# Database akun pengguna menggunakan Dictionary (Key: username, Value: dictionary password & role)
data_akun = {
    "admin": {
        "password": "1234",
        "role": "admin"
    },
    "isna": {
        "password": "2808",
        "role": "user"
    }
}

# Database pet menggunakan Dictionary (Key: ID_Hewan, Value: dictionary informasi hewan)
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

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print("      APLIKASI PENGELOLAAN PET CARE & PENITIPAN HEWAN")
    print("=" * 60)
    
    if not status_login:
        print("1. Login")
        print("2. Register (Pengguna Baru)")
        print("3. Keluar Program")
        pilihan_awal = input("Pilih menu (1-3): ")
        
        if pilihan_awal == "1":
            print("\n--- MENU LOGIN ---")
            u = input("Username: ")
            p = input("Password: ")

            login_sukses = False
            if u in data_akun and data_akun[u]["password"] == p:
                login_sukses = True
                role_login = data_akun[u]["role"]
                user_aktif = u
            if login_sukses:
                print(f"\nLogin berhasil sebagai {role_login.upper()}!")
                status_login = True
            else:
                print("\nUsername atau Password salah!")
            input("\nTekan Enter untuk melanjutkan...")
                
        elif pilihan_awal == "2":
            print("\n--- MENU REGISTER ---")
            u_baru = input("Buat Username baru: ")
            
            if u_baru in data_akun:
                print("\nUsername sudah digunakan, silakan coba yang lain!")
            else:
                p_baru = input("Buat Password baru: ")
                data_akun[u_baru] = {
                    "password": p_baru,
                    "role": "user"
                }
                print("\nRegistrasi berhasil! Silakan login.")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan_awal == "3":
            print("\nTerima kasih telah menggunakan program ini.")
            break
        else:
            print("\nPilihan tidak valid!")
            input("\nTekan Enter untuk melanjutkan...")
            
    else:
        print(f"Status: Login sebagai [{role_login.upper()}] ({user_aktif})")
        print("=" * 60)
        print("1. Lihat Data Hewan & Status (Read)")
        print("2. Tambah Data Hewan (Create)")
        print("3. Perbarui Status Perawatan / Layanan (Update)")
        print("4. Hapus Data Hewan (Delete)")
        print("5. Logout")
        
        pilihan_menu = input("Pilih menu (1-5): ")
        
        if pilihan_menu == "1":
            print("\n" + "=" * 90)
            print("                        DAFTAR HEWAN & STATUS PERAWATAN")
            print("=" * 90)
            if len(data_pet) == 0:
                print("Belum ada data hewan.")
            else:
                print(f"{'No':<4} | {'ID':<6} | {'Nama Hewan':<12} | {'Jenis':<15} | {'Pemilik':<10} | {'Layanan':<20} | {'Status'}")
                print("-" * 90)
                no = 1
                for id_pet, info in data_pet.items():
                    print(f"{no:<4} | {id_pet:<6} | {info['nama']:<12} | {info['jenis']:<15} | {info['pemilik']:<10} | {info['layanan']:<20} | {info['status']}")
                    no += 1
            print("=" * 90)
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan_menu == "2":
            print("\n--- TAMBAH DATA HEWAN BARU (CREATE) ---")
            id_pet = input("Masukkan ID Hewan (Contoh: P003): ")
            if id_pet in data_pet:
                print("\nID Hewan sudah terdaftar!")
            else:
                nama_pet = input("Masukkan Nama Hewan: ")
                jenis_pet = input("Masukkan Jenis/Ras Hewan: ")
                pemilik_pet = input("Masukkan Nama Pemilik: ")
                layanan_pet = input("Masukkan Jenis Layanan: ")
                status_awal = "Belum Dirawat / Masuk Penitipan"
                
                data_pet[id_pet] = {
                    "nama": nama_pet,
                    "jenis": jenis_pet,
                    "pemilik": pemilik_pet,
                    "layanan": layanan_pet,
                    "status": status_awal
                }
                print("\nData hewan berhasil ditambahkan!")
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan_menu == "3":
            print("\n--- PERBARUI STATUS PERAWATAN HEWAN (UPDATE) ---")
            if len(data_pet) == 0:
                print("Data kosong, tidak ada yang bisa diubah.")
            else:
                keys_pet = list(data_pet.keys())
                i = 0
                while i < len(keys_pet):
                    k = keys_pet[i]
                    print(f"[{i}] ID: {k} | Nama: {data_pet[k]['nama']} | Pemilik: {data_pet[k]['pemilik']} | Status Saat Ini: {data_pet[k]['status']}")
                    i += 1
                
                idx_str = input("\nPilih nomor indeks data hewan yang ingin diperbarui statusnya: ")
                if idx_str.isdigit():
                    idx = int(idx_str)
                    if idx >= 0 and idx < len(keys_pet):
                        target_id = keys_pet[idx]
                        print(f"\nHewan dipilih: {data_pet[target_id]['nama']} (Milik {data_pet[target_id]['pemilik']})")
                        print("Pilih Perubahan Status:")
                        print("1. Sudah Grooming")
                        print("2. Sudah Diberi Makan")
                        print("3. Selesai Vaksin / Check-up")
                        print("4. Ketik Status Lainnya (Kustom)")
                        
                        pilih_status = input("Masukkan pilihan status (1-4): ")
                        
                        if pilih_status == "1":
                            data_pet[target_id]['status'] = "Sudah Grooming"
                        elif pilih_status == "2":
                            data_pet[target_id]['status'] = "Sudah Diberi Makan"
                        elif pilih_status == "3":
                            data_pet[target_id]['status'] = "Selesai Vaksin / Check-up"
                        elif pilih_status == "4":
                            data_pet[target_id]['status'] = input("Ketik status baru: ")
                        else:
                            print("\nPilihan tidak valid, status batal diubah.")

                        if pilih_status in ["1", "2", "3", "4"]:
                            print("\nStatus perawatan hewan berhasil diperbarui!")
                    else:
                        print("\nIndeks tidak ada dalam daftar!")
                else:
                    print("\nInput harus berupa angka indeks!")
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan_menu == "4":
            print("\n--- HAPUS DATA HEWAN (DELETE) ---")
            if len(data_pet) == 0:
                print("Data kosong, tidak ada yang bisa dihapus.")
            else:
                keys_pet = list(data_pet.keys())
                i = 0
                while i < len(keys_pet):
                    k = keys_pet[i]
                    print(f"[{i}] ID: {k} | Nama: {data_pet[k]['nama']}")
                    i += 1
                
                idx_str = input("\nMasukkan indeks data yang ingin dihapus: ")
                if idx_str.isdigit():
                    idx = int(idx_str)
                    if idx >= 0 and idx < len(keys_pet):
                        target_id = keys_pet[idx]
                        del data_pet[target_id]
                        print("\nData hewan berhasil dihapus!")
                    else:
                        print("\nIndeks tidak ada dalam daftar!")
                else:
                    print("\nInput harus berupa angka indeks!")
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan_menu == "5":
            status_login = False
            role_login = ""
            user_aktif = ""
            print("\nBerhasil logout.")
            input("\nTekan Enter untuk kembali...")
        else:
            print("\nPilihan menu tidak valid!")
            input("\nTekan Enter untuk kembali...")