print('Staging Manipulasi List')
data_buah = ['jeruk', 'mangga', 'apel']
print(f'List data buah = {data_buah}')

data_buah1 = [buah.capitalize() for buah in data_buah]

# mengakses elemen/item indeks ke 1
data1 = data_buah1[1]
print(f'Data pertama adalah : {data1}')

data_terakhir = data_buah1[-1]
print(f'Data terakhir adalah : {data_terakhir}')

