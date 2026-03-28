# List awal yang mau kita urutkan
my_list = [8, 10, 6, 2, 4]

# Kita set True supaya while loop bisa jalan pertama kali
swapped = True  

# Selama masih ada pertukaran (swap), ulangi proses
while swapped:
    
    # Di awal setiap putaran, anggap belum ada pertukaran
    swapped = False  
    
    # Loop untuk membandingkan elemen satu per satu
    # len(my_list) - 1 supaya tidak out of range saat akses i+1
    for i in range(len(my_list) - 1):
        
        # Bandingkan elemen sekarang dengan elemen setelahnya
        if my_list[i] > my_list[i + 1]:
            
            # Kalau lebih besar, berarti salah urut → tukar posisi
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            
            # Tandai bahwa terjadi pertukaran
            swapped = True

# Setelah tidak ada pertukaran lagi, list sudah terurut
print(my_list)