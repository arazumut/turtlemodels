
import tkinter as tk

aray�z = tk.Tk() 
aray�z.title("Kullan�c� Giri� Ekran�") 
aray�z.geometry("250x300") 


a1 = []
a2 = []

def giris_komut():
    kullan = y.get()
    sifre = x.get()
    print(kullan, sifre)
    if kullan in a1 and sifre in a2:
        print("�ifre Ve Kullan�c� Ad� Do�ru")
        Dogru = tk.Label(text="�ifre Ve Kullan�c� Ad� Do�ru", fg="green")
        Dogru.place(x=10, y=130)
    else:
        print("�ifre Veya Kullan�c� Ad� Yanl��")
        Yanl�s = tk.Label(text="�ifre Veya Kullan�c� Ad� Yanl��", fg="red")
        Yanl�s.place(x=10, y=130)

def kayit_ol():
    kullan = y.get()
    sifre = x.get()
    
    a1.append(kullan)
    a2.append(sifre)
    print("Yeni kullan�c� kaydedildi:", kullan, sifre)

kullanici = tk.Label(text="KULLANICI ADI:")
kullanici.place(x=10, y=10)

y = tk.StringVar()
kullanici_girisi = tk.Entry(textvariable=y)
kullanici_girisi.place(x=100, y=11)

sifre = tk.Label(text="��FRE G�R���:")
sifre.place(x=20, y=40)

x = tk.StringVar()
sifre_girisi = tk.Entry(textvariable=x)
sifre_girisi.place(x=100, y=41)

giris = tk.Button(text="G�R��", command=giris_komut)
giris.place(x=10, y=70)

kayit_ol = tk.Button(text="KAYIT OL", command=kayit_ol)
kayit_ol.place(x=10, y=100)

aray�z.mainloop()
