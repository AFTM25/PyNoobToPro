# Intro for loop

'''
Ada beberapa hal baru nih. Santai, kita kupas pelan-pelan:

* `for` itu buat mulai perulangan.
  Uniknya? Nggak ada kondisi kayak di `while`. Kita nggak perlu mikirin “selama ini benar atau salah”. Sistemnya udah ngecek sendiri di dalam. Auto pilot mode.

* Variabel setelah `for` itu jadi penghitung putaran loop.
  Dia yang nyatet: “oke ini putaran ke-0, ke-1, ke-2…” dan seterusnya. Kita nggak usah nambahin manual.

* Keyword `in` itu kayak jembatan.
  Dia bilang: “nih, variabel ini bakal ngambil nilai dari sini ya.”

* Keyword `range()` itu mesin penghasil angka.
  Misalnya dikasih angka 100, dia bakal ngeluarin angka dari 0 sampai 99.
  Ingat ya: dia mulai dari 0 dan berhenti **sebelum** angka yang kita masukin. Jadi kalau tulis 100, bukan sampai 100, tapi stop di 99. Classic jebakan batman.

* Nah, `pass` itu basically… kosong.
  Dia nggak ngapa-ngapain. Cuma placeholder biar struktur kodenya sah.
  Soalnya `for`, `if`, `elif`, `else`, dan `while` itu wajib punya isi. Kalau belum ada isi, ya pakai `pass` dulu.

---

Intinya?
`for` = mesin loop otomatis
`range()` = supplier angka
variabel = penghitung
`pass` = “yaudah sini dulu, belum ada isi”
'''

# Case 1 : 
# Mencetak Nilai saat ini
for i in range(10):
  # print(f'Nilai i saat ini adalah {i}')
  pass 

# Case 2 :
# range(start, stop)
# Artinya : dimulai dari angka hingga sebelum stop (-1)
for i in range(2, 8):
  # print(f'Nilai saat ini adalah {i}')
  pass 

# Case 2 
# range(start, stop, step)
# Artinya dimulai dari start
# Berhenti sebelum stop (-1)
# Langkahi looping dengan sebanyak step
for i in range(2, 8, 3):
  # print(f'Nilai saat ini adalah {i}')
  pass 


# Catatan juga : Apabila range(1,1) alias start dan stop nya satu
# Program tidak akan dijalankan
# Jadi, harus b < a
# Karena , range(start, stop) itu aslinya range(start, stop, +1)
# Kalau pun pengen jalan a > b atau sama dengan, maka
# range(start, stop, -step)
for i in range(9,0,-1):
  # print(i)
  pass

power = 1
for expo in range(16):
  # print(f'2 to the power of {expo} is {power} ')
  # power *= 2
  pass 

# Program perkalian 4 
# 1 x 4 = 4 
# 2 x 4 = 8
for i in range(10):
  # print(f'{i+1} x 4 = {(i+1) * 4}')
  pass 

# Perkalian 9
for x in range(10):
  print(f'{x+1} x 9 = {(x+1) * 9}')
