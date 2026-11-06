from data_store import load_excel, save_excel, MOVIES_FILE, USERS_FILE, TRANSACTIONS_FILE
from prettytable import PrettyTable

def add_new_movie():
    movies = load_excel(MOVIES_FILE)
    print("\n=== TAMBAH FILM BARU ===")
    m_id = f"M{len(movies) + 1}"
    judul = input("Masukkan Judul Film: ").strip()
    genre = input("Masukkan Genre: ").strip()
    
    try:
        harga = int(input("Masukkan Harga Tiket (Rp): "))
        kapasitas = int(input("Kapasitas Kursi Studio: "))
    except ValueError:
        print("Harga dan kapasitas harus angka!")
        return
        
    studio = input("Nama Studio (Contoh: Studio 1): ").strip()
    jadwal = input("Jadwal Tayang (pisahkan dengan koma, contoh: 13:00, 16:00): ").strip()
    
    movies.append({
        "movie_id": m_id, "judul": judul, "genre": genre,
        "harga": harga, "studio": studio, "kapasitas": kapasitas, "jadwal": jadwal
    })
    save_excel(MOVIES_FILE, movies)
    print(f"Film '{judul}' berhasil ditambahkan dengan ID: {m_id}")

def update_movie_detail():
    movies = load_excel(MOVIES_FILE)
    print("\n=== UPDATE JAM TAYANG / HARGA TIKET ===")
    m_id = input("Masukkan ID Film yang diubah: ").strip().upper()
    
    selected_movie = next((m for m in movies if m["movie_id"] == m_id), None)
    if not selected_movie:
        print("ID Film tidak ditemukan!")
        return
        
    print(f"Mengedit Film: {selected_movie['judul']}")
    try:
        harga_baru = input(f"Harga Baru (Kosongkan jika tetap Rp{selected_movie['harga']}): ")
        if harga_baru:
            selected_movie["harga"] = int(harga_baru)
            
        jadwal_baru = input("Jadwal Baru (Kosongkan jika tidak berubah, pisah koma): ")
        if jadwal_baru:
            selected_movie["jadwal"] = jadwal_baru.strip()
            
        save_excel(MOVIES_FILE, movies)
        print("Data film berhasil diperbarui!")
    except ValueError:
        print("Input harga tidak valid!")

def delete_movie():
    movies = load_excel(MOVIES_FILE)
    print("\n=== HAPUS FILM (TURUN LAYAR) ===")
    m_id = input("Masukkan ID Film yang akan dihapus: ").strip().upper()
    
    new_movies = [m for m in movies if m["movie_id"] != m_id]
    if len(new_movies) < len(movies):
        save_excel(MOVIES_FILE, new_movies)
        print(f"Film dengan ID {m_id} berhasil dihapus dari sistem.")
    else:
        print("ID Film tidak ditemukan.")

def view_all_customers():
    users = load_excel(USERS_FILE)
    print("\n=== DAFTAR PELANGGAN TERDAFTAR ===")
    table = PrettyTable()
    table.field_names = ["Username", "Nama Lengkap", "Role"]
    
    for u in users:
        if u["role"] == "customer":
            table.add_row([u["username"], u["nama"], u["role"]])
    print(table)

def delete_customer_account():
    users = load_excel(USERS_FILE)
    print("\n=== HAPUS AKUN PELANGGAN (PALSU/AKUN FAKE) ===")
    usn = input("Masukkan Username Pelanggan yang akan dihapus: ").strip().lower()
    
    new_users = [u for u in users if not (u["username"] == usn and u["role"] == "customer")]
    if len(new_users) < len(users):
        save_excel(USERS_FILE, new_users)
        print(f"Akun pelanggan '{usn}' berhasil dihapus.")
    else:
        print("Username tidak ditemukan atau merupakan akun Admin.")

def view_and_update_transactions():
    transactions = load_excel(TRANSACTIONS_FILE)
    print("\n=== REKAPITULASI & KONFIRMASI TRANSAKSI ===")
    
    if not transactions:
        print("Belum ada transaksi tiket masuk.")
        return
        
    table = PrettyTable()
    table.field_names = ["Kode Booking", "Pelanggan", "Judul Film", "Harga", "Status"]
    for t in transactions:
        table.add_row([t["booking_code"], t["username"], t["judul"], f"Rp{int(t['harga']):,}", t["status"]])
    print(table)
    
    pilihan = input("\nUbah status pembayaran pelanggan? (y/n): ").strip().lower()
    if pilihan == 'y':
        code_input = input("Masukkan Kode Booking: ").strip().upper()
        selected_tx = next((t for t in transactions if t["booking_code"] == code_input), None)
        
        if selected_tx:
            print("Pilih Status Baru: 1. Lunas | 2. Pending | 3. Batal")
            st = input("Pilihan (1-3): ").strip()
            status_map = {"1": "Lunas", "2": "Pending", "3": "Batal"}
            if st in status_map:
                selected_tx["status"] = status_map[st]
                save_excel(TRANSACTIONS_FILE, transactions)
                print(f"Status transaksi {code_input} diubah menjadi {status_map[st]}!")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Kode Booking tidak ditemukan.")