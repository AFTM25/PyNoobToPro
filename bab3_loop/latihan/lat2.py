'''
Teks itu menjelaskan tentang **Collatz Conjecture** (Hipotesis Collatz). Mari saya jelaskan dengan bahasa yang sederhana:

## Apa itu Hipotesis Collatz?

Pada tahun 1937, seorang matematikawan Jerman bernama Lothar Collatz membuat tebakan (hipotesis) yang menarik. Hipotesis ini sebenarnya belum terbukti kebenarannya sampai sekarang.

### Aturan Mainnya:

1. **Ambil angka berapa saja** (angka positif, bukan nol). Sebut angka ini `c0`.

2. **Kalau angkanya genap**: 
   - Bagi 2 angka tersebut (`c0 = c0 ÷ 2`)

3. **Kalau angkanya ganjil**: 
   - Kalikan 3, lalu tambah 1 (`c0 = 3 × c0 + 1`)

4. **Ulangi langkah 2-3** sampai akhirnya `c0` bernilai 1.

### Yang Menarik:
Hipotesis ini mengatakan bahwa **tidak peduli angka awal berapa pun**, kalau kita terus mengikuti aturan di atas, pasti akan sampai ke angka 1.

### Contoh Sederhana:

Misal kita mulai dengan `c0 = 6`:
- 6 (genap) → 6 ÷ 2 = 3
- 3 (ganjil) → 3 × 3 + 1 = 10
- 10 (genap) → 10 ÷ 2 = 5
- 5 (ganjil) → 5 × 3 + 1 = 16
- 16 (genap) → 16 ÷ 2 = 8
- 8 (genap) → 8 ÷ 2 = 4
- 4 (genap) → 4 ÷ 2 = 2
- 2 (genap) → 2 ÷ 2 = 1 (selesai)

### Tugas Program yang Diminta:

Buat program yang:
1. **Membaca satu angka** dari pengguna
2. **Menjalankan langkah-langkah** di atas selama `c0` belum sampai ke 1
3. **Menghitung berapa langkah** yang diperlukan
4. **Menampilkan semua nilai** `c0` di setiap langkah

### Contoh Output Program:

Misal input = 6
```
6
3
10
5
16
8
4
2
1
steps = 8
```

### Intinya:
Program ini akan menggunakan **while loop** untuk terus menjalankan aturan Collatz sampai angkanya menjadi 1, sambil mencatat setiap perubahan nilainya.

Paham maksudnya? Mau coba bikin programnya?

'''

c0 = int(input("Masukkan angka bukan negatif: "))
steps = 0

while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = c0 * 3 + 1
    steps += 1

print(c0)
print('steps = ', steps)
