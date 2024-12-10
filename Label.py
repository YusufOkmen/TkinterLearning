import tkinter as tk

form = tk.Tk()
form.title("Label Lesson")

label1 = tk.Label(form, text="Hello World")
label1.pack()

label2 = tk.Label(form, text="My name is Yusuf Ökmen", fg="White", bg="black", font="Times 21 italic")
label2.pack()

label3 = tk.Label(form, text="My mother's name is Emine Ökmen", fg="green", bg="yellow", font="Times 15 bold")
label3.pack()

form.mainloop()