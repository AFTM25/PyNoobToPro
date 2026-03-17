# Perulangan while dan for juga dapat memiliki klausa else di Python. Klausa else dieksekusi setelah perulangan selesai dijalankan selama belum diakhiri oleh break, misalnya

print('Program while else')
n = 0
# Ketika n tidak sama dengan 3
while n != 3:
    print(n)
    n += 1
# Ketika perulangan sudah dijalankan semua
else:
    print(n, 'else')

print('End\n')

print('Prgram for else')
for i in range(1, 10):
    if i % 2 == 1:
        i = i + 4 / 3
    else:
        i //= 2
else:
    print('Akhir program for loop : ', i)
    

