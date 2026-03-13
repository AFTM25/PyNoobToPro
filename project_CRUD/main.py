from builtins import int
import os
import crud as CRUD
if __name__ == '__main__':
    os_opr = os.name
    
    # check database ada atau tidak
    CRUD.init_console()
    
    match os_opr:
            case 'posix':os.system('clear')
            case 'nt' : os.system('cls')
    
    
    while True:
            
        print('Program Database Perpustakaan')
        print('=============================')
        print('1. Read Data')
        print('2. Create Data')
        print('3. Update Data')
        print('4. Delete Data')
        
        
        usr_opt = input('Masukkan opsi: ')
        
        match usr_opt:
            case '1': CRUD.read_console()
            case '2': CRUD.create_console()
            case '3': CRUD.update_console()
            case '4': CRUD.delete_console()
            case _: print('Sorry, opsi hingga 4')
        
        is_done = input('Apakah Selesai? y/n : ')
        if is_done == 'y' or is_done == 'Y':
            break

    print('Akhir dari program, Terimakasih')
        
        
