data = ['minyak goreng', 'sari roti', 'madu super 150gr', 'tejahe bandrek', 'gula pasir']

panjang = len(data)
for y in range(len(data)) :
    print(y + 1, data[y])

for reverses in range(panjang // 2):
    data[reverses], data[panjang - reverses - 1] = data[panjang - reverses - 1] , data[reverses]
    
print('\nReverses')
for item in range(len(data)):
    print(item + 1, data[item])
    
