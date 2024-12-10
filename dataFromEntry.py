import tkinter as tk

form = tk.Tk()
form.title("ENTRY AND DATA")
form.geometry("500x500+250+250")

entry = tk.Entry(form)
entry.pack()

entry2 = tk.Entry(form, show="*")
entry2.pack()

def verial():
    etiket["text"] = entry.get()

def sil():
    entry.delete(0,"end")
    entry2.delete(0,"end")

button = tk.Button(form, text="verileri çek", fg="green", bg="red", command=verial)
button.pack()

button = tk.Button(form, text="verileri sil", fg="red", bg="green", command=sil)
button.pack()

etiket = tk.Label(text="verileri buraya çek")
etiket.pack()




form.mainloop()
