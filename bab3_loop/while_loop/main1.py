# Simpan angka besar disini
larg_num = -999999999

# Masukkan nilai pertama
num = int(input('Enter a number or type -1 to stop: '))

# Jika number bukan -1, maka lakukan perulangan
while num != -1:
  # Cek apakah number lebih besar dari larg_num
  if num > larg_num:
    # jika true, update larg_num
    larg_num = num
  
  # masukkan lagi number
  num = int(input('Enter a number or type -1 to stop: '))

print('Largest number is: ', larg_num)

