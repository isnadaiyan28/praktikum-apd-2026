import inquirer
from database import status
from fungsi_dan_library import bersihkan_layar, tampilkan_header
from menu_login import proses_login, proses_register, proses_logout
import CRUD

def main():
    while True:
        bersihkan_layar()
        tampilkan_header("APLIKASI PENGELOLAAN PET CARE & PENITIPAN HEWAN")
        
        if not status["status_login"]:
            pertanyaan_awal = [
                inquirer.List('menu',
                              message="Silakan pilih menu utama:",
                              choices=[
                                  ("Login ke Sistem", "1"),
                                  ("Register Akun Baru", "2"),
                                  ("Keluar Program", "3")
                              ],)
            ]
            jawaban = inquirer.prompt(pertanyaan_awal)
            if not jawaban:
                break
                
            pilihan_awal = jawaban['menu']
            
            if pilihan_awal == "1":
                proses_login()
            elif pilihan_awal == "2":
                proses_register()
            elif pilihan_awal == "3":
                print("\nTerima kasih telah menggunakan sistem Pet Care!")
                break

        else:
            print(f"Status Sesi : Login sebagai [{status['role_login'].upper()}] ({status['user_aktif']})")
            print("=" * 70)
            
            pertanyaan_menu = [
                inquirer.List('menu',
                              message="Menu Navigasi Pet Care:",
                              choices=[
                                  ("Lihat Data Hewan & Status (Read)", "1"),
                                  ("Tambah Data Hewan Baru (Create)", "2"),
                                  ("Perbarui Status Perawatan (Update)", "3"),
                                  ("Hapus Data Hewan (Delete - Khusus Admin)", "4"),
                                  ("Logout dari Akun", "5")
                              ],)
            ]
            
            jawaban_menu = inquirer.prompt(pertanyaan_menu)
            if not jawaban_menu:
                continue
                
            pilihan_menu = jawaban_menu['menu']
            
            if pilihan_menu == "1":
                CRUD.lihat_data_pet()
            elif pilihan_menu == "2":
                CRUD.tambah_data_pet()
            elif pilihan_menu == "3":
                CRUD.perbarui_status_pet()
            elif pilihan_menu == "4":
                CRUD.hapus_data_pet()
            elif pilihan_menu == "5":
                proses_logout()
                
            input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()