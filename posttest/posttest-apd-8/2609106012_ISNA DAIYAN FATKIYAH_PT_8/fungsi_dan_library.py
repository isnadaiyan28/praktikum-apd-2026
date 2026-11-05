import os
from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cetak_pesan(pesan, jenis="info"):
    if jenis == "sukses":
        print(f"\n{Fore.GREEN}[SUKSES]: {pesan}{Style.RESET_ALL}")
    elif jenis == "error":
        print(f"\n{Fore.RED}[ERROR/GAGAL]: {pesan}{Style.RESET_ALL}")
    elif jenis == "peringatan":
        print(f"\n{Fore.YELLOW}[PERINGATAN]: {pesan}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.CYAN}[INFO]: {pesan}{Style.RESET_ALL}")

def tampilkan_header(judul):
    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + f"{judul:^70}")
    print(Fore.CYAN + "=" * 70 + Style.RESET_ALL)

def buat_tabel_pet(data_pet):
    tabel = PrettyTable()
    tabel.field_names = ["No", "ID", "Nama Hewan", "Jenis / Ras", "Pemilik", "Layanan", "Status Perawatan"]
    
    tabel.align["No"] = "c"
    tabel.align["ID"] = "c"
    tabel.align["Nama Hewan"] = "l"
    tabel.align["Jenis / Ras"] = "l"
    tabel.align["Pemilik"] = "l"
    tabel.align["Layanan"] = "l"
    tabel.align["Status Perawatan"] = "l"

    no = 1
    for id_pet, info in data_pet.items():
        tabel.add_row([
            no, id_pet, info['nama'], info['jenis'],
            info['pemilik'], info['layanan'], info['status']
        ])
        no += 1
    return tabel