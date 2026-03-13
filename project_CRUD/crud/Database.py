from builtins import int
from . import Operasi
DB_NAME = 'project_CRUD/crud/data.txt'
TEMPLATE = {
    'pk':'XXXXXX',
    'date_add':'yyyy-mm-dd',
    'judul':255*"",
    'penulis':255*"",
    'tahun':'yyyy'
}

def init_console():
    try:
        with open(DB_NAME,'r') as fl:
            print('Database tersedia')
    except:
        print('Database tidak dapat ditemukan, silahkan buat baru')
        Operasi.create_first_data()