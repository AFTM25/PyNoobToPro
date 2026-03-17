# for i in range(1,7):
#   if i == 5:
#     continue
#   print(f'Angka saat ini = {i}')

# print('Program selesai')

angka_max = -99999999
counter = 0 

angka_input = int(input('Masukkan angka atau -1: '))

while angka_input != -1:
  if angka_input == -1:
    continue 
  
  counter += 1 

  if angka_input > angka_max:
    angka_max = angka_input 
    angka_input = int(input('Masukkan angka atau -1: '))

if counter:
  print(f'Angka terbesar = {angka_max}')
else:
  print('Kamu belum memasukkan apa pun')