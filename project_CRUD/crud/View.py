from . import Operasi
from builtins import int

def delete_console():
    read_console()
    while True:
        print('Silahkan pilih nomor buku yang mau di delete')
        no_buku = int(input('No Buku : '))
        data_buku = Operasi.baca(index=no_buku)
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
        
            # Data yang ingin di delete
            print('\n'+'='*100)
            print('Data yang mau dihapus')
            print(f'1. Penulis\t: {penulis:.40}')
            print(f'2. Judul\t: {judul:.40}')
            print(f'3. Tahun\t: {tahun:4}')
            
            data_backup = (pk, data_add, penulis, judul, tahun)
            
            is_done = input('Apakah yakin ingin dihapus? y/n/undo : ')
            if is_done.lower() == 'y':
                Operasi.delete(no_buku)
                break
            elif is_done.lower() == 'undo':
                pk, data_add, penulis, judul, tahun = data_backup
                print('Perubahan dibatalkan, data dikembalikan ke semula')
            else:
                print('Pilihan tidak tersedia, Silahkan pilih y/n/undo : ')
        else:
            print('Nomor buku tidak valid, harap masukkan ulang')
            
            
        
        
        
            
def update_console():
    read_console()
    while True:
        print('Silahkan pilih nomor buku yang mau di update')
        no_buku = int(input('No Buku : '))
        data_buku = Operasi.baca(index=no_buku)
        if data_buku:
            break
        else:
            print('Nomor buku tidak valid, harap masukkan ulang')
    
    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    # Backup data lama buat fitur undo
    data_backup = (pk, data_add, penulis, judul, tahun)
    
    while True:
        # Data yang ingin diupdate
        print('\n'+'='*100)
        print('Silahkan pilih data yang mau diubah')
        print(f'1. Penulis\t: {penulis:.40}')
        print(f'2. Judul\t: {judul:.40}')
        print(f'3. Tahun\t: {tahun:4}')
        
        # Memilih mode yang akan diupdate
        usr_opt = input('Pilih data [1,2,3] : ')
        print('\n'+'='*100)
        match usr_opt:
            case '1': penulis = input('Penulis\t: ')
            case '2': judul = input('Judul\t: ')
            case '3':
                while True:
                    try:
                        tahun = int(input('Tahun\t : '))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print('Tahun tidak boleh kurang atau lebih dari 4 angka')
                    except:
                        print('Tahun hanya boleh angka, silahkan masukkan tahun lagi (yyyy)')
            case _: print('Nomor data tidak ditemukan')
            
        is_done = input('Apakah data sudah sesuai? y/n/undo : ')
        if is_done.lower() == 'y':
            break
        elif is_done.lower() == 'undo':
            pk, data_add, penulis, judul, tahun = data_backup
            print('Perubahan dibatalkan, data dikembalikan ke semula')
            
        
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)
    


def create_console():
    print('\n\n'+'='*100)
    print('Silahkan Tambah Data Buku')
    penulis = input('Penulis\t : ')
    judul = input('Judul\t : ')
    while True:
        try:
            tahun = int(input('Tahun\t : '))
            if len(str(tahun)) == 4:
                break
            else:
                print('Tahun tidak boleh kurang atau lebih dari 4 angka')
        except:
            print('Tahun hanya boleh angka, silahkan masukkan tahun lagi (yyyy)')
    
    Operasi.create(tahun, judul, penulis)
    print('Berikut adalah data anda')
    read_console()
    
def read_console():
    data_file = Operasi.baca()
    
    index = 'No'
    penulis = 'Penulis'
    judul = 'Judul'
    tahun = 'Tahun'
    
    # Header
    print('\n'+'='*100)
    print(f'{index:^5} | {penulis:^40} | {judul:^40} | {tahun:5}')
    print('-'*100)
    
    # Data
    for index, data in enumerate(data_file):
        if data.strip() == '':
            continue

        data_break = data.split(',')
        
        if len(data_break) >= 5:  # Validasi jika data lengkap
            pk = data_break[0]
            date_add = data_break[1] 
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4]
            
            print(f"{index+1:^5} | {penulis:^40} | {judul:^40} | {tahun:5}",end="")
        else:
            print(f"Data rusak atau tidak lengkap: {data_break}")

    
    
    # Footer
    print('='*100+'\n')
    