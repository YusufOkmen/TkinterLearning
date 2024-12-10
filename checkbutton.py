import tkinter as tk

form = tk.Tk()
form.title("CHECKBUTTON")
form.geometry("500x500+250+250")

x = tk.IntVar()
x.set(0)

def control():
    if x.get() == 0:
        print("Onaylanmadı")
    else:
        print("Onaylandı" )

check = tk.Checkbutton(form, text="Onay", fg="white", bg="black", variable=x, command=control)
check.pack()





form.mainloop()