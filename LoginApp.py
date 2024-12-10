import tkinter as tk

form = tk.Tk()
form.title("LOGIN APP")
form.geometry("500x500+250+250")

def sil():
    entry1.delete(0, "end")
    entry2.delete(0, "end")

def signIn():
    label3 = tk.Label(form, text="Username", fg="white", bg="black")
    label3.place(x=10, y=200)

    label4 = tk.Label(form, text="Email", fg="white", bg="black")
    label4.place(x=10, y=230)

    label5 = tk.Label(form, text="Password", fg="white", bg="black")
    label5.place(x=10, y=260)

    entry3 = tk.Entry(form)
    entry3.place(x=80, y=200)

    entry4 = tk.Entry(form)
    entry4.place(x=80, y=230)

    entry5 = tk.Entry(form, show="*")
    entry5.place(x=80, y=260)

    def sil2():
        entry3.delete(0, "end")
        entry4.delete(0, "end")
        entry5.delete(0, "end")

    button3 = tk.Button(form, text="Finish", fg="white", bg="black", command=sil2)
    button3.place(x=120, y=290)

label1 = tk.Label(form, text="Username", fg="white", bg="black")
label1.place(x=10, y=50)

label2 = tk.Label(form, text="Password", fg="white", bg="black")
label2.place(x=10, y=80)

entry1 = tk.Entry(form)
entry1.place(x=80, y = 50)

entry2 = tk.Entry(form, show="*")
entry2.place(x=80, y = 80)

button1 = tk.Button(form, text="Sign In", fg="white", bg="black", command=signIn)
button1.place(x=100, y=110)

button2 = tk.Button(form, text="Login", fg="white", bg="black", command=sil)
button2.place(x=150, y=110)


form.mainloop()