import tkinter as tk

form = tk.Tk()
form.title("Entry")
form.geometry("500x500+250+250")

giris = tk.Entry(form, fg="orange", bg="green")
giris.pack(side=tk.RIGHT)

giris2 = tk.Entry(form, fg="white", bg="black")
giris2.pack(side=tk.LEFT)

form.mainloop()