print('\nLatihan Sederhana')
data = []
max_input = int(input('Mau berapa kali data di masukkan? : '))
for input2 in range(max_input):
    input_data = input(f'Masukkan data ke {input2+1}: ')
    data.append(input_data)

print('Data ditampilkan sebagai berikut: ')
for no, item in enumerate(data):
    print(f'{no+1}. {item.title()}')

print('\nCari data: ') 
cari_data = input('Masukkan pencarian: ')
ditemukan = False # flag
for hasil in range(len(data)):
    ditemukan = data[hasil] == cari_data
    if ditemukan:
        break

if ditemukan:
    print(f'{cari_data} ditemukan pada index ke {hasil}')
else:
    print(f'{cari_data} tidak ditemukan')
    
print('\n\n\n')

