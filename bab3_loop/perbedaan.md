Perbedaan Penggunaan For dan While

---

🔁 `while` vs `for` — Bedanya di Cara Mikir

🧠 1. `while` → Loop Selama Kondisi Benar

Mindset-nya:

> “Selama ini masih true, lanjut terus.”

Kita sendiri yang kontrol:

* kapan mulai
* kapan berhenti
* kapan nambah nilai
* kapan bisa infinite loop 💀

Contoh logika:

* Selama stok masih ada → kirim barang
* Selama password salah → minta input ulang
* Selama koneksi belum terhubung → coba lagi

⚠️ Risiko: kalau lupa update kondisi → loop nggak berhenti.
Ini tipe loop yang butuh disiplin.

---

🔄 2. `for` → Loop Berdasarkan Jumlah / Data

Mindset-nya:

> “Lakuin ini sebanyak X kali”
> atau
> “Lakuin ini untuk setiap item.”

Lebih clean, lebih aman, lebih predictable.

Contoh logika:

* Ulangi 10 kali
* Untuk setiap nama dalam daftar
* Untuk setiap angka dari 0 sampai 99

Di sini:

* Nggak perlu mikirin kondisi
* Nggak perlu nambah variabel manual
* Nggak gampang infinite

---

🎯 Perbandingan Simpel

| `while`                    | `for`                       |
| -------------------------- | --------------------------- |
| Berbasis kondisi           | Berbasis jumlah / koleksi   |
| Fleksibel banget           | Lebih terstruktur           |
| Bisa chaos kalau salah     | Lebih aman                  |
| Cocok untuk proses dinamis | Cocok untuk data yang jelas |

---

🚀 Kapan Pakai Mana?

🔥 Pakai `while` kalau:

* Nggak tahu berapa kali bakal looping
* Loop tergantung kondisi real-time
* Ada kemungkinan berhenti mendadak

🔥 Pakai `for` kalau:

* Sudah tahu jumlah iterasi
* Lagi ngolah list / data
* Mau kode lebih clean dan readable

---

🧩 Cara Gampang Ngerti

`for` itu kayak:

> “Gue lari 10 putaran. Fix.”

`while` itu kayak:

> “Gue lari sampai capek.”

Capeknya kapan? Tergantung kondisi 😌

---

Kalau jujur ya , di dunia nyata programmer, 80% kasus harian itu lebih sering pakai `for`.
`while` dipakai kalau logic-nya lebih “hidup” dan nggak bisa diprediksi jumlahnya.

Kalau kamu lagi bangun mindset jadi programmer tajam, jangan cuma hafal sintaks.
Tanya ke diri sendiri dulu:

> Ini problem berbasis jumlah?
> Atau berbasis kondisi?

Nah itu baru attacker mindset 🔥
