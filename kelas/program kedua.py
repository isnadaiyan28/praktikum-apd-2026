# Program 2: Penyaring Hostel Interaktif & Konversi Rupiah
# Menggunakan Looping (While), Input Dinamis, Selection, dan Konversi Kurs

print("=== PROGRAM PENYARING HOSTEL INTERAKTIF & KONVERSI RUPIAH ===")

# Input nilai kurs dan batas maksimal budget dari pengguna
KURS_SGD_TO_IDR = float(input("Masukkan kurs 1 SGD ke IDR saat ini (misal 11500): "))
max_budget_sgd = float(input("Masukkan batas budget maksimal per malam (SGD): "))

daftar_hostel_lolos = []
tambah_lagi = "y"

# 1. LOOPING WHILE (INPUT DATA HOSTEL DINAMIS)
while tambah_lagi.lower() == "y":
    print("\n--- Input Data Hostel ---")
    nama_hostel = input("Nama Hostel/Dorm: ")
    harga_sgd = float(input(f"Harga per malam {nama_hostel} (SGD): "))
    
    # Hitung konversi ke Rupiah
    harga_idr = harga_sgd * KURS_SGD_TO_IDR
    
    # Selection untuk mengecek apakah hostel sesuai budget
    if harga_sgd <= max_budget_sgd:
        print(f"-> [LOLOS BUDGET] {nama_hostel} masuk kriteria! (Rp{harga_idr:,.2f})")
        daftar_hostel_lolos.append({
            "nama": nama_hostel, 
            "harga_sgd": harga_sgd,
            "harga_idr": harga_idr
        })
    else:
        print(f"-> [TERLALU MAHAL] {nama_hostel} melebihi budget {max_budget_sgd} SGD (Rp{harga_idr:,.2f}).")
    
    tambah_lagi = input("\nTambah data hostel lain? (y/n): ")

# 2. MENAMPILKAN HASIL DAN SIMULASI BIAYA
print("\n==========================================")
print("=== DAFTAR HOSTEL REKOMENDASI TERPILIH ===")
print("==========================================")

if len(daftar_hostel_lolos) > 0:
    for item in daftar_hostel_lolos:
        print(f"- {item['nama']}: {item['harga_sgd']} SGD / malam (Rp{item['harga_idr']:,.2f})")
    
    print("\n--- SIMULASI BIAYA MENGINAP ---")
    durasi = int(input("Berapa malam rencana menginap?: "))
    
    # Mengambil opsi hostel terhitung paling murah untuk simulasi
    hostel_termurah = min(daftar_hostel_lolos, key=lambda x: x['harga_sgd'])
    
    malam_ke = 1
    while malam_ke <= durasi:
        total_sgd = malam_ke * hostel_termurah['harga_sgd']
        total_idr = total_sgd * KURS_SGD_TO_IDR
        print(f"Menginap {malam_ke} malam di {hostel_termurah['nama']} = Total {total_sgd} SGD (Rp{total_idr:,.2f})")
        malam_ke += 1
else:
    print("Tidak ada hostel yang sesuai dengan budget Anda. Coba naikkan batas budget!")