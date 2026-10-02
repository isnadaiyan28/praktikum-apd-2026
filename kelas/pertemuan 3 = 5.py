batas = 5
for i in range(batas):
    print ("Perulangan ke-", i)

nilai = [75, 60, 80, 60, 50]
for item in nilai:
    if item > 70:
        print (item, "lulus")
    else:
        print ("tidak lulus")
    print (item)

#range (start, stop, step) *kalau satu angka masukknya ke stop
for i in range(5, 0, -1):
    print (i)

#nested if
for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
    for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
        print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi

#perulangan while
jawab = "ya"
hitung = 0
while(jawab == "ya"):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
print(f"Total Perulangan : {hitung}")

#kontrol perulangan 
##break
for i in range(10):
    if i == 5:
        break
    print(i)

##continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")


for i in range(10):
    if i == 0:
        continue
    elif i == 5:
        break
    else:
        print (i)

#studi kasus
jumlah_uang_saku_awal = int(input("masukkan jumlah uang saku anda:"))
pengeluaran = int(input("masukkan pengeluaran anda:"))
sisa_uang_saku = jumlah_uang_saku_awal
while sisa_uang_saku != 0:
    sisa_uang_saku = int(jumlah_uang_saku_awal - pengeluaran)
    pengeluaran = int(input("masukkan pengeluaran anda lagi"))
    print (sisa_uang_saku)
print (pengeluaran)