kata = input('Enter of word: ')
upper_kata = kata.upper()
sample = ''
kumpulan_karakter = ['A', 'I', 'U', 'E', 'O']

for letter in upper_kata:
    if letter in kumpulan_karakter:
        continue
    else:
        sample += letter
        
print(sample)
        