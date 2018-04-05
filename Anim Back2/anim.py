from Tkinter import *
from PIL import ImageTk, Image
import os
import time

running = True

def blink():
   if running:
	b.config(image=img1)
	root.configure(background='black')
	b.after(100,lambda:b.config(image=img2))
	c.config(image=img1)
        root.configure(background='black')
        c.after(100,lambda:c.config(image=img2))

	b.config(image=img2)
	root.configure(background='black')
	b.after(150,lambda:b.config(image=img3))
	c.config(image=img1)
        root.configure(background='black')
        c.after(100,lambda:c.config(image=img3))


	b.config(image=img3)
	root.configure(background='black')
	b.after(150,lambda:b.config(image=img4))
	c.config(image=img1)
        root.configure(background='black')
        c.after(150,lambda:c.config(image=img4))


	b.config(image=img4)
	root.configure(background='black')
	b.after(200,lambda:b.config(image=img5))
	c.config(image=img1)
        root.configure(background='black')
        c.after(200,lambda:c.config(image=img5))


	b.config(image=img5)
        root.configure(background='black')
        b.after(200,lambda:b.config(image=img6))
	c.config(image=img1)
        root.configure(background='black')
        c.after(200,lambda:c.config(image=img6))


        b.config(image=img6)
        root.configure(background='black')
        b.after(250,lambda:b.config(image=img7))
	c.config(image=img1)
        root.configure(background='black')
        c.after(250,lambda:c.config(image=img7))


        b.config(image=img7)
        root.configure(background='black')
        b.after(250,lambda:b.config(image=img8))
	c.config(image=img1)
        root.configure(background='black')
        c.after(250,lambda:c.config(image=img8))


	b.config(image=img8)
        root.configure(background='black')
        b.after(300,lambda:b.config(image=img9))
	c.config(image=img1)
        root.configure(background='black')
        c.after(300,lambda:c.config(image=img9))


        b.config(image=img9)
        root.configure(background='black')
        b.after(300,lambda:b.config(image=img10))
	c.config(image=img9)
        root.configure(background='black')
        c.after(300,lambda:c.config(image=img10))


        b.config(image=img10)
        root.configure(background='black')
        b.after(350,lambda:b.config(image=img11))
	c.config(image=img10)
        root.configure(background='black')
        c.after(350,lambda:c.config(image=img11))


        b.config(image=img11)
        root.configure(background='black')
        b.after(350,lambda:b.config(image=img12))
	c.config(image=img11)
        root.configure(background='black')
        c.after(350,lambda:c.config(image=img12))

        b.config(image=img12)
        root.configure(background='black')
        b.after(400,lambda:b.config(image=img13))
	c.config(image=img12)
        root.configure(background='black')
        c.after(400,lambda:c.config(image=img13))

        b.config(image=img13)
        root.configure(background='black')
        b.after(400,lambda:b.config(image=img14))
	c.config(image=img13)
        root.configure(background='black')
        c.after(400,lambda:c.config(image=img14))

        b.config(image=img14)
        root.configure(background='black')
        b.after(450,lambda:b.config(image=img15))
	c.config(image=img14)
        root.configure(background='black')
        c.after(450,lambda:c.config(image=img15))

	b.config(image=img15)
        root.configure(background='black')
        b.after(450,lambda:b.config(image=img16))
	c.config(image=img15)
        root.configure(background='black')
        c.after(450,lambda:c.config(image=img16))


        b.config(image=img16)
	root.configure(background='black')
        b.after(500,lambda:b.config(image=img1))
	c.config(image=img16)
        root.configure(background='black')
        c.after(500,lambda:c.config(image=img1))

   root.after(5000,blink)
def start():
	global running
	running=True
def stop():
	global running
	running= False
	b1.visible= False

		
root=Tk()
#root.configure(background='black')
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
#top=Frame(root,background='black',height=1000,width=2000)
#bottom=Frame(root,background='black',height=1000,width=2000)
#bottom.pack(fill="both",expand=True,padx=20,pady=20)
#top.place(in_=bottom,anchor="c",relx=0.5,rely=0.5)
img1= PhotoImage(file="round.gif",format="gif -index 0")
img2= PhotoImage(file="round.gif",format="gif -index 0")
img3= PhotoImage(file="round.gif",format="gif -index 1")
img4= PhotoImage(file="round.gif",format="gif -index 1")
img5= PhotoImage(file="round.gif",format="gif -index 2")
img6= PhotoImage(file="round.gif",format="gif -index 2")
img7= PhotoImage(file="round.gif",format="gif -index 3")
img8= PhotoImage(file="round.gif",format="gif -index 3")
img9= PhotoImage(file="round.gif",format="gif -index 4")
img10= PhotoImage(file="round.gif",format="gif -index 4")
img11= PhotoImage(file="round.gif",format="gif -index 5")
img12= PhotoImage(file="round.gif",format="gif -index 5")
img13= PhotoImage(file="round.gif",format="gif -index 6")
img14= PhotoImage(file="round.gif",format="gif -index 6")
img15= PhotoImage(file="round.gif",format="gif -index 7")
img16= PhotoImage(file="round.gif",format="gif -index 7")

#panel=Label(root, image=img1)
#panel.pack(side="bottom",fill="both",expand="yes")
main_frame= Frame(root)
main_frame.grid(row=3)

frame1 = Frame(main_frame,bg="black",width=800,height=90)
frame2 = Frame(main_frame,bg="black",width=70,height=300)
frame3 = Frame(main_frame,bg="black",width=300,height=300)
frame4 = Frame(main_frame,bg="black",width=60,height=300)
frame5 = Frame(main_frame,bg="black",width=300,height=300)
frame6 = Frame(main_frame,bg="black",width=70,height=300)
frame7 = Frame(main_frame,bg="black",width=800,height=90)

frame1.grid(row=1,column=1,columnspan=5)
frame2.grid(row=2,column=1)
frame3.grid(row=2,column=2)
frame4.grid(row=2,column=3)
frame5.grid(row=2,column=4)
frame6.grid(row=2,column=5)
frame7.grid(row=3,column=1,columnspan=5)
frame3.pack_propagate(0)
frame5.pack_propagate(0)
frame2.pack_propagate(0)
frame6.pack_propagate(0)


b=Button(frame3,bg='black',fg='black',image=img1,state='normal',activebackground='black',relief='flat',command=start,borderwidth=0,highlightbackground='black')
c=Button(frame5,bg='black',fg='black',state='normal',relief='flat',activebackground='black',image=img1,command=stop,borderwidth=0,highlightbackground='black')
#b.config(height=200,width=200)

#b.place(relx=0.5,rely=0.5,anchor=CENTER)
#c.place(relx=0.5,rely=0.5,anchor=CENTER)
b1= Button(frame2,text="1",width=7,height=6)
b2= Button(frame2,text="2",width=7,height=7)
b3= Button(frame2,text="3",width=7,height=6)
b4= Button(frame6,text="4",width=7,height=6)
b5= Button(frame6,text="5",width=7,height=7)
b6= Button(frame6,text="6",width=7,height=6)

#b1.pack(side=TOP)
#b2.pack(side=TOP)
#b3.pack(side=TOP)
#b4.pack(side=TOP)
#b5.pack(side=TOP)
#b6.pack(side=TOP)

b1.visible= False

b.pack(side=LEFT)
c.pack(side=RIGHT)
root.after(100,blink)
root.mainloop()

