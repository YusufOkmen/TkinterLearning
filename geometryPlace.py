import tkinter as tk

form = tk.Tk()
form.title("Place")
form.geometry("500x500+250+250")

button = tk.Button(form, text="Test", fg="yellow", bg="green", font="Times 17 italic")
# button.place(x=100, y=50) 
button.place(relx=0.5, rely=0.5) # with this code line, our button can move with the window.

button.place(width=100, height=100) # with this code line, we can control out button's width and height.












form.mainloop()