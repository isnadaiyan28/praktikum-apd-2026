import random
from datetime import datetime
from data_store import load_excel, save_excel, MOVIES_FILE, TRANSACTIONS_FILE
from search_filter import display_movie_table
from prettytable import PrettyTable

def generate_booking_code(existing_codes):
    """Fungsi Rekursi untuk membuat kode booking unik (Modul 7.1)."""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = "TKT-" + "".join(random.choice(chars) for _ in range(6))
    if code in existing_codes:
        return generate_booking_code(existing_codes)
    return code

def render_seat_map(kapasitas, occupied_seats):
    """Menampilkan denah kursi bioskop (Nested Loop - Modul 4 & 5)."""
    print("\n  [ LAYAR CINEMA ]  ")
    print("--------------------")
    rows = "ABCDEFGH"
    row_count = (kapasitas // 4) + (1 if kapasitas % 4 != 0 else 0)
    
    seat_idx = 0
    for r in range(row_count):
        row_str = f"{rows[r]} | "
        for c in range(1, 5):
            seat_idx += 1
            if seat_idx > kapasitas:
                break
            seat_code = f"{rows[r]}{c}"
            if seat_code in occupied_seats:
                row_str += "[X] "
            else:
                row_str += f"[{seat_code}] "
        print(row_str)

def make_reservation(username):
    movies = load_excel(MOVIES_FILE)
    transactions = load_excel(TRANSACTIONS_FILE)
    
    print("\n=== RESERVASI TIKET BIOSKOP ===")
    display_movie_table(movies)
    
    movie_id = input("Masukkan ID Film yang ingin dipesan: ").strip().upper()
    selected_movie = next((m for m in movies if m["movie_id"] == movie_id), None)
    
    if not selected_movie:
        print("ID Film tidak ditemukan!")
        return
        
    jadwal_list = [j.strip() for j in str(selected_movie["jadwal"]).split(",")]
    print(f"\nJadwal Tayang {selected_movie['judul']}:")
    for idx, j in enumerate(jadwal_list, 1):
        print(f"{idx}. {j}")
        
    try:
        j_choice = int(input("Pilih Nomor Jadwal: ")) - 1
        jadwal = jadwal_list[j_choice]
    except (ValueError, IndexError):
        print("Jadwal tidak valid!")
        return

    # Ambil kursi terisi dari data transaksi Excel
    occupied_seats = [
        t["kursi"] for t in transactions
        if t["movie_id"] == movie_id and t["jadwal"] == jadwal and t["status"] != "Batal"
    ]
    
    render_seat_map(int(selected_movie["kapasitas"]), occupied_seats)
    pilih_kursi = input("Masukkan Kode Kursi (contoh: A1): ").strip().upper()
    
    try:
        if pilih_kursi in occupied_seats:
            raise ValueError("Kursi sudah dipesan oleh orang lain!")
    except ValueError as e:
        print(f"Error: {e}")
        return

    existing_codes = {t["booking_code"] for t in transactions}
    booking_code = generate_booking_code(existing_codes)
    now_str = datetime.now().strftime("%d-%m-%Y %H:%M")
    
    transactions.append({
        "booking_code": booking_code,
        "username": username,
        "movie_id": movie_id,
        "judul": selected_movie["judul"],
        "jadwal": jadwal,
        "kursi": pilih_kursi,
        "harga": selected_movie["harga"],
        "status": "Pending",  # Default status
        "tanggal": now_str
    })
    
    save_excel(TRANSACTIONS_FILE, transactions)
    print("\nReservasi Berhasil dibuat!")
    print(f"Kode Booking Anda : {booking_code}")
    print("Status Pembayaran : Pending (Silakan konfirmasi pembayaran ke Admin)")

def view_customer_history(username):
    transactions = load_excel(TRANSACTIONS_FILE)
    user_tx = [t for t in transactions if t["username"] == username]
    
    print("\n=== RIWAYAT TIKET PESANAN SAYA ===")
    if not user_tx:
        print("Belum ada riwayat pemesanan tiket.")
        return
        
    table = PrettyTable()
    table.field_names = ["Kode Booking", "Judul Film", "Jadwal", "Kursi", "Total Bayar", "Status", "Tanggal"]
    for t in user_tx:
        table.add_row([
            t["booking_code"], t["judul"], t["jadwal"], t["kursi"], 
            f"Rp{int(t['harga']):,}", t["status"], t["tanggal"]
        ])
    print(table)

def change_seat_choice(username):
    transactions = load_excel(TRANSACTIONS_FILE)
    pending_tx = [t for t in transactions if t["username"] == username and t["status"] == "Pending"]
    
    if not pending_tx:
        print("Tidak ada pesanan berstatus 'Pending' yang dapat diubah kursinya.")
        return
        
    print("\n=== TUKAR PILIHAN KURSI (BELUM DIBAYAR) ===")
    for t in pending_tx:
        print(f"Kode Booking: {t['booking_code']} | Film: {t['judul']} | Kursi Sekarang: {t['kursi']}")
        
    code_choice = input("Masukkan Kode Booking yang ingin diubah kursinya: ").strip().upper()
    selected_tx = next((t for t in pending_tx if t["booking_code"] == code_choice), None)
    
    if not selected_tx:
        print("Kode Booking tidak ditemukan atau sudah dibayar.")
        return
        
    movies = load_excel(MOVIES_FILE)
    movie_info = next((m for m in movies if m["movie_id"] == selected_tx["movie_id"]), {})
    
    occupied = [
        t["kursi"] for t in transactions
        if t["movie_id"] == selected_tx["movie_id"] and t["jadwal"] == selected_tx["jadwal"] 
        and t["status"] != "Batal" and t["booking_code"] != code_choice
    ]
    
    render_seat_map(int(movie_info.get("kapasitas", 12)), occupied)
    kursi_baru = input("Masukkan Kode Kursi Baru: ").strip().upper()
    
    if kursi_baru in occupied:
        print("Kursi baru tersebut sudah terisi!")
        return
        
    for t in transactions:
        if t["booking_code"] == code_choice:
            t["kursi"] = kursi_baru
            break
            
    save_excel(TRANSACTIONS_FILE, transactions)
    print(f"Kursi berhasil ditukar menjadi {kursi_baru}!")

def cancel_reservation(username):
    transactions = load_excel(TRANSACTIONS_FILE)
    pending_tx = [t for t in transactions if t["username"] == username and t["status"] == "Pending"]
    
    if not pending_tx:
        print("Tidak ada pesanan berstatus 'Pending' yang dapat dibatalkan.")
        return
        
    print("\n=== BATALKAN PESANAN TIKET ===")
    for t in pending_tx:
        print(f"- Kode Booking: {t['booking_code']} [{t['judul']} - Kursi {t['kursi']}]")
        
    code_choice = input("Masukkan Kode Booking yang ingin dibatalkan: ").strip().upper()
    
    found = False
    for t in transactions:
        if t["booking_code"] == code_choice and t["username"] == username and t["status"] == "Pending":
            t["status"] = "Batal"
            found = True
            break
            
    if found:
        save_excel(TRANSACTIONS_FILE, transactions)
        print(f"Pesanan {code_choice} berhasil dibatalkan!")
    else:
        print("Kode Booking tidak ditemukan atau tidak valid.")