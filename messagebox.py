import tkinter as tk
from tkinter import messagebox

def message():
    messagebox.showinfo(title="mesaj1", message="Selam Ben Yusuf Ökmen")
    messagebox.askretrycancel(title="mesaj2", message="Selam Ben Abdullah Ökmen")
    messagebox.askyesno(title="mesaj3", message="Selam Ben Elif Ökmen")
    messagebox.askquestion(title="mesaj4", message="Selam Ben Emine Ökmen")

form = tk.Tk()
form.title("MESSAGEBOX")
form.geometry("500x500+250+250")

button = tk.Button(form, text="click and you will recieve the message", command=message).pack()








form.mainloop()