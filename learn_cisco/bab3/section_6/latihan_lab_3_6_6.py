'''
Deskripsi tersebut adalah sebuah tantangan pemrograman (biasanya dari modul latihan Python seperti Cisco Networking Academy) untuk melakukan **Data Deduplication** atau menghapus angka yang duplikat dalam sebuah *list*.

Secara logis, maksud dari tugas tersebut bisa kita bedah menjadi beberapa poin poin kritis:

### 1. Masalah Utama (Problem)
Kamu memiliki sebuah *list* berisi angka bulat (integer). Di dalam *list* tersebut, ada angka-angka yang muncul lebih dari satu kali (duplikat). Tugasmu adalah memastikan setiap angka hanya muncul **satu kali saja**.

### 2. Batasan & Aturan (Constraints)
* **Hard-coded:** List awalnya sudah tertulis di dalam kode (tidak perlu input manual dari keyboard, kecuali kamu ingin menambahkannya sebagai fitur tambahan).
* **Temporary Work Area:** Disarankan untuk membuat **list baru** sebagai tempat menampung hasil pembersihan, bukan langsung mengubah list aslinya (*in-situ*). Ini jauh lebih aman dalam pengolahan data untuk menjaga integritas data sumber.

---

### 3. Logika Algoritmanya (Step-by-Step)
Jika kita hubungkan dengan kode *Linear Search* yang kamu tulis sebelumnya, alurnya akan seperti ini:

1.  Siapkan `list_sumber` (yang ada duplikatnya).
2.  Siapkan `list_bersih` (kosong, untuk menampung angka unik).
3.  Lakukan perulangan (`for`) untuk setiap angka di dalam `list_sumber`.
4.  **Logika Kritis:** Di setiap putaran, periksa dulu: *"Apakah angka ini sudah ada di dalam `list_bersih`?"*
    * Jika **Belum ada** (Gunakan operator `not in`), masukkan angka tersebut ke `list_bersih`.
    * Jika **Sudah ada**, abaikan (jangan masukkan) dan lanjut ke angka berikutnya.
5.  Setelah selesai, `list_bersih` akan berisi angka-angka unik tanpa duplikat.



---
'''

my_list = [8, 9, 9, 10, 8, 7, 4, 3, 1, 8, 2]
list_clear_duplikat = []
for nilai in my_list:
    if nilai not in list_clear_duplikat:
        list_clear_duplikat.append(nilai)
print(my_list)
list_clear_duplikat.sort()
print(list_clear_duplikat)