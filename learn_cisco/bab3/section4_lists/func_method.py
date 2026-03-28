# --- PERBEDAAN FUNCTION vs METHOD ---

# 1. FUNCTION (Fungsi): Mandiri, tidak punya "tuan".
# Cara panggil: nama_fungsi(data)
# Contoh: len(my_list) -> Menghitung panjang list.
# Analogi: Seperti alat perkakas yang bisa dipakai ke benda apa saja.

# 2. METHOD (Metode): Terikat, dimiliki oleh tipe data tertentu.
# Cara panggil: data.nama_method(argumen)
# Contoh: my_list.append("data") -> Menambah data ke dalam list.
# Analogi: Seperti fitur bawaan pada sebuah benda (misal: tombol 'on' pada laptop).

# POIN PENTING:
# Method menggunakan tanda TITIK (.) dan bisa mengubah isi/kondisi 
# internal dari data tersebut secara langsung.

# Method yang digunakan oleh list 
# 1. .append() dan .insert()
# Kegunaan .append() untuk menambah item di akhir list
# Kegunaan .insert(location, itemNew) untuk menambah item di list dengan lokasi tertentu. Lokasi ini berupa index

# Contoh 
numbers = [111, 7, 2, 1]
print(numbers)
print(len(numbers))

### 
numbers.append(4)

print(numbers)
print(len(numbers))

numbers.insert(1, 333)
print(numbers)
print(len(numbers))
print()

### 

myList = [] # Membuat list kosong
for i in range(5):
  myList.append(i + 1)
print(myList)

del myList

myList = []
for i in range(5):
  myList.insert(0, i + 1) # akan menghasilkan urutan terbalik
print(myList)
keterangan_reverse = '''
Kenapa hasilnya jadi terbalik? Karena angka baru diletakkan bukan di paling belakang, melainkan dipaksa diposisikan di paling depan(index 0).
LOGIKA ALGORITMA INSERT(0, ...)

1. POSISI TETAP: Setiap iterasi, target indeks SELALU 0 (paling depan).
2. PERGESERAN: Setiap angka baru masuk ke indeks 0, angka-angka yang sudah ada sebelumnya "terdorong" satu langkah ke kanan (indeks n + 1).
3. URUTAN: Karena angka yang muncul terakhir di loop (angka 5) dipaksa masuk ke posisi paling depan, maka hasil akhirnya menjadi terbalik.

# Visualisasi Sederhana:
# Iterasi 1: [1]
# Iterasi 2: [2, 1]          <- 2 masuk ke depan, 1 geser ke kanan
# Iterasi 3: [3, 2, 1]       <- 3 masuk ke depan, 2 & 1 geser
# Iterasi 4: [4, 3, 2, 1]    <- 4 masuk ke depan, dst.
# Iterasi 5: [5, 4, 3, 2, 1] <- Hasil Akhir
'''