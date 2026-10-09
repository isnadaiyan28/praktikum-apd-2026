# Program 3: Manajemen Logistik & Wisata Interaktif (Multi-Remove & Multi-Add)
# Menggunakan Tuple (Immutable), List (Mutable), dan Set (Unik)

print("=== PROGRAM MANAJEMEN LOGISTIK & WISATA ARYA & DAVID ===")

# 1. TUPLE: Dokumen Resmi & Aturan Mutlak (TIDAK BISA DIUBAH / IMMUTABLE)
dokumen_dan_aturan = (
    "Paspor RI", 
    "SG Arrival Card", 
    "KTP", 
    "Dilarang Buang Sampah & Makan di MRT (Aturan Kak Mei)"
)

print("\n1. DOKUMEN & ATURAN WAJIB (TUPLE - PERMANEN):")
for doc in dokumen_dan_aturan:
    print(f"  [FIX] {doc}")

# 2. LIST: Barang Bawaan di Ransel (BISA DIUBAH / MUTABLE)
barang_ransel = ["Laptop", "Kabel Charger", "Kaos 3 Biji", "Minyak Kayu Putih"]

print("\n2. KELOLA BARANG RANSEL (LIST):")
print("Barang Awal:", barang_ransel)

# Input Tambah Beberapa Barang (Dipisahkan Koma)
input_tambah = input("\nMasukkan barang baru (pisahkan dengan koma jika lebih dari satu): ")
if input_tambah.strip():
    items_tambah = [item.strip() for item in input_tambah.split(",")]
    for item in items_tambah:
        barang_ransel.append(item)
        print(f"-> '{item}' berhasil ditambahkan ke List!")

# Input Hapus Beberapa Barang sekaligus (Dipisahkan Koma)
input_hapus = input("\nMasukkan barang yang mau dikeluarkan (pisahkan dengan koma): ")
if input_hapus.strip():
    items_hapus = [item.strip() for item in input_hapus.split(",")]
    for item in items_hapus:
        if item in barang_ransel:
            barang_ransel.remove(item)
            print(f"-> '{item}' berhasil dihapus dari List!")
        else:
            print(f"-> '{item}' tidak ditemukan di ransel.")

print("\nBarang Ransel Terbaru:", barang_ransel)

# 3. SET: Rencana Destinasi Wisata Unik (BEBAS DUPLIKASI)
rencana_wisata = set()

print("\n3. INPUT DESTINASI WISATA (SET - OTOMATIS FILTER DUPLIKAT):")
tambah_destinasi = "y"

while tambah_destinasi.lower() == "y":
    tempat = input("Masukkan nama tempat wisata yang ingin dikunjungi: ")
    rencana_wisata.add(tempat)
    tambah_destinasi = input("Tambah tempat wisata lain? (y/n): ")

print("\n=== REKAP DESTINASI WISATA UNIK ===")
for i, tempat in enumerate(rencana_wisata, 1):
    print(f"{i}. {tempat}")