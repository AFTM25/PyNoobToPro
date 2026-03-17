# Program else branch pada looping

# while 

counter = 5 
# while counter > 3:
#     print(counter)
#     counter -= 1
# else:
#     print('else ', counter)

while counter >= 3:
    print(counter)
    counter -= 1
else:
    print('else: ', counter)
"""
else pada while loop:
- Bukan dijalankan setiap loop, tapi SATU KALI di AKHIR
- Dieksekusi SETELAH kondisi while bernilai False
- Nilai variabel yang ditampilkan adalah nilai TERAKHIR setelah loop selesai
- Cocok untuk mengeksekusi kode "setelah selesai melakukan perulangan"
"""
# Inti dari while else di atas : "Ketika hasilnya false, baru si else itu nampilinnya" ✅
