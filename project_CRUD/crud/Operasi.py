import time
import os
from . import Database
from .Utility import random_string
from builtins import int

def delete(no_buku):
    try:
        with open(Database.DB_NAME, 'r') as file:
            lines = file.readlines()
            
        with open('project_CRUD/crud/data_temp.txt', 'w', encoding='utf-8') as temp_file:
            for index, line in enumerate(lines):
                if index != no_buku - 1:
                    temp_file.write(line)
                    
        os.remove(Database.DB_NAME)
        os.rename('project_CRUD/crud/data_temp.txt', Database.DB_NAME)
        print('Data berhasil dihapus')
        
    except Exception as e:
        print(f'Error message : {e}')
                
                    
                    

def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = pk
    data['date_add'] = data_add
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    data_length = len(data_str)
    try:
        with open(Database.DB_NAME, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            index = no_buku - 1
            
            if index >= 0 and index < len(lines):
                lines[index] = data_str
                
                file.seek(0)
                file.writelines(lines)
                file.truncate()
                print('Data berhasil di update')
            else:
                print('Nomor buku tidak valid')
    except:
        print('Error dalam update data')

def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime()) 
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as fl:
            fl.write(data_str)
    except:
        print('Data gagal ditambahkan')

def create_first_data():
    penulis = input('Penulis: ')
    judul = input('Judul: ')
    while True:
        try:
            tahun = int(input('Tahun\t : '))
            if len(str(tahun)) == 4:
                break
            else:
                print('Tahun tidak boleh kurang atau lebih dari 4 angka')
        except:
            print('Tahun hanya boleh angka, silahkan masukkan tahun lagi (yyyy)')
    
    # data frame
    data = Database.TEMPLATE.copy()
    
    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime()) 
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
            
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as fl:
            fl.write(data_str)
    except:
        print('Udahlah gagal')
        
def baca(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if 'index' in kwargs:
                index_buku = kwargs['index'] - 1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else :
                    return content[index_buku]
            else:
                return content
    except:
        print('Membaca database error')
        return False