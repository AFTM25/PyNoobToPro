print('Staging Manipulasi List')
data_buah = ['jeruk', 'mangga', 'apel']
print(f'List data buah = {data_buah}')

data_buah1 = [buah.capitalize() for buah in data_buah]

# mengakses elemen/item indeks ke 1
data1 = data_buah1[1]
print(f'Data pertama adalah : {data1}')

data_terakhir = data_buah1[-1]
print(f'Data terakhir adalah : {data_terakhir}')

# mengetahui panjang atau jumlah item pada list
jumlah_data = len(data_buah1)
print(f'Jumlah data pada list buah adalah {jumlah_data}\n')

# Menambah item list dengan menggunakan insert(indeks, newItem)
data_buah1.insert(0, 'Stroberi')
print(f'Data buah setelah di insert = {data_buah1}\n')

# Menambahkan item list dengan posisi terakhir
data_buah1.append('Nanas')
print(f'Data buah setelah di append = {data_buah1}\n')

# Menambahkan data list dengan data list baru
data_buah = ['Pepaya', 'Belimbing', 'Semangka']
data_buah1.extend(data_buah)
print(f'Data buah setelah di extend = {data_buah1}')
print(f'Jumlah nya sekarang adalah {len(data_buah1)} item\n')

# Merubah item pada list dengan index 
data_buah1[1] = 'Melon'
print(f'Data buah setelah di ubah = {data_buah1}\n')

# Menghapus item
data_buah1.remove('Pepaya')
print(f'Data buah setelah di remove = {data_buah1}\n')

# Menghapus item terakhir
del_data = data_buah1.pop()
print(f'Data buah sekarang adalah {data_buah1}')
print(f'Item yang dihapus adalah {del_data}')

