username = "isna"
password = "012"
pin = "012012"
saldo = 5000000
akun_terblokir = False
kesempatan_login = 3
print("====================================================")
print("Selamat Datang di ATM MBBM (My Beloved Bunda Muach)")
print("====================================================")

while kesempatan_login > 0:
    username_input = input("masukkan username: ")
    password_input = input("masukkan password: ")

    username_valid = username_input == username
    password_valid = password_input == password

    if username_valid and password_valid:
        print("\nLogin Berhasil!")
        break
    else:
        kesempatan_login = kesempatan_login - 1

        if not username_valid and not password_valid:
            print("\nUsername dan Password yang anda masukkan salah!")
        elif not username_valid:
            print("\nUsername yang anda masukkan salah!")
        else:
            print("\nPassword yang anda masukkan salah!")

        if kesempatan_login > 0:
            print(f"sisa kesempatan login anda: {kesempatan_login}")
        else:
            print("\nAnda Telah Gagal Login Sebanyak 3 Kali, AKUN ANDA TERBLOKIR!")
            print("Program dihentikan demi keamanan akun anda!")
            akun_terblokir = True

while not akun_terblokir:
    print("\n=====================================")
    print("         menu Utama ATM MBBM          ")
    print("=====================================")
    print("1. Transfer Uang")
    print("2. Logout (Keluar dari ATM MBBM)")

    pilihan = input("Masukkan Pilihan Anda (1/2): ")

    if pilihan == "1":
        lanjut_transfer = "y"

        while lanjut_transfer == "y" and not akun_terblokir:
            print("\n=======================================")
            print("          Menu Transfer Uang")
            print("=======================================")
            print(f"saldo Anda Saat ini: Rp{saldo:,}")

            penerima = input("masukkan username penerima: ")

            nominal_valid = False
            while not nominal_valid:
                nominal = float(input("Masukkan Nominal Transfer (Rp50.000 - Rp1.000.000): Rp"))

                if nominal < 50000:
                    print("Nominal Minimal Transfer Adalah Rp50.000")
                elif nominal > 1000000:
                    print("Nominal Maksimal Transfer Adalah Rp1.000.000")
                elif nominal > saldo:
                    print("Saldo Anda Tidak Mencukupi Untuk Melakukan Transaksi Ini!")
                else:
                    nominal_valid = True

            kesempatan_pin = 3
            pin_berhasil = False

            while kesempatan_pin > 0:
                pin_input = input("masukkan PIN konfirmasi Transaksi: ")

                if pin_input == pin:
                    saldo = saldo - nominal
                    pin_berhasil = True

                    print("\n==================================")
                    print("      STRUK BUKTI TRANSFER")
                    print("==================================")
                    print(f"Pengirim   : {username}")
                    print(f"Penerima   : {penerima}")
                    print(f"Nominal    : Rp{nominal:,}")
                    print(f"Sisa Saldo : Rp{saldo:,}")
                    print("status     : TRANSAKSI BERHASIL!")
                    print("==================================")
                    break
                else:
                    kesempatan_pin = kesempatan_pin - 1
                    print("PIN yang anda masukkan salah")
                    if kesempatan_pin > 0:
                        print(f"Sisa Kesempatan PIN :{kesempatan_pin}x")
                    else:
                        print("AKUN DIBLOKIR: Anda salah memasukkan PIN sebanyak 3 kali.")
                        print("Program dihentikan demi keamanan akun anda!")
                        akun_terblokir = True


            if pin_berhasil and not akun_terblokir:
                print("\ny = yes")
                print("n = no")
                lanjut_transfer = input("Apakah pengguna ingin melakukan transfer lagi (y/n)? :").lower()
                
    elif pilihan == "2":
        print("\nTerima Kasih Telah Menggunaan ATM MBBM (My Beloved Bunda Muach). Sampai Jumpa lagi")
        break
    else:
        print("Pilihan Tidak Valid! Silahkan pilih 1 atau 2")