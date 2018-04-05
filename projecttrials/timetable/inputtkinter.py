from Tkinter import *


def get_class():
	print(var.get())
def get_entry():
	print(ent.get())
	lsum["text"]="ohh noooo"
	textinp.set("shit")

root=Tk()
var=StringVar()
textinp=StringVar()

ent=Entry(root,textvariable=var)
ent.place(x=10,y=10,width=100)
ent2=Entry(root,textvariable=textinp)
lsum=Label(root,text="the")
btn1=Button(root,text="Variable class",command=get_class)
btn2=Button(root,text="Get Method",command=get_entry)
ent.pack()
ent2.pack()
btn1.pack()
btn2.pack()
lsum.pack()
root.mainloop()
