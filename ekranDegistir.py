import tkinter as tk

def ikinciekranagit():
    ikiekran.deiconify()
    anaekran.withdraw()
    ikiekran.title("İkinci Ekran")
    
def birinciekranagit():
    anaekran.deiconify()
    ikiekran.withdraw()


anaekran = tk.Tk()
anaekran.title("Ana Ekran")
anaekran.geometry("300x200+400+400")

ikiekran = tk.Toplevel()
ikiekran.title("İkinci Ekran")
ikiekran.geometry("300x200+400+400")
ikiekran.withdraw()

btn1 = tk.Button(anaekran, text="İkinci Ekranı Aç.", command = ikinciekranagit)
btn1.pack()

btn2=tk.Button(ikiekran, text="Birinci Ekrana Git", command = birinciekranagit)
btn2.pack()

anaekran.mainloop()
