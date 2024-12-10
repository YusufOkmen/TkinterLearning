# TEKRAR UYGULAMASI"

"""
1-50 arasında 5 adet rastgele sayı üretip göster adındaki butona tıklandığında label'a yazdırsın, değerleri saydamlaştır adında buton olup penceremizi saydamlaştırsın, eski haline döndürmek için döndün butonu olsun, max ve min yap butonları ile de pencereyi tam ekran yapıp küçültebilelim
"""

import tkinter as tk
import random


liste = []

for repeat in range(5):
    sayi = random.randrange(1,50)
    liste.append(sayi)


form = tk.Tk()
form.title("Practise")
form.geometry("500x500")



def sayiGoster():
    randomlabel = tk.Label(form, fg="green", bg="pink")
    randomlabel.pack()

    randomlabel.config(text= liste)


def transparency():
    form.attributes("-alpha", 0.5)


def revTrans():
    form.attributes("-alpha", 1)


def zoomed():
    form.state("zoomed")

def window():
    form.state("normal")

randombutton = tk.Button(form, text="Random Numbers", fg="yellow", bg="green", command=sayiGoster)
randombutton.pack()

transparencyB = tk.Button(form, text="Transparency", command=transparency)
transparencyB.pack()

reverseTrans = tk.Button(form, text="Reverse the Transparency", fg="pink", bg="gray", command=revTrans)
reverseTrans.pack()

fullScreen = tk.Button(form, text="FullScreen", fg="black", bg="yellow", command=zoomed)
fullScreen.pack()

normalScreen = tk.Button(form, text="SmallScreen", fg="red", bg="black", command=window)
normalScreen.pack()

form.mainloop()