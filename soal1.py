# Soal 1
# Membuat Class Mahasiswa
# Output : Halo nama saya {nama}, nim saya {nim}, dan saya berasal dari jurusan {jurusan}

import tkinter as tk 
from tkinter.messagebox import showinfo 
from tkinter import ttk 

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.__nama = nama 
        self.__nim = nim
        self.__jurusan = jurusan 
        
    @property 
    def nama(self):
        return self.__nama 
    
    @property 
    def nim(self):
        return self.__nim 
    
    @property 
    def jurusan(self):
        return self.__jurusan 
    
    def info_mahasiswa(self):
        showinfo("Data Mahasiswa", 
                 f"Halo nama saya {self.__nama}, saya berasal dari jurusan {self.__jurusan}")
        
# Validasi inputan
def submit_on():
    nama = entry_nama.get().strip()
    nim = entry_nim.get().strip()
    jurusan = entry_jurusan.get().strip()
    
    if not nama or not nim or not jurusan:
        showinfo('Error', 'Nama, NIM dan jurusan tidak boleh kosong!')
        return 
    
    if not nim.isdigit():
        showinfo('Error', 'NIM harus berupa angka!')
        return 
    
    if len(nim) > 6:
        showinfo('Error', 'NIM tidak boleh lebih dari 6 digit!')
        return 
    
    mhs = Mahasiswa(nama, int(nim), jurusan)
    mhs.info_mahasiswa()
    
# Buat GUI
window = tk.Tk()
window.title('Form Mahasiswa')

ttk.Label(window, text='Nama : ').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry_nama = ttk.Entry(window)
entry_nama.grid(row=0, column=1, padx=5, pady=5)


ttk.Label(window, text='NIM : ').grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
entry_nim = ttk.Entry(window)
entry_nim.grid(row=1, column=1, padx=5,pady=5)

ttk.Label(window, text='Jurusan : ').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
entry_jurusan = ttk.Entry(window)
entry_jurusan.grid(row=2, column=1, padx=5, pady=5)

ttk.Button(window, text='Kirim', command=submit_on).grid(row=3, column=1, sticky=tk.E, padx=5, pady=10)

window.mainloop()        
