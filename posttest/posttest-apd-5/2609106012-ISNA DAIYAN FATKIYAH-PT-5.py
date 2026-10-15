import os 
#Database akun pengguna (nested list : [[username, password, role]...])
data_akun = [
    ["admin", "1234", "admin"],
    ["isna", "2808", "user"]
]
#format : [[ID_Hewan, Nama_Hewan, Jenis_Hewan, Nama_Pemillik, layanan]...]
data_pet = [
    ["P001", "Abas", "Kucing Persia", "Jasmine", "Grooming & Penitipan", "Belum Dimandikan"],
    ["P002", "Aren", "Kucing Domestik", "Rani", "Vaksinasi & Check-up", "Menunggu Vaksin"]
]

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
            for akun in data_akun:
                if akun[0] == u and akun[1] == p:
                    login_sukses = True
                    role_login = akun[2]
                    user_aktif = akun[0]
                    break
            
            if login_sukses:
                print(f"\nLogin berhasil sebagai {role_login.upper()}!")
                status_login = True
            else:
                print("\nUsername atau Password salah!")
            input("\nTekan Enter untuk melanjutkan...")
                
        elif pilihan_awal == "2":
            print("\n--- MENU REGISTER ---")
            u_baru = input("Buat Username baru: ")
            
            sudah_ada = False
            for akun in data_akun:
                if akun[0] == u_baru:
                    sudah_ada = True
                    break
            
            if sudah_ada:
                print("\nUsername sudah digunakan, silakan coba yang lain!")
            else:
                p_baru = input("Buat Password baru: ")
                data_akun.append([u_baru, p_baru, "user"])
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
                i = 0
                while i < len(data_pet):
                    print(f"{i+1:<4} | {data_pet[i][0]:<6} | {data_pet[i][1]:<12} | {data_pet[i][2]:<15} | {data_pet[i][3]:<10} | {data_pet[i][4]:<20} | {data_pet[i][5]}")
                    i += 1
            print("=" * 90)
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan_menu == "2":
            print("\n--- TAMBAH DATA HEWAN BARU (CREATE) ---")
            id_pet = input("Masukkan ID Hewan (Contoh: P003): ")
            nama_pet = input("Masukkan Nama Hewan: ")
            jenis_pet = input("Masukkan Jenis/Ras Hewan: ")
            pemilik_pet = input("Masukkan Nama Pemilik: ")
            layanan_pet = input("Masukkan Jenis Layanan: ")
            status_awal = "Belum Dirawat / Masuk Penitipan"
            
            data_pet.append([id_pet, nama_pet, jenis_pet, pemilik_pet, layanan_pet, status_awal])
            print("\nData hewan berhasil ditambahkan!")
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan_menu == "3":
            print("\n--- PERBARUI STATUS PERAWATAN HEWAN (UPDATE) ---")
            if len(data_pet) == 0:
                print("Data kosong, tidak ada yang bisa diubah.")
            else:
                i = 0
                while i < len(data_pet):
                    print(f"[{i}] Nama: {data_pet[i][1]} | Pemilik: {data_pet[i][3]} | Status Saat Ini: {data_pet[i][5]}")
                    i += 1
                
                idx_str = input("\nPilih nomor indeks data hewan yang ingin diperbarui statusnya: ")
                if idx_str.isdigit():
                    idx = int(idx_str)
                    if idx >= 0 and idx < len(data_pet):
                        print(f"\nHewan dipilih: {data_pet[idx][1]} (Milik {data_pet[idx][3]})")
                        print("Pilih Perubahan Status:")
                        print("1. Sudah Grooming")
                        print("2. Sudah Diberi Makan")
                        print("3. Selesai Vaksin / Check-up")
                        print("4. Ketik Status Lainnya (Kustom)")
                        
                        pilih_status = input("Masukkan pilihan status (1-4): ")
                        
                        if pilih_status == "1":
                            data_pet[idx][5] = "Sudah Grooming"
                        elif pilih_status == "2":
                            data_pet[idx][5] = "Sudah Diberi Makan"
                        elif pilih_status == "3":
                            data_pet[idx][5] = "Selesai Vaksin / Check-up"
                        elif pilih_status == "4":
                            data_pet[idx][5] = input("Ketik status baru: ")
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
                i = 0
                while i < len(data_pet):
                    print(f"[{i}] ID: {data_pet[i][0]} | Nama: {data_pet[i][1]}")
                    i += 1
                
                idx_str = input("\nMasukkan indeks data yang ingin dihapus: ")
                if idx_str.isdigit():
                    idx = int(idx_str)
                    if idx >= 0 and idx < len(data_pet):
                        data_pet.pop(idx)
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