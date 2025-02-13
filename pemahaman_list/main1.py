print('Ini adalah pemahaman pertama yakni pembuatan list')

# membuat list
list_angka = [1,7,8,3,88,90]

# menampilkan list
print(f'Data angka = {list_angka}')

# membuat list dengan list comprehension
list_nama = ['anggun', 'iwan', 'mahdara', 'keyla', 'zaka']
list_nama_upp = [nama.upper() for nama in list_nama]
print(f'Data nama = {list_nama_upp}')
