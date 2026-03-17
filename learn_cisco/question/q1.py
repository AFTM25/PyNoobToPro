def q1():
  '''Pertanyaan 1: Buatlah perulangan for yang menghitung dari 0 hingga 10, dan mencetak angka ganjil ke layar. Gunakan kerangka di bawah ini.'''
  for i in range(0, 11):
    if i % 2 == 1:
      print(i)

def q2():
  '''
  Pertanyaan 2: Buatlah perulangan while yang menghitung dari 0 hingga 10, dan mencetak angka ganjil ke layar. Gunakan kerangka di bawah ini.
  '''
  x = 1
  while x < 11:
    if x % 2 != 0:
      print(x)
    x += 1

def q3():
  '''
  Pertanyaan 3: Buat program dengan perulangan for dan pernyataan break. Program tersebut harus mengulang karakter dalam alamat email, keluar dari perulangan ketika mencapai simbol @, dan mencetak bagian sebelum @ dalam satu baris. Gunakan kerangka di bawah ini.
  '''
  for ch in 'john.smith@pythoninstitute.org':
    if ch == '@':
      break 
    print(ch, end="")

def q4():
  '''
  Pertanyaan 4: Buatlah program dengan perulangan for dan pernyataan continue. Program tersebut harus mengulang string angka, mengganti setiap angka 0 dengan x, dan mencetak string yang telah dimodifikasi ke layar. Gunakan kerangka di bawah ini.
  '''
  for digit in '0165031806510':
    if digit == '0':
      print('x', end='')
      continue
    print(digit, end='')

def q5():
  '''
  Question 5: What is the output of the following code?
  '''
  n = 3
  while n > 0:
    print(n + 1)
    n -= 1
  else:
    print(n)

q5()