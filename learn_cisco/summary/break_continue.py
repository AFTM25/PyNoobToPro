# Break and Continue untuk merubah flow perulangan
# apakah berhenti atau lanjut 
print('Program dengan break')
print('Start')
for i in range(1, 10):
    print(i)
    if i == 4:
        print('sudah berhenti di ', i)
        break

print()

text = 'OpenEDG Python Institute'
for letter in text:
    if letter == 't':
        break
    print(letter, end='*')

print()
print('End\n')

print('Program dengan Continue')
print('Start')
text = 'Kenapa ada begini sih?'
for huruf in text:
    if huruf == 'd':
        continue
    print(huruf, end=" * ")
    
