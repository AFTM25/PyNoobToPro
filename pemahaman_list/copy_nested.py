data_nama_laki2 = ['iriawan', 'iwan', 'samsul', 'jaki','aditya']
data_nama_perempuan = ['mawar', 'bunga', 'fira', 'andini', 'ravena']

nama_laki2 = [laki2.capitalize() for laki2 in data_nama_laki2]
nama_perempuan = [perempuan.capitalize() for perempuan in data_nama_perempuan]

print(f'Data nama kelamin laki-laki = {nama_laki2}')
print(f'Data nama kelamin perempuan = {nama_perempuan}')

data_nama = [nama_laki2, nama_perempuan]
print(f'Data Nama :\n{data_nama}\n')

from copy import deepcopy
data_deepCopy = deepcopy(data_nama)
print(f'Data deepcopy =\n{data_deepCopy}\n')

data_deepCopy[0][2] = 'Bahroni'
print(f'Data Nama :\n{data_nama}\n')
print(f'Data deepcopy :\n{data_deepCopy}\n')
