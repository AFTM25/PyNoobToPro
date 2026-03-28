# list berupa data angka kosong
daftar_angka = []

# pertanyaan mau berapa kali nilai dimasukkan
input_max_nilai = int(input('Masukkan maximal nilai yang ingin dimasukkan: '))

# lakukan perulangan dan tambahan input dari pengguna lalu tambahkan ke list daftar_angka
for nilai in range(input_max_nilai):
  input_nilai = int(input(f'Masukkan nilai {nilai + 1}: '))
  daftar_angka.append(input_nilai)

print(daftar_angka)

daftar_angka.sort()
print('Daftar angka setelah diurutkan: ', daftar_angka)

daftar_angka.sort(reverse=True)
print('Daftar angka setelah diurutkan secara terbalik: ', daftar_angka)





'''
# PERBEDAAN .sort(reverse=True) vs .reverse()

# .sort(reverse=True)
# - Melakukan proses pengurutan (sorting).
# - Data akan diurutkan berdasarkan nilai (dari terbesar ke terkecil).
# - Menggunakan algoritma sorting internal Python (Timsort).
# - Cocok digunakan ketika ingin mendapatkan urutan descending yang benar.
# - Kompleksitas waktu sekitar O(n log n).
# - Mengubah isi list secara langsung (in-place).

# .reverse()
# - Tidak melakukan pengurutan.
# - Hanya membalik urutan elemen sesuai posisi saat ini.
# - Tidak peduli apakah data sudah terurut atau belum.
# - Cocok digunakan ketika hanya ingin membalik urutan yang sudah ada.
# - Kompleksitas waktu sekitar O(n).
# - Juga mengubah isi list secara langsung (in-place).

# Kesimpulan inti:
# .sort(reverse=True) = mengurutkan dari besar ke kecil.
# .reverse() = membalik posisi elemen tanpa mengurutkan.


'''