import inquirer
from database import data_pet, status
from fungsi_dan_library import tampilkan_header, cetak_pesan, buat_tabel_pet

def hitung_total_hewan():
    return len(data_pet)

def validasi_id_pet(id_input):
    if not id_input.isalnum():
        return False, "ID Hewan hanya boleh berisi kombinasi huruf dan angka!"
    if id_input in data_pet:
        return False, "ID Hewan sudah terdaftar di sistem!"
    return True, "Valid"

def cari_pet_by_id(id_target):
    return data_pet.get(id_target, None)

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
        cetak_pesan("Belum ada data hewan terdaftar.", "peringatan")
    else:
        tabel = buat_tabel_pet(data_pet)
        print(tabel)
        
        keys = list(data_pet.keys())
        jumlah_grooming = hitung_hewan_by_status_rekursif(keys, "Sudah Grooming")
        print(f"\nTotal Hewan Terdaftar    : {total}")
        print(f"Status 'Sudah Grooming'  : {jumlah_grooming} ekor (Dihitung via Rekursif)")

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
        cetak_pesan(str(e), "error")
    else:
        status_awal = "Belum Dirawat / Masuk Penitipan"
        data_pet[id_pet] = {
            "nama": nama_pet, "jenis": jenis_pet, "pemilik": pemilik_pet,
            "layanan": layanan_pet, "status": status_awal
        }
        cetak_pesan(f"Data hewan '{nama_pet}' (ID: {id_pet}) berhasil ditambahkan!", "sukses")

def perbarui_status_pet():
    tampilkan_header("PERBARUI STATUS PERAWATAN HEWAN (UPDATE)")
    if hitung_total_hewan() == 0:
        cetak_pesan("Data kosong, tidak ada data hewan yang bisa diubah.", "peringatan")
        return

    choices_pet = [(f"ID: {k} | Nama: {data_pet[k]['nama']} (Pemilik: {data_pet[k]['pemilik']})", k) for k in data_pet.keys()]
    
    pertanyaan = [
        inquirer.List('target_id',
                      message="Pilih hewan yang ingin diperbarui statusnya:",
                      choices=choices_pet,),
    ]
    
    jawaban = inquirer.prompt(pertanyaan)
    if not jawaban:
        return
    
    target_id = jawaban['target_id']
    pet_info = cari_pet_by_id(target_id)
    
    print(f"\nHewan Terpilih: {pet_info['nama']} (Milik {pet_info['pemilik']})")
    
    pertanyaan_status = [
        inquirer.List('status_pilihan',
                      message="Pilih Status Perawatan Baru:",
                      choices=[
                          ("Sudah Grooming", "Sudah Grooming"),
                          ("Sudah Diberi Makan", "Sudah Diberi Makan"),
                          ("Selesai Vaksin / Check-up", "Selesai Vaksin / Check-up"),
                          ("Input Status Kustom (Ketik Sendiri)", "kustom")
                      ],)
    ]
    
    j_status = inquirer.prompt(pertanyaan_status)
    if not j_status:
        return
        
    try:
        if j_status['status_pilihan'] == "kustom":
            status_baru = input("Ketik status perawatan baru: ").strip()
            if not status_baru:
                raise ValueError("Status kustom tidak boleh kosong!")
        else:
            status_baru = j_status['status_pilihan']
    except ValueError as e:
        cetak_pesan(str(e), "error")
    else:
        data_pet[target_id]['status'] = status_baru
        cetak_pesan(f"Status perawatan untuk {pet_info['nama']} berhasil diperbarui menjadi '{status_baru}'!", "sukses")

def hapus_data_pet():
    tampilkan_header("HAPUS DATA HEWAN (DELETE - KHUSUS ADMIN)")
    if status["role_login"] != "admin":
        cetak_pesan("Akses Ditolak! Hanya pengguna dengan role 'ADMIN' yang diizinkan menghapus data.", "error")
        return
    if hitung_total_hewan() == 0:
        cetak_pesan("Data kosong, tidak ada data hewan yang bisa dihapus.", "peringatan")
        return

    choices_pet = [(f"ID: {k} | Nama: {data_pet[k]['nama']} (Pemilik: {data_pet[k]['pemilik']})", k) for k in data_pet.keys()]
    
    pertanyaan = [
        inquirer.List('target_id',
                      message="Pilih data hewan yang ingin DIHAPUS:",
                      choices=choices_pet,),
    ]
    
    jawaban = inquirer.prompt(pertanyaan)
    if not jawaban:
        return
        
    target_id = jawaban['target_id']
    nama_dihapus = data_pet[target_id]['nama']
    
    konfirmasi = [
        inquirer.Confirm('lanjut', message=f"Yakin ingin menghapus data hewan '{nama_dihapus}' (ID: {target_id})?", default=False)
    ]
    j_konfirm = inquirer.prompt(konfirmasi)
    
    if j_konfirm and j_konfirm['lanjut']:
        del data_pet[target_id]
        cetak_pesan(f"Data hewan '{nama_dihapus}' (ID: {target_id}) berhasil dihapus dari sistem!", "sukses")
    else:
        cetak_pesan("Penghapusan data dibatalkan.", "info")