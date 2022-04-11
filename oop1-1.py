from tkinter import *
window = Tk()

window.geometry("500x400+30+20")
window.title("Welcome to Python Programming")

#add button widget
btn = Button(window, text="Click to add name", fg="blue")
btn.place(x=80, y=100)

#add label widget
lbl = Label(window, text="Student Personal Information", fg="blue", bg="orange")
lbl.place(relx=.5, y=50, anchor='center')

lbl2 = Label(window, text="Gender", fg="red")
lbl2.place(x=80, y=150)

#add text field widget
txtfld = Entry(window, bd=3, font=("Verdana", 16))
txtfld.place(x=250,  y=100)

#add radio button
v1 = StringVar()
v2 = StringVar()
#v1.set(1)

r1 = Radiobutton(window, text="Male",value=1)
r1.place(x=80, y=200)

r2 = Radiobutton(window, text="Female",value=2)
r2.place(x=200, y=200)

#add checkbox

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
chckbox = Checkbutton(window,text="basketball",variable=v3)
chckbox2 = Checkbutton(window,text="tennis",variable=v4)
chckbox3 = Checkbutton(window,text="swimming",variable=v5)

chckbox.place(x=80, y=300)
chckbox2.place(x=220, y=300)
chckbox3.place(x=350, y=300)

#add listbox
lbl3 = Label(window, text="Sports")
lbl3.place(x=80, y=270)
lbl4 = Label(window, text = "Subjects")
lbl4.place(x=80, y=350)
var = StringVar ()
var.set("arithmetic")
data1 = "arithmetic"
data2 = "reading"
data3 = "writing"
lstbox = Listbox(window, height=5, selectmode='multiple')
lstbox.insert(END,data1,data2,data3)
lstbox.place(x=80, y=400)

window.mainloop()
