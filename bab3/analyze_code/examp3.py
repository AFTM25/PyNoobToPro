import os
# Hal yang sama pada examp2, sedikit revisi dengan menggunakna fungsi bawaan

bil1 = int(input('Masukkan bilangan pertama: '))
bil2 = int(input('Masukkan bilangan kedua: '))
bil3 = int(input('Masukkan bilangan ketiga: '))

angka_terbesar = max(bil1, bil2, bil3)
angka_terkecil = min(bil1, bil2, bil3)

name_os = os.name
match name_os:
  case 'posix' : os.system('clear')
  case 'nt' : os.system('cls')
print('\n' + '+' + 50 * '-' + '+')
print(f'Angka terbesar adalah: {angka_terbesar}')
print(f'Angka terkecil adalah: {angka_terkecil}')