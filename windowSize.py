import tkinter as tk

form = tk.Tk()
form.title("Window Sizing")

form.geometry("500x500+250+250")# width, height, x, y

# form.minsize(400,400)
# form.maxsize(500,500)

form.resizable(False, False)# Can't pull width or height





label1 = tk.Label(form, text="Yusuf", fg="pink", bg="blue", font="24")
label1.pack()




form.mainloop()
