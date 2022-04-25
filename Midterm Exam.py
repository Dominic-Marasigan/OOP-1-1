from tkinter import *
window = Tk()
window.geometry("700x400")
window.title("Midterm in OOP")

L1=Label(window, text="Enter your fullname:", fg="Red")
L1.place(x=50, y=100)

str1=StringVar()
str2=StringVar()

def Click():
    str2.set(str1.get())

E1=Entry(window, font="Verdana", width=20, bd=6, textvariable=str1)
E1.place(x=300, y=100)
E2=Entry(window, font="Verdana", width=20, bd=6, textvariable=str2)
E2.place(x=300, y=150)

B1=Button(window, text="Click to display your Fullname", fg="Red", command=lambda:Click())
B1.place(x=50, y=150)

window.mainloop()