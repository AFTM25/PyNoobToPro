print(10*'='+' Nested List ' + '='*10)
# Nested List / List Bersarang
nama1 = ['Andi', 22, 'Laki-laki']
nama2 = ['Asep', 21, 'Laki-laki']
nama3 = ['Salsabila', 22, 'Perempuan']

list_nama = [nama1, nama2, nama3]

for nama in list_nama:
    print(f'Nama\t: {nama[0]}')
    print(f'Usia\t: {nama[1]}')
    print(f'Gender\t: {nama[2]}\n')
