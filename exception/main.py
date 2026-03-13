hll_ = input('Masukkan teks : ')
if not hll_.isalpha():
  raise Exception('Hanya berupa teks, tidak bisa angka, dan karakter lainnya')
print('Teks yang dimasukkan : ' + hll_)