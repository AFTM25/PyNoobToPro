# Bagaimana cara kita mengelola / memanipulasi bit-bit tunggal (0 atau 1) di dalam sebuah bilangan integer menggunakan operator python 

# Sebuah integer bisa menyimpan banyak flag (setiap bit = satu kondisi yes/no)

# Untuk mengecek satu bit tertentu, kita tidak boleh membandingkan seluruh nilai variabel
# karena bit lain bisa memiliki nilai yang berubah-ubah

# Gunakan bit mask → angka yang memiliki 1 hanya pada posisi bit yang ingin dicek
# Contoh: bit ke-3 → mask = 2^3 = 8

# Gunakan operasi bitwise AND untuk mengisolasi bit tersebut
# hasil = flag_register & mask

# Jika hasil == 0 → bit bernilai 0 (tidak aktif)
# Jika hasil != 0 → bit bernilai 1 (aktif)

# Karena di Python selain 0 dianggap True, pengecekan bisa langsung di if