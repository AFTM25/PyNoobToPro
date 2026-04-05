# Negative Slicing 
# Indeks negatif --> Menghitung elemen dari arah belakang(ujung list).
# berguna untuk mengambil item / nilai dari akhir list tanpa harus mengetahui panjang list.

daftar_nama = ['Alice', 'Zaka', 'Pratama', 'Andi', 'Mawar']
print(daftar_nama[1:-1]) # Artinya mulai dari indeks pertama ('Alice') sampai sebelum indeks terakhir ('Mawar')

# Ada logika error : 
# Jika start > end maka py akan mengembalikan list kosong. 
# Karena py berjalan maju (dari kiri ke kanan)
# Kalau pun mau dipaksa start < end maka ada step nya

copy_list = daftar_nama[:]
copy_list.append('Maman')
# Seperti di bawah ini  
print(copy_list[-1:1:-2])

print('-'*40)

# Ada juga cara singkat (menghilangkan indeks / omitting)
# Tanpa start [:end]
print(copy_list[:2]) # Mengambil elemen dari awal sampai sebelum indeks ke-2 (tidak termasuk indeks ke-2)
# Tanpa end [start:]
print(copy_list[2:]) # Mengambil elemen dari indeks ke-2 sampai akhir list
# Tanpa start dan end [:] 
print(copy_list[:]) # Mengambil semua elemen dari list (membuat salinan list)

print('-'*40)

'''
Perintah del my_list[index] slice
# Menghapus potongan elemen dengan del dan slicing di list.

# Contoh: del my_list[1:3] menghapus elemen indeks 1 dan 2.

# Setelah dihapus, list langsung rapat tanpa elemen di tengah.

# del my_list[:] mengosongkan list tapi variabelnya tetap ada.

# del my_list menghapus list secara total dari memori.

'''
del daftar_nama[:] # Menghapus keseluruhan isi dalam list 
print(daftar_nama)

daftar_nama.extend(['Zaka', 'Mawar', 'Revaldi', 'Sulis'])


del daftar_nama[:2]
print(daftar_nama)