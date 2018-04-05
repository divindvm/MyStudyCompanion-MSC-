from Tkinter import *
from PIL import ImageTk, Image
import os
import time

root=Tk()
#root.overrideredirect(True)
root.attributes("-fullscreen",1)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

main_frame= Frame(root)
main_frame.grid(row=0)

frame1 = Frame(main_frame,bg="black",width=800,height=40)
frame2 = Frame(main_frame,bg="white",width=800,height=80)
frame3 = Frame(main_frame,bg="black",width=800,height=90)
frame4 = Frame(main_frame,bg="white",width=800,height=90)
frame5 = Frame(main_frame,bg="black",width=800,height=90)
frame6 = Frame(main_frame,bg="white",width=800,height=90)

frame1.grid(row=1,column=1,columnspan=5)
frame2.grid(row=2,column=1,columnspan=5)
frame3.grid(row=3,column=1,columnspan=5)
frame4.grid(row=4,column=1,columnspan=5)
frame5.grid(row=5,column=1,columnspan=5)
frame6.grid(row=6,column=1,columnspan=5)

frame1.pack_propagate(0)
frame2.pack_propagate(0)
frame3.pack_propagate(0)
frame4.pack_propagate(0)
frame5.pack_propagate(0)
frame6.pack_propagate(0)

def btnClick(numbers):
        global operator
        operator=operator+str(numbers)
        text_Input.set(operator)

def btnClearDisplay():
        global operator
        operator=""
        text_Input.set("")

def btnEqualsInput():
        global operator
        sumup=str(eval(operator))
        text_Input.set(sumup)    
        operator=sumup
def delete_entries():
        global operator
        temp=text_Input.get()
        temp=temp[:-1]
        operator=str(temp)
        text_Input.set(temp)



operator=""
text_Input =StringVar()

txtDisplay =Entry(frame2,font=('arial',20,'bold'),textvariable=text_Input, bd=7 ,insertwidth=8,
                  bg="white",justify='right').pack(side=LEFT,expand=YES,fill=BOTH)



l= Label(frame1,text='MSC Calculator',font=("Arial",12,"bold"),bg='black',fg='grey')
l.pack(side=LEFT)







def callback():
    print e.get()










b1=Button(frame3,text="7",command=lambda:btnClick(7),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
b2=Button(frame3,text="8",command=lambda:btnClick(8),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
b3=Button(frame3,text="9",command=lambda:btnClick(9),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',borderwidth=0,relief='flat',highlightbackground='grey')
b4=Button(frame3,text="/",command=lambda:btnClick("/"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
b5=Button(frame3,text="C",command=delete_entries,font=("Arial",10,"bold"),width=20,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
b6=Button(frame4,text="4",command=lambda:btnClick(4),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
b7=Button(frame4,text="5",command=lambda:btnClick(5),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
b8=Button(frame4,text="6",command=lambda:btnClick(6),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
b9=Button(frame4,text="x",command=lambda:btnClick("*"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
b10=Button(frame4,text="AC",command=btnClearDisplay,font=("Arial",10,"bold"),width=20,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')

b11=Button(frame5,text="1",command=lambda:btnClick(1),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
b12=Button(frame5,text="2",command=lambda:btnClick(2),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
b13=Button(frame5,text="3",command=lambda:btnClick(3),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
b14=Button(frame5,text="-",command=lambda:btnClick("-"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
b15=Button(frame5,text="v",command=lambda:btnClick("**0.5"),font=("Arial",10,"bold"),width=20,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
b16=Button(frame6,text="0",command=lambda:btnClick(0),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
b17=Button(frame6,text=".",command=lambda:btnClick("."),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
b18=Button(frame6,text="%",command=lambda:btnClick("%"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
b19=Button(frame6,text="+",command=lambda:btnClick("+"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
b20=Button(frame6,text="=",command=btnEqualsInput,font=("Arial",10,"bold"),width=20,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
b6.pack(side=LEFT)
b7.pack(side=LEFT)
b8.pack(side=LEFT)
b9.pack(side=LEFT)
b10.pack(side=LEFT)

b11.pack(side=LEFT)
b12.pack(side=LEFT)
b13.pack(side=LEFT)
b14.pack(side=LEFT)
b15.pack(side=LEFT)
b16.pack(side=LEFT)
b17.pack(side=LEFT)
b18.pack(side=LEFT)
b19.pack(side=LEFT)
b20.pack(side=LEFT)


def click(key):
    print key.char


def close():
    root.destroy()

c=Button(frame1,text="X",bg='red',fg='white',state='normal',relief='flat',activebackground='black',command=close,borderwidth=0,highlightbackground='black')
c.pack(side=RIGHT)
root.mainloop()

