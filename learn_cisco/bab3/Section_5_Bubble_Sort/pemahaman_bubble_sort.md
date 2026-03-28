# Bubble Sort - Pemahaman Dasar

## Apa itu Bubble Sort?

Bubble Sort adalah algoritma pengurutan sederhana yang bekerja dengan
cara membandingkan dua elemen yang bersebelahan, lalu menukarnya jika
urutannya salah.

Disebut *bubble* karena nilai terbesar akan "menggelembung" ke posisi
paling akhir setelah satu putaran penuh.

------------------------------------------------------------------------

## Cara Kerja (Step by Step)

Misal data:

    [8, 10, 6, 2, 4]

### Putaran 1:

-   8 dan 10 → tidak ditukar
-   10 dan 6 → ditukar → `[8, 6, 10, 2, 4]`
-   10 dan 2 → ditukar → `[8, 6, 2, 10, 4]`
-   10 dan 4 → ditukar → `[8, 6, 2, 4, 10]`

Setelah putaran pertama, angka terbesar (10) sudah berada di posisi
terakhir.

------------------------------------------------------------------------

### Proses Berulang

Algoritma akan terus mengulang proses tersebut sampai tidak ada lagi
pertukaran.

Biasanya digunakan variabel boolean seperti:

    swapped = True

Jika dalam satu putaran tidak ada pertukaran, berarti data sudah terurut
dan proses berhenti.

------------------------------------------------------------------------

## Kompleksitas

-   Worst Case: O(n²)
-   Average Case: O(n²)
-   Best Case (jika sudah hampir urut): O(n)

Karena menggunakan nested loop, algoritma ini kurang efisien untuk data
berukuran besar.

------------------------------------------------------------------------

## Perbandingan dengan Python Built-in

Python memiliki method bawaan:

    my_list.sort()

Method ini menggunakan algoritma yang jauh lebih efisien (Timsort)
dengan kompleksitas rata-rata O(n log n).

Bubble Sort biasanya digunakan untuk pembelajaran logika dan algoritma,
bukan untuk produksi.

------------------------------------------------------------------------

## Inti Pembelajaran

Dengan memahami Bubble Sort, kita belajar:

-   Cara kerja loop bersarang
-   Logika perbandingan nilai
-   Teknik pertukaran (swap)
-   Penggunaan flag untuk kontrol kondisi berhenti
-   Dasar pemikiran efisiensi algoritma

------------------------------------------------------------------------

## Kesimpulan

Bubble Sort adalah fondasi untuk memahami algoritma pengurutan dan cara
berpikir sistematis dalam pemrograman. Meskipun jarang digunakan dalam
proyek nyata, konsepnya penting untuk membangun kemampuan problem
solving.
