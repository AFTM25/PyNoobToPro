print(10*'='+' Copy List ' + '='*10)
# teknik menduplikat list

data_buah = ['mangga', 'apel', 'jeruk']
print(f'Data buah klasemen 1 : {data_buah}')

data_buah_copy = data_buah # pass by reference , hasil dari address akan sama dan juga ketika item nya dirubah salah satu akan mempengaruhi item pada list sebelumnya
print(f'Data buah klasemen 1 : {data_buah}')
print(f'Data buah klasemen 2(setelah di copy) : {data_buah_copy}')

# merubah nilai/isi elemen dari data buah 
data_buah[1] = 'pepaya'
print(f'Data buah klasemen 3 : {data_buah}')
print(f'Data buah klasemen 4(setelah di copy) : {data_buah_copy}')
print(f'Address data buah 1 = {hex(id(data_buah))}')
print(f'Address data buah copy = {hex(id(data_buah_copy))}')

# menyalin list tanpa sama address nya dan lebih power full
# list.copy()
data_buah_copy2 = data_buah.copy() # full duplikat
print(f'\nData buah 1 = {data_buah}')
print(f'\nData buah 2 = {data_buah_copy}')
print(f'\nData buah 3 = {data_buah_copy2}')

data_buah_copy2[1] = 'stroberi'
print(f'\nData buah 1 = {data_buah}')
print(f'\nData buah 2 = {data_buah_copy}')
print(f'\nData buah 3 = {data_buah_copy2}')
