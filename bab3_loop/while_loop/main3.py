import os
os_name = os.name 
match os_name:
  case 'posix' : os.system('clear')
  case 'nt' : os.system('cls')

secret_number = 777

print(
  '''
  \t\t+=================================+
  \t\t| Welcome to my Game, muggle!     |
  \t\t| Enter an integer number         |
  \t\t| and guess what number I've      |
  \t\t| picked for you.                 |
  \t\t| So, what is the secret number?  |
  \t\t+=================================+
  '''
)

user_guess = int(input('Masukkan angka: '))
while user_guess != secret_number:
  print('Ha ha! You are stuck in my loop!')
  user_guess = int(input('Masukkan angka lagi: '))

print(user_guess)
print('Well done, muggle! You are free now.')