# --- PROSES SEQUENTIAL (Jalan berurutan dari atas ke bawah) ---
KURS_SGD_TO_IDR = 11500.0  # 1 SGD = 11.500 IDR

print("=== PROGRAM CEK BELANJA SINGAPURA ===")

# Mengambil input dari pengguna
nama_makanan = input("Masukkan nama makanan: ")
harga_sgd = float(input("Masukkan harga makanan (dalam SGD): "))
sisa_saldo_idr = float(input("Masukkan sisa saldo tabungan kamu (dalam IDR): "))

# Perhitungan konversi
harga_idr = harga_sgd * KURS_SGD_TO_IDR

print("\n--- HASIL PENGECEKAN ---")
print(f"Makanan: {nama_makanan}")
print(f"Harga dalam Rupiah: Rp{harga_idr:,.2f}")

# --- PROSES SELECTION (Pengambilan Keputusan) ---
if harga_idr > sisa_saldo_idr:
    print("Status: Batal Beli! Sisa uang tidak cukup.")
elif harga_idr > 80000:
    print("Status: Tahan Dulu! Terlalu mahal untuk dompet pengungsi.")
else:
    sisa_saldo_idr -= harga_idr  # Mengurangi saldo
    print(f"Status: Aman, Silakan Beli! Sisa saldo: Rp{sisa_saldo_idr:,.2f}")