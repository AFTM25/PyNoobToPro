print('\n')
print(10*'='+' Operasi List '+'='*10)
print('\n')

data_huruf = ['a','b','c','a','c','b','c','a']

# count data
data_a = data_huruf.count('a')
data_b = data_huruf.count('b')
print(f'Jumlah huruf a = {data_a}')
print(f'Jumlah huruf b = {data_b}\n')

# ambil posisi data (indeks)
data_nama = ['Jakaria', 'Kalama', 'Mawar', 'Saepuddin', 'Abdul', 'Baroja']
posisi_jakaria = data_nama.index('Jakaria')
posisi_mawar = data_nama.index('Mawar')
print(f'Indeks Jakaria pada indeks ke-{posisi_jakaria}')
print(f'Indeks Mawar pada indeks ke-{posisi_mawar}\n')

# mengurutkan list
data_angka = [1,2,1,3,4,2,4,7,1,9,14,11,10]
print(f'Jumlah angka 4 = {data_angka.count(4)}')
print(f'Posisi angka 2 = {data_angka.index(2)}\n')
print(f'Data Angka sebelum di sort = {data_angka}')
data_angka.sort()
print(f'Data angka sesudah di sort = {data_angka}')
print(f'Data nama sebelum di sort = {data_nama}')

# untuk string
data_nama.sort()
print(f'Data nama setelah di sort = {data_nama}')

# # untuk campuran  akan error
# data_campuran = ['a', 10, 'menarik', False, True, 'b']
# print(f'Data campuran = {data_campuran}')
# data_campuran.sort()
# print(f'Data campuran setelah di sort = {data_campuran}')

# membalikkan list
data_angka.reverse()
data_nama.reverse()
print(f'Data setelah di reverse = \n{data_angka}\n{data_nama}')
