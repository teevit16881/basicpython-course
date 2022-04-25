#GUI-calculator.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() # T ตัวใหญ่ k ตัวเล็ก
GUI.title('Convert Moles to Numbers of Particles')
GUI.geometry('500x450')

bg = PhotoImage(file='molecules_1.png')
BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='Input Amount of Substance in Mole(s)',font=(None,20))
L.pack(pady=10)

v_mol = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_mol, font=(None,20))
E1.pack(pady=10)

def Cal():
    try:    
        quan = float(v_mol.get())
        calc = quan * 6.022 * (10**23) # 1 mol = 6.022*10^23
        messagebox.showinfo('No. of Particles','{} Particles'.format(calc))
        v_mol.set('1')
        E1.focus() #โฟกัส cursor ไปที่ช่องกรอก E1 หลังจาก try
    except:
        messagebox.showwarning('invalid input data','please input numbers of moles')
        v_mol.set('1')

B = ttk.Button(GUI, text='Calculate',command=Cal)
B.pack(ipadx=20,ipady=15) #ipadx ขยายความกว้าง x/y

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา