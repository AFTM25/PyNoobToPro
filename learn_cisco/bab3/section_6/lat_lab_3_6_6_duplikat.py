import os 
import subprocess as sp 
if os.name == 'nt':
  sp.run('cls', shell=True)
else:
  sp.run('clear', shell=True)

# Siapkan list untuk menampung barang yang diinputkan oleh user
barang = []
duplikat = []

# Loop untuk menerima input dari user 
while True:
  input_barang = input('Masukkan nama barang (atau stop): ')
  
  if input_barang.lower() == 'stop':
    break

  if not input_barang.strip():
    print('Input tidak boleh spasi kosong. Silahkan coba lagi')
    continue

  barang.append(input_barang)

# Loop untuk memeriksa duplikat
for item in barang:
  if item not in duplikat:
    duplikat.append(item)

# Tampilkan nama barang yang sudah di input user 
print(f"{'No':^5} | {'Nama Barang':<30}")
for no, item in enumerate(duplikat):
  print(f'{no+1:^5} | {item.title():<30}')
