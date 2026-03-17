'''
Ceritanya begini: Ada seorang anak laki-laki dan ayahnya yang bekerja sebagai programmer komputer. Mereka sedang bermain dengan balok-balok kayu. Mereka akan membuat piramida.

Piramida mereka agak unik, karena sebenarnya ini adalah dinding berbentuk piramida - jadi bentuknya pipih/datar. Piramidanya disusun dengan satu aturan sederhana: setiap lapisan yang lebih bawah berisi satu balok lebih banyak daripada lapisan di atasnya.

**Contoh susunannya:**
- Lapisan paling atas (lapisan 1): 1 balok
- Lapisan ke-2: 2 balok
- Lapisan ke-3: 3 balok
- Lapisan ke-4: 4 balok
- Dan seterusnya...

Jadi bentuknya seperti ini kalau dilihat dari samping:
```
□              ← lapis 1 (1 balok)
□□             ← lapis 2 (2 balok)
□□□            ← lapis 3 (3 balok)
□□□□           ← lapis 4 (4 balok)
```

**Tugas kamu:**
Buatlah program yang membaca jumlah balok yang tersedia, lalu menghitung berapa tinggi piramida yang bisa dibuat dari balok-balok tersebut.

**Yang dimaksud dengan "tinggi"** adalah jumlah lapisan yang berhasil diselesaikan dengan sempurna. Artinya, jika baloknya tidak cukup untuk membuat lapisan berikutnya, maka mereka berhenti dan tidak melanjutkan.

**Contoh:**
- Kalau punya 6 balok:
  - Lapis 1: butuh 1 balok (sisa 5)
  - Lapis 2: butuh 2 balok (sisa 3) 
  - Lapis 3: butuh 3 balok (sisa 0)
  - Lapis 4: butuh 4 balok (tidak cukup)
  - Jadi tingginya = 3 lapis

- Kalau punya 10 balok:
  - Lapis 1: 1 (sisa 9)
  - Lapis 2: 2 (sisa 7)
  - Lapis 3: 3 (sisa 4)
  - Lapis 4: 4 (sisa 0)
  - Lapis 5: 5 (tidak cukup)
  - Jadi tingginya = 4 lapis

Programnya harus bisa menghitung berapa lapisan lengkap yang bisa dibuat dari jumlah balok yang tersedia.
'''

blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
total_balok_yang_dipakai = 0
lapis = 1
while total_balok_yang_dipakai + lapis <= blocks:
    total_balok_yang_dipakai += lapis
    height += 1
    lapis += 1


print("The height of the pyramid:", height)

