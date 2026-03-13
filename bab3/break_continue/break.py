# for i in range(16):
#   if i == 3:
#     break 
#   print(f'Angka saat ini {i}')

# print('Program selesai')

# Meneruskan program yang menentukan angka terbesar dari inputan
angka_terbesar = -99999999999
counter = 0

while True:
  try:
    angka_input = int(input('Masukkan angka atau -1 untuk berhenti: '))

    # Cek apakah inputan sama dengan -1
    if angka_input == -1:
      break 

    # tambahkan counter sebagai perhitungan berapa kali user masukkan angka
    counter += 1

    # Cek kondisi lagi apakah inputan lebih besar dari angka_terbesar
    if angka_input > angka_terbesar:
      angka_terbesar = angka_input 

  except ValueError:
    print('Harap masukkan angka, bukan karakter kosong')

# Kondisi untuk mengecek apakah user memasukkan angka selain -1 
# Jika iya maka tampilkan hasil nya angka terbesar 
# Jika tidak berhenti, tapi -1 tidak masuk sebagai hitungan 
if counter != 0:
  print(f'Angka terbesar = {angka_terbesar}')
else:
  print('Kamu belum memasukkan angka apa pun')

  