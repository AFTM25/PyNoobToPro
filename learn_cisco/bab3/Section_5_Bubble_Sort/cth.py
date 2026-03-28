# List berupa data angka kosong
data_angka = []
tukar_menukar = True

# Pertanyaan mau berapa data yang dimasukkan
jumlah_nilai = int(input('Mau berapa kali nilai dimasukkan?: '))

for nilai in range(jumlah_nilai):
  # Input nilai yang dimasukkan oleh user
  nilai_input = float(input('Masukkan nilai: '))
  data_angka.append(nilai_input)

while tukar_menukar:
  tukar_menukar = False
  for nilai_angka in range(len(data_angka) - 1):
    if data_angka[nilai_angka] > data_angka[nilai_angka + 1]:
      tukar_menukar = True
      data_angka[nilai_angka], data_angka[nilai_angka + 1] = data_angka[nilai_angka + 1], data_angka[nilai_angka]

print(data_angka)