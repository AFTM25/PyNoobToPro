print('Program ini bertujuan untuk mencari angka terbesar pada list')
data_angka = [17, 3, 11, 5, 1, 9, 7, 15, 13]
print(data_angka)

# Asumsikan nilai pertama dalam list adalah angka terbesar
terbesar = data_angka[0]

# Kemudian di telusuri dan di cek satu per satu apakah ada angka yang lebih besar dari nilai terbesar
for angka in range(1, len(data_angka)):
  if data_angka[angka] > terbesar:
    terbesar = data_angka[angka]
print(f'Angka terbesar pada list adalah {terbesar}')

for angka in range(1, len(data_angka)):
  if data_angka[angka] < terbesar:
    terbesar = data_angka[angka]
print(f'Angka terkecil pada list adalah {terbesar}\n')

# Kode di atas sama dengan seperti ini 
del data_angka[:]
del terbesar 

data_angka = [83, 88, 12, 77, 65, 10, 11]
angka_max = data_angka[0]
for angka in data_angka:
  if angka > angka_max:
    angka_max = angka
print(f'Angka terbesar pada list adalah {angka_max}')
print()

print('Program ini bertujuan untuk mencari angka yang sesuai')

# Persiapan data 
list_angka = [1,2,3,4,5,6,7,8,9,10]

# target yang ingin ditemukan 
angka_target = 7

# Ini disebut sebagai flag (bendera). Gunanya sebagai penanda status. Di awal, kita asumsikan angka belum ditemukan, maka nilainya False.
found = False

# Proses penelusuran data pada list 
for val in range(len(list_angka)):
  found = list_angka[val] == angka_target
  if found:
    break 

if found:
  print(f'Angka {angka_target} ditemukan pada index ke-{val}')
else:
  print(f'Angka {angka_target} tidak ditemukan pada list')

print('\n\n\n')

data = ['motor', 'mobil', 'pesawat', 'bajai', 'helikopter']
cari_data = 'mobil'
found = False # flag
for hasil in range(len(data)):
    found = data[hasil] == cari_data
    if found :
        break
    
if found:
    print(f'{cari_data} ditemukan pada index ke {hasil}')
else:
    print(f'{cari_data} tidak ditemukan pada index')
