# Sebuah program yang membaca serangkaian angka 
# dan menghitung berapa banyak angka genap dan berapa banyak angka ganjil. 
# Program berhenti ketika angka nol dimasukkan
angka_genap = 0
angka_ganjil = 0

# masukkan nilai 
angka = int(input('Masukkan angka atau 0 untuk stop: '))

while angka != 0:
  if angka % 2 == 1:
    angka_ganjil += 1
  else:
    angka_genap += 1

  angka = int(input('Masukkan angka atau 0 untuk stop: '))

print('Jumlah Angka ganjil = ', angka_ganjil)
print('Jumlah angka genap = ', angka_genap)
