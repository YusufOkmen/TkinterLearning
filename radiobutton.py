import tkinter as tk

form = tk.Tk()
form.title("RADIOBUTTON")
form.geometry("500x500+250+250")

def control():
    if  x.get() == "1":
        print("Kadın")
    
    elif x.get() == "2":
        print("Erkek")

    else:
        print("Kadın veya Erkek")

button = tk.Button(form, text="Clıck me", fg="white", bg="black", activebackground="red", command=control)
button.pack()

x = tk.StringVar()

radio = tk.Radiobutton(form,
                       text="Radio Button 1",
                       activebackground="purple", 
                       value=1, 
                       variable=x)
radio.pack()

radio2 = tk.Radiobutton(form,
                       text="Radio Button 2",
                       activebackground="green", 
                       value=2, 
                       variable=x)
radio2.pack()








form.mainloop()