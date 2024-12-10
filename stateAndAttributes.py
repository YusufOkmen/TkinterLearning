import tkinter as tk

form = tk.Tk()
form.title("Hoş Geldiniz!")
form.geometry("300x300+500+350")

form.state("normal")# The style of the window when it is first opened
# form.state("iconic")
# form.state("zoomed")

form.wm_attributes("-alpha", 0.6) # transparency



form.mainloop()