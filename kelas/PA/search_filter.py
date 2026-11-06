from data_store import load_excel, MOVIES_FILE
from prettytable import PrettyTable

def search_and_filter_movies():
    movies = load_excel(MOVIES_FILE)
    if not movies:
        print("Belum ada film yang sedang tayang.")
        return

    print("\n=== PENCARIAN & FILTER FILM ===")
    print("1. Cari Berdasarkan Judul")
    print("2. Filter Berdasarkan Genre")
    print("3. Tampilkan Semua Film")
    pilihan = input("Pilih Menu Filter (1-3): ").strip()

    filtered = []
    if pilihan == "1":
        keyword = input("Masukkan kata kunci judul: ").strip().lower()
        filtered = [m for m in movies if keyword in str(m["judul"]).lower()]
    elif pilihan == "2":
        # Menggunakan Set untuk mengambil genre unik (Modul 6)
        genres = list({m["genre"] for m in movies})
        print("\nDaftar Genre Tersedia:")
        for idx, g in enumerate(genres, 1):
            print(f"{idx}. {g}")
        try:
            g_idx = int(input("Pilih Nomor Genre: ")) - 1
            selected_genre = genres[g_idx]
            filtered = [m for m in movies if str(m["genre"]).lower() == selected_genre.lower()]
        except (ValueError, IndexError):
            print("Pilihan genre tidak valid!")
            return
    elif pilihan == "3":
        filtered = movies
    else:
        print("Pilihan tidak valid.")
        return

    display_movie_table(filtered)

def display_movie_table(movies_list):
    if not movies_list:
        print("Film tidak ditemukan.")
        return
        
    table = PrettyTable()
    table.field_names = ["ID Film", "Judul Film", "Genre", "Studio", "Harga (Rp)", "Jadwal Tayang"]
    for m in movies_list:
        table.add_row([m["movie_id"], m["judul"], m["genre"], m["studio"], f"{m['harga']:,}", m["jadwal"]])
    print(table)