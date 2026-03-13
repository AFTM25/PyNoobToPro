import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox import showinfo 

class Perhitungan:
    def __init__(self, angka1, angka2):
        self.__angka1 = angka1 
        self.__angka2 = angka2 
        
    @property 
    def angka1(self):
        return self.__angka1 
    
    @property 
    def angka2(self):
        return self.__angka2 
    
    def __add__(self):
        return self.__angka1 + self.__angka2 
    
    def __sub__(self):
        return self.__angka1 - self.__angka2 
    
    def __mul__(self):
        return self.__angka1 * self.__angka2
    
    def __truediv__(self):
        return self.__angka1 / self.__angka2 if self.__angka2 != 0 else 'Tidak dapat dibagi dengan nol'
    
    def __call__(self, operasi):
        match operasi:
            case '+':
                showinfo('Tambah', 
                        f'{self.__angka1} + {self.__angka2} = {self.__add__()}')
            case '-':
                showinfo('Kurang',
                        f'{self.__angka1} - {self.__angka2} = {self.__sub__()}')
                
            case 'x':
                showinfo('Perkalian',
                        f'{self.__angka1} x {self.__angka2} = {self.__mul__()}')
                
            case '/':
                showinfo('Pembagian',
                        f'{self.__angka1} / {self.__angka2} = {self.__truediv__()}')                
            case _:
                raise ValueError('Operator tidak dapat dikenali!')
            
def submit_on(operasi=None):
    angka1 = entry_angka1.get().strip()
    angka2 = entry_angka2.get().strip()
    
    if not angka1 or not angka2:
        showinfo('Error', 'Form tidak boleh kosong!')
        return 
    
    if not angka1.isdigit() or not angka2.isdigit():
        showinfo('Error', 'Inputan harus berupa angka!')
        return
        
    if operasi is None:
        showinfo('Error lagi', 'Operasi belum dipilih cuy!')
        return
    
    x = Perhitungan(int(angka1), int(angka2))
    x(operasi)

def reset_btn():
    entry_angka1.delete(0, tk.END)
    entry_angka2.delete(0, tk.END)

# Membuat GUI 
wd = tk.Tk() 
wd.title('Perhitungan Sederhana')
wd.geometry('300x300')
wd.resizable(False, False)
wd.configure(bg='chocolate')

ttk.Label(wd, text='Input Angka Pertama ').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry_angka1 = ttk.Entry(wd)
entry_angka1.grid(row=0, column=1, padx=5, pady=5) 

ttk.Label(wd, text='Input Angka Kedua ').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entry_angka2 = ttk.Entry(wd)
entry_angka2.grid(row=1, column=1, padx=5, pady=5)

ttk.Button(wd, text='Submit', command=submit_on).grid(row=3, column=0, pady=10, padx=5, sticky=tk.E)

ttk.Button(wd, text='Reset', command=reset_btn).grid(row=3, column=1, sticky=tk.E, padx=5, pady=10)

frm_opr = ttk.Frame(wd)
frm_opr.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

ttk.Button(frm_opr, text='+', command=lambda : submit_on('+')).grid(row=0, column=0, padx=5, pady=5)

ttk.Button(frm_opr, text='-', command=lambda : submit_on('-')).grid(row=1, column=0, padx=5, pady=5)

ttk.Button(frm_opr, text='x', command=lambda : submit_on('x')).grid(row=2, column=0, padx=5, pady=5)

ttk.Button(frm_opr, text='/', command=lambda:submit_on('/')).grid(row=3, column=0, padx=5, pady=5)

wd.bind('<Return>', lambda event:submit_on())
wd.bind('<Escape>', lambda event:reset_btn())
wd.mainloop()       
