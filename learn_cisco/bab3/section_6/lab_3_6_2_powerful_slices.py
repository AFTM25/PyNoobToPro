# Menyalin seluruh daftar 
data_buah = ['Mangga', 'Apel', 'Jeruk', 'Stroberi']
data_buah2 = data_buah[::]
data_buah[0] = 'Delima'

# Menampilkan daftar buah di list data_buah
for buah1 in range(len(data_buah)):
  print(f'{buah1 + 1} -> {data_buah[buah1]}')

print('-'*40)

# Menampilkan daftar buah2 alias copy an dari list data_buah2
for buah2 in range(len(data_buah2)):
  print(f'{buah2 + 1} -> {data_buah2[buah2]}')

print('-'*40)

# Menyalin sebagian list 
data_buah3 = data_buah2[3:6]
data_buah3.append('Melon')
data_buah3.append('Semangka')
print(data_buah3)
