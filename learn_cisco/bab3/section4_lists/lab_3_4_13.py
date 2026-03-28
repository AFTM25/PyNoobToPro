# Question 1
angka = [7, 4, 3, 1, 8]
angka.insert(1, 6)
del angka[0]
angka.append(10)

# Question 2
# Hasil akhir nya menambahkan item dari kiri ke kanan
# Bukan menjumlahkan seluruh item nya
angka = [3, 8, 9, 10, 12, 11]
angka2 = []
tambah = 0 #variabel berpengaruh untuk menambahkan angka yang sudah di tambahkan sebelumnya

for angka_hasil in angka:
  tambah += angka_hasil
  angka2.append(tambah)

print(angka2)