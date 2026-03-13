try:
  with open('exception/log1.log') as f:
    print(f.read())
except FileNotFoundError:
    print('File tidak ditemukan')