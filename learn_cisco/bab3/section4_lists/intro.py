# Indexing list
angka = [12, 11, 109, .67]
print(angka)

angka[2] = 109 + 78
print(angka)

angka[3] = angka[2]
print(angka)

# removing list
del angka[1]
print(angka)

# removing dengan variabel nya
del angka

# coba-coba aja dengan mencari nilai average dari list
angka = [x * 2 for x in range(1,10)]
angka_kecil = min(angka)
print(sum(angka) // len(angka))

# Soal 
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
angka_baru = int(input('Masukkan angka yang baru: '))
hat_list[2] = angka_baru

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)
print()


angka = [4, 7, 2, 9]
total = 0
for i in range(len(angka)):
    if angka[i] % 2 == 1:
        angka[i] = 0
    
    total += angka[i]
    
print(total)