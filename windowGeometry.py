"""
side = left ,right, bottom, top
fill = x, y
expand = 0 - 1
anchor = "n" yukarı, "s" aşağı, "e" sağ, "w" sol, "ne" yukarı sağ, "nw" yukarı sol, "se" aşağı sağ, "sw" aşağı sol, "center" orta
"""


import tkinter as tk

form = tk.Tk()
form.geometry("500x500+250+250")



label = tk.Label(text="By Yusuf Ökmen", fg="white", bg="black")
label.pack(side=tk.TOP)

button = tk.Button(text="Geometri", bg="red")
button.pack(padx=50 ,pady=50)




form.mainloop()