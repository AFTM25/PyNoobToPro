# Bilangan terbesar dari tiga bilangan

num1 = int(input('Masukkan bilangan pertama: '))
num2 = int(input('Masukkan bilangan kedua: '))
num3 = int(input('Masukkan bilangan ketiga: '))

# Untuk sementara, asumsikan saja angka pertama
# Adalah yang terbesar
larg_num = num1 

# kemudian, periksa apakah angka ke 2 lebih besar dari 
# larg_num pertama, jika iya lakukan update
if num2 > larg_num: larg_num = num2

# periksa lagi, apakah num3 lebih besar dari larg_num, jika iya lakukan update kembali pada num3
if num3 > larg_num: larg_num = num3 

print('Bilangan terbesar nya adalah : ', larg_num)
