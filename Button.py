import tkinter as tk


form = tk.Tk()

form.title("Butonlar")

form.geometry("500x500+500+350")

def topla():
    print("toplama")

button = tk.Button(form, text="CLICK", fg="white", bg="pink", command=topla)
button.pack(side = tk.RIGHT)# command = when you click the button this command will be display.# side = tk.RIGHT: Put this button on the right side of the interface

button2 = tk.Button(form,  text="DON'T CLICK ME", command=topla)
button2.pack(side = tk.LEFT)


form.mainloop()
