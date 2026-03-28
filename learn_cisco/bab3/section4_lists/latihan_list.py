import time
'''
Latihan List: Manajemen Stok Gudang
---

Skenario: Sistem Inventaris Barang Masuk

Kamu sedang mengelola rak penyimpanan barang di gudang. Saat ini, ada beberapa barang yang baru datang dan harus masuk ke dalam sistem pendataan menggunakan `list`.

Tugasnya:
Tulis sebuah program untuk mensimulasikan alur keluar-masuk barang berikut:

Step 1: Buat sebuah List bernama `stok_gudang` yang berisi barang awal: "Kabel LAN", "Router", dan "Switch".
Step 2:Gunakan method `append()` untuk menambahkan satu barang baru yang baru saja datang dari supplier: "Access Point".
Step 3:Ternyata ada kiriman mendadak sebanyak 3 jenis barang (misal: "Crimping Tool", "Tester", "RJ45"). Gunakan `for loop` dan `input()` untuk meminta pengguna memasukkan ketiga nama barang tersebut ke dalam `stok_gudang`.
Step 4:Supervisor (SPV) menginformasikan bahwa barang terakhir yang Adit masukkan tadi (barang ke-3 dari input) salah kirim dan harus segera dihapus dari list.
Step 5:Ada barang prioritas tinggi yaitu "Server Rack" yang harus diletakkan di urutan paling pertama agar mudah dicek
'''

# Step 1
stok_gudang = ["Kabel LAN", "Router", "Switch"]
print(f'Stok awal di gudang: {', '.join(stok_gudang)}\n')
time.sleep(2)

# Step 2
barang_baru = 'Access Point'
stok_gudang.append(barang_baru)
print(f'Stok setelah ada penambahan barang baru: {stok_gudang}\n')
time.sleep(2)

# Step 3
print('Ada kiriman mendadak sebanyak 3 jenis barang. Silakan masukkan nama barang tersebut')
for barang_datang_mendadak in range(3):
  input_barang = input('Masukkan nama barang yang baru datang secara mendadak: ')
  stok_gudang.append(input_barang)
print(f'Stok setelah ada kiriman mendadak: {stok_gudang}\n')
time.sleep(2)

# Step 4 
del stok_gudang[-1]
print(f'Stok setelah menghapus barang terakhir: {stok_gudang}\n')
time.sleep(2)

# Step 5
barang_prioritas = 'Server Rack'
stok_gudang.insert(0, barang_prioritas)
print(f'Stok setelah menambahkan barang prioritas: {stok_gudang}\n')
time.sleep(2)
