'''
Membuat program perhitungan dari gambar 

Sample input    |  Sample Ouput
1               | 0.6000000000000001
10              | 0.09901951266867294
100             | 0.009999000199950014
-5              | -0.19258202567760344

'''

num_x = float(input('Enter value for x : '))
result = 1. / (num_x + 1. / (num_x + 1. / (num_x + 1.)))
print(f'Result : {result}')
