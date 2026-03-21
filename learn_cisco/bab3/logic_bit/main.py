'''
================================

LOGIKA KOMPUTER(ComputerLogic)

================================

1. Dalam kehidupan nyata, kondisi biasanya tidak berdiri sendiri.
   Sering kali suatu keputusan bergantung pada lebih dari satu syarat.

2. Jika dua kondisi harus terpenuhi bersamaan, maka dalam logika disebut "conjunction" (dan / AND).
  
  Contoh:
  Jika punya waktu luang DAN cuaca bagus → pergi jalan.

  Artinya: kedua kondisi harus True agar hasilnya True.

  3. Jika keputusan bergantung pada minimal salah satu kondisi,

  maka disebut "disjunction" (atau / OR).

  Contoh:

  Jika kamu di mall ATAU saya di mall → beli hadiah.

  Artinya: cukup salah satu kondisi True agar hasilnya True.

  4. Python menyediakan logical operators untuk menangani

  hubungan antar kondisi:

  - and  → conjunction

  - or   → disjunction

  - not  → membalik nilai boolean

  5. Tanpa logical operators, Python tidak bisa membuat

  kondisi yang kompleks seperti di dunia nyata.

  Intinya:

  Logical operators membantu kita menggabungkan beberapa

  kondisi agar program bisa mengambil keputusan dengan benar.

================================
'''

# Logical Expression
var = 1
print(var > 0)
print(not(var <= 0))

print(var != 0)
print(not(var == 0))

# De Morgan's laws
# Perhatikan dalam penggunaan dengan tanda kurung atau tanpa tanda kurung
p = True 
q = False
print(not (p and q) == (not p) or (not q) )
print(not (p or q) == (not p) and (not q))

'''
gws, ada empat operator yang bisa lo pake buat ngoprek bit-bit data satu per satu. Nama mereka tuh bitwise operators.

Mereka tuh ngelakuin semua operasi yang udah kita bahas sebelumnya di konteks logika, plus satu operator tambahan. Yang ini namanya xor (kependekan dari exclusive or), dan dilambangin pake ^ (caret).

Ini dia semuanya:

& (ampersand) -> bitwise conjunction;
| (bar) -> bitwise disjunction;
~ (tilde) -> bitwise negation;
^ (caret) -> bitwise exclusive or (xor).

Note : Nilai dari operator ini adalah harus berupa bilangan bulat.
'''
i = 15
j = 22 
cek_logic = i and j 
cek_bit = i & j
print(f'{i:08b}')
print(f'{j:08b}')
print(f'-----------&')
print(f'{cek_bit:08b}\n')

cek_notLogic = not i 
print(cek_notLogic)

cek_negasiBit = ~i 
print(f'{cek_negasiBit:08b} = {cek_negasiBit}')