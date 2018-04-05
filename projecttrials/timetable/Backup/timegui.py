from Tkinter import *

tim=Tk()
#cal.title("Calculator")
operator=" "
text_Input =StringVar()
tim.attributes("-fullscreen",1)

main_frame= Frame(tim)
main_frame.grid(row=0)




frame1 = Frame(main_frame,bg="black",width=800,height=40)
frame2 = Frame(main_frame,bg="grey",width=800,height=5)
frame3 = Frame(main_frame,bg="blue",width=800,height=50)
frame4 = Frame(main_frame,bg="red",width=800,height=50)
frame5 = Frame(main_frame,bg="black",width=800,height=50)
frame6 = Frame(main_frame,bg="white",width=800,height=50)
frame7 = Frame(main_frame,bg="black",width=800,height=50)
frame8 = Frame(main_frame,bg="white",width=800,height=50)
frame9 = Frame(main_frame,bg="black",width=800,height=50)
frame10 = Frame(main_frame,bg="black",width=800,height=10)
frame11 = Frame(main_frame,bg="grey",width=800,height=5)
frame12 = Frame(main_frame,bg="black",width=800,height=50)
frame13 = Frame(main_frame,bg="black",width=800,height=50)

frame1.grid(row=1,column=1,columnspan=5)
frame2.grid(row=2,column=1,columnspan=5)
frame3.grid(row=3,column=1,columnspan=5)
frame4.grid(row=4,column=1,columnspan=5)
frame5.grid(row=5,column=1,columnspan=5)
frame6.grid(row=6,column=1,columnspan=5)
frame7.grid(row=7,column=1,columnspan=5)
frame8.grid(row=8,column=1,columnspan=5)
frame9.grid(row=9,column=1,columnspan=5)
frame10.grid(row=10,column=1,columnspan=5)
frame11.grid(row=11,column=1,columnspan=5)
frame12.grid(row=12,column=1,columnspan=5)
frame13.grid(row=13,column=1,columnspan=5)


frame1.pack_propagate(0)
frame2.pack_propagate(0)
frame3.pack_propagate(0)
frame4.pack_propagate(0)
frame5.pack_propagate(0)
frame6.pack_propagate(0)
frame7.pack_propagate(0)
frame8.pack_propagate(0)
frame9.pack_propagate(0)
frame10.pack_propagate(0)
frame11.pack_propagate(0)


head=Label(frame1,text=" MSC Time Table ",bg="black",fg="white")
head.pack(side=LEFT)


#txtDisplay =Entry(frame3,font=('arial',20,'bold'),textvariable=text_Input, bd=30 ,insertwidth=4,
#		  bg="powder blue",justify='right').grid(columnspan=4)


#----------------------------Periods------------------------------------------------
p1 = Frame(frame3,bg="black",width=100,height=50)
p2 = Frame(frame3,bg="black",width=100,height=50)
p3 = Frame(frame3,bg="black",width=100,height=50)
p4 = Frame(frame3,bg="black",width=100,height=50)
p5 = Frame(frame3,bg="black",width=100,height=50)
p6 = Frame(frame3,bg="black",width=100,height=50)
p7 = Frame(frame3,bg="black",width=100,height=50)
p8 = Frame(frame3,bg="black",width=100,height=50)

p1.grid(row=1,column=1,columnspan=1)
p2.grid(row=1,column=2,columnspan=1)
p3.grid(row=1,column=3,columnspan=1)
p4.grid(row=1,column=4,columnspan=1)
p5.grid(row=1,column=5,columnspan=1)
p6.grid(row=1,column=6,columnspan=1)
p7.grid(row=1,column=7,columnspan=1)
p8.grid(row=1,column=8,columnspan=1)

p1.pack_propagate(0)
p2.pack_propagate(0)
p3.pack_propagate(0)
p4.pack_propagate(0)
p5.pack_propagate(0)
p6.pack_propagate(0)
p7.pack_propagate(0)
p8.pack_propagate(0)

pl7=Label(p1,text="  Days/Periods  ",fg="grey",bg="black")
pl7.pack(side=LEFT)
pl1=Label(p2,text="                1  ",fg="grey",bg="black")
pl1.pack(side=LEFT)
pl2=Label(p3,text="                2  ",fg="grey",bg="black")
pl2.pack(side=LEFT)
pl3=Label(p4,text="                3  ",fg="grey",bg="black")
pl3.pack(side=LEFT)
pl4=Label(p5,text="                4  ",fg="grey",bg="black")
pl4.pack(side=LEFT)
pl5=Label(p6,text="                5  ",fg="grey",bg="black")
pl5.pack(side=LEFT)
pl6=Label(p7,text="                6  ",fg="grey",bg="black")
pl6.pack(side=LEFT)
pl7=Label(p8,text="                7  ",fg="grey",bg="black")
pl7.pack(side=LEFT)




#-------------------------------------------------------------------------------------------



#----------------------------monday------------------------------------------------
m1 = Frame(frame4,bg="black",width=100,height=50)
m2 = Frame(frame4,bg="white",width=100,height=50)
m3 = Frame(frame4,bg="blue",width=100,height=50)
m4 = Frame(frame4,bg="white",width=100,height=50)
m5 = Frame(frame4,bg="black",width=100,height=50)
m6 = Frame(frame4,bg="black",width=100,height=50)
m7 = Frame(frame4,bg="white",width=100,height=50)
m8 = Frame(frame4,bg="white",width=100,height=50)

m1.grid(row=1,column=1,columnspan=1)
m2.grid(row=1,column=2,columnspan=1)
m3.grid(row=1,column=3,columnspan=1)
m4.grid(row=1,column=4,columnspan=1)
m5.grid(row=1,column=5,columnspan=1)
m6.grid(row=1,column=6,columnspan=1)
m7.grid(row=1,column=7,columnspan=1)
m8.grid(row=1,column=8,columnspan=1)

m1.pack_propagate(0)
m2.pack_propagate(0)
m3.pack_propagate(0)
m4.pack_propagate(0)
m5.pack_propagate(0)
m6.pack_propagate(0)
m7.pack_propagate(0)
m8.pack_propagate(0)


l1=Label(m1,text="  Monday",fg="grey",bg="black")
l1.pack(side=LEFT)

me1=Entry(m2,insertwidth=3)
me1.pack(side=RIGHT,expand=YES,fill=Y)
me2=Entry(m3,insertwidth=3)
me2.pack(side=RIGHT,expand=YES,fill=Y)
me3=Entry(m4,insertwidth=3)
me3.pack(side=RIGHT,expand=YES,fill=Y)
me4=Entry(m5,insertwidth=3)
me4.pack(side=RIGHT,expand=YES,fill=Y)
me5=Entry(m6,insertwidth=3)
me5.pack(side=RIGHT,expand=YES,fill=Y)
me6=Entry(m7,insertwidth=3)
me6.pack(side=RIGHT,expand=YES,fill=Y)
me7=Entry(m8,insertwidth=3)
me7.pack(side=RIGHT,expand=YES,fill=Y)


#-------------------------------------------------------------------------------------------

#----------------------------Tuesday--------------------------------------------------------
t1 = Frame(frame5,bg="black",width=100,height=50)
t2 = Frame(frame5,bg="white",width=100,height=50)
t3 = Frame(frame5,bg="blue",width=100,height=50)
t4 = Frame(frame5,bg="white",width=100,height=50)
t5 = Frame(frame5,bg="black",width=100,height=50)
t6 = Frame(frame5,bg="black",width=100,height=50)
t7 = Frame(frame5,bg="white",width=100,height=50)
t8 = Frame(frame5,bg="white",width=100,height=50)

t1.grid(row=1,column=1,columnspan=1)
t2.grid(row=1,column=2,columnspan=1)
t3.grid(row=1,column=3,columnspan=1)
t4.grid(row=1,column=4,columnspan=1)
t5.grid(row=1,column=5,columnspan=1)
t6.grid(row=1,column=6,columnspan=1)
t7.grid(row=1,column=7,columnspan=1)
t8.grid(row=1,column=8,columnspan=1)

t1.pack_propagate(0)
t2.pack_propagate(0)
t3.pack_propagate(0)
t4.pack_propagate(0)
t5.pack_propagate(0)
t6.pack_propagate(0)
t7.pack_propagate(0)
t8.pack_propagate(0)


tl1=Label(t1,text="  Tuesday",fg="grey",bg="black")
tl1.pack(side=LEFT)

te1=Entry(t2,insertwidth=3)
te1.pack(side=RIGHT,expand=YES,fill=Y)
te2=Entry(t3,insertwidth=3)
te2.pack(side=RIGHT,expand=YES,fill=Y)
te3=Entry(t4,insertwidth=3)
te3.pack(side=RIGHT,expand=YES,fill=Y)
te4=Entry(t5,insertwidth=3)
te4.pack(side=RIGHT,expand=YES,fill=Y)
te5=Entry(t6,insertwidth=3)
te5.pack(side=RIGHT,expand=YES,fill=Y)
te6=Entry(t7,insertwidth=3)
te6.pack(side=RIGHT,expand=YES,fill=Y)
te7=Entry(t8,insertwidth=3)
te7.pack(side=RIGHT,expand=YES,fill=Y)


#-------------------------------------------------------------------------------------------


#----------------------------Wednesday--------------------------------------------------------
w1 = Frame(frame6,bg="black",width=100,height=50)
w2 = Frame(frame6,bg="white",width=100,height=50)
w3 = Frame(frame6,bg="blue",width=100,height=50)
w4 = Frame(frame6,bg="white",width=100,height=50)
w5 = Frame(frame6,bg="black",width=100,height=50)
w6 = Frame(frame6,bg="black",width=100,height=50)
w7 = Frame(frame6,bg="white",width=100,height=50)
w8 = Frame(frame6,bg="white",width=100,height=50)

w1.grid(row=1,column=1,columnspan=1)
w2.grid(row=1,column=2,columnspan=1)
w3.grid(row=1,column=3,columnspan=1)
w4.grid(row=1,column=4,columnspan=1)
w5.grid(row=1,column=5,columnspan=1)
w6.grid(row=1,column=6,columnspan=1)
w7.grid(row=1,column=7,columnspan=1)
w8.grid(row=1,column=8,columnspan=1)

w1.pack_propagate(0)
w2.pack_propagate(0)
w3.pack_propagate(0)
w4.pack_propagate(0)
w5.pack_propagate(0)
w6.pack_propagate(0)
w7.pack_propagate(0)
w8.pack_propagate(0)


wl1=Label(w1,text="  Wednesday",fg="grey",bg="black")
wl1.pack(side=LEFT)

we1=Entry(w2,insertwidth=3)
we1.pack(side=RIGHT,expand=YES,fill=Y)
we2=Entry(w3,insertwidth=3)
we2.pack(side=RIGHT,expand=YES,fill=Y)
we3=Entry(w4,insertwidth=3)
we3.pack(side=RIGHT,expand=YES,fill=Y)
we4=Entry(w5,insertwidth=3)
we4.pack(side=RIGHT,expand=YES,fill=Y)
we5=Entry(w6,insertwidth=3)
we5.pack(side=RIGHT,expand=YES,fill=Y)
we6=Entry(w7,insertwidth=3)
we6.pack(side=RIGHT,expand=YES,fill=Y)
we7=Entry(w8,insertwidth=3)
we7.pack(side=RIGHT,expand=YES,fill=Y)


#-------------------------------------------------------------------------------------------



#----------------------------Thursday--------------------------------------------------------
th1 = Frame(frame7,bg="black",width=100,height=50)
th2 = Frame(frame7,bg="white",width=100,height=50)
th3 = Frame(frame7,bg="blue",width=100,height=50)
th4 = Frame(frame7,bg="white",width=100,height=50)
th5 = Frame(frame7,bg="black",width=100,height=50)
th6 = Frame(frame7,bg="black",width=100,height=50)
th7 = Frame(frame7,bg="white",width=100,height=50)
th8 = Frame(frame7,bg="white",width=100,height=50)

th1.grid(row=1,column=1,columnspan=1)
th2.grid(row=1,column=2,columnspan=1)
th3.grid(row=1,column=3,columnspan=1)
th4.grid(row=1,column=4,columnspan=1)
th5.grid(row=1,column=5,columnspan=1)
th6.grid(row=1,column=6,columnspan=1)
th7.grid(row=1,column=7,columnspan=1)
th8.grid(row=1,column=8,columnspan=1)

th1.pack_propagate(0)
th2.pack_propagate(0)
th3.pack_propagate(0)
th4.pack_propagate(0)
th5.pack_propagate(0)
th6.pack_propagate(0)
th7.pack_propagate(0)
th8.pack_propagate(0)


thl1=Label(th1,text="  Thursday",fg="grey",bg="black")
thl1.pack(side=LEFT)

the1=Entry(th2,insertwidth=3)
the1.pack(side=RIGHT,expand=YES,fill=Y)
the2=Entry(th3,insertwidth=3)
the2.pack(side=RIGHT,expand=YES,fill=Y)
the3=Entry(th4,insertwidth=3)
the3.pack(side=RIGHT,expand=YES,fill=Y)
the4=Entry(th5,insertwidth=3)
the4.pack(side=RIGHT,expand=YES,fill=Y)
the5=Entry(th6,insertwidth=3)
the5.pack(side=RIGHT,expand=YES,fill=Y)
the6=Entry(th7,insertwidth=3)
the6.pack(side=RIGHT,expand=YES,fill=Y)
the7=Entry(th8,insertwidth=3)
the7.pack(side=RIGHT,expand=YES,fill=Y)


#-------------------------------------------------------------------------------------------


#----------------------------Friday--------------------------------------------------------
f1 = Frame(frame8,bg="black",width=100,height=50)
f2 = Frame(frame8,bg="white",width=100,height=50)
f3 = Frame(frame8,bg="blue",width=100,height=50)
f4 = Frame(frame8,bg="white",width=100,height=50)
f5 = Frame(frame8,bg="black",width=100,height=50)
f6 = Frame(frame8,bg="black",width=100,height=50)
f7 = Frame(frame8,bg="white",width=100,height=50)
f8 = Frame(frame8,bg="white",width=100,height=50)

f1.grid(row=1,column=1,columnspan=1)
f2.grid(row=1,column=2,columnspan=1)
f3.grid(row=1,column=3,columnspan=1)
f4.grid(row=1,column=4,columnspan=1)
f5.grid(row=1,column=5,columnspan=1)
f6.grid(row=1,column=6,columnspan=1)
f7.grid(row=1,column=7,columnspan=1)
f8.grid(row=1,column=8,columnspan=1)

f1.pack_propagate(0)
f2.pack_propagate(0)
f3.pack_propagate(0)
f4.pack_propagate(0)
f5.pack_propagate(0)
f6.pack_propagate(0)
f7.pack_propagate(0)
f8.pack_propagate(0)


fl1=Label(f1,text="  Friday",fg="grey",bg="black")
fl1.pack(side=LEFT)

fe1=Entry(f2,insertwidth=3)
fe1.pack(side=RIGHT,expand=YES,fill=Y)
fe2=Entry(f3,insertwidth=3)
fe2.pack(side=RIGHT,expand=YES,fill=Y)
fe3=Entry(f4,insertwidth=3)
fe3.pack(side=RIGHT,expand=YES,fill=Y)
fe4=Entry(f5,insertwidth=3)
fe4.pack(side=RIGHT,expand=YES,fill=Y)
fe5=Entry(f6,insertwidth=3)
fe5.pack(side=RIGHT,expand=YES,fill=Y)
fe6=Entry(f7,insertwidth=3)
fe6.pack(side=RIGHT,expand=YES,fill=Y)
fe7=Entry(f8,insertwidth=3)
fe7.pack(side=RIGHT,expand=YES,fill=Y)

#-------------------------------------------------------------------------------------------


#----------------------------Saturday--------------------------------------------------------
s1 = Frame(frame9,bg="black",width=100,height=50)
s2 = Frame(frame9,bg="white",width=100,height=50)
s3 = Frame(frame9,bg="blue",width=100,height=50)
s4 = Frame(frame9,bg="white",width=100,height=50)
s5 = Frame(frame9,bg="black",width=100,height=50)
s6 = Frame(frame9,bg="black",width=100,height=50)
s7 = Frame(frame9,bg="white",width=100,height=50)
s8 = Frame(frame9,bg="white",width=100,height=50)

s1.grid(row=1,column=1,columnspan=1)
s2.grid(row=1,column=2,columnspan=1)
s3.grid(row=1,column=3,columnspan=1)
s4.grid(row=1,column=4,columnspan=1)
s5.grid(row=1,column=5,columnspan=1)
s6.grid(row=1,column=6,columnspan=1)
s7.grid(row=1,column=7,columnspan=1)
s8.grid(row=1,column=8,columnspan=1)

s1.pack_propagate(0)
s2.pack_propagate(0)
s3.pack_propagate(0)
s4.pack_propagate(0)
s5.pack_propagate(0)
s6.pack_propagate(0)
s7.pack_propagate(0)
s8.pack_propagate(0)


sl1=Label(s1,text="  Saturday",fg="grey",bg="black")
sl1.pack(side=LEFT)

se1=Entry(s2,insertwidth=3)
se1.pack(side=RIGHT,expand=YES,fill=Y)
se2=Entry(s3,insertwidth=3)
se2.pack(side=RIGHT,expand=YES,fill=Y)
se3=Entry(s4,insertwidth=3)
se3.pack(side=RIGHT,expand=YES,fill=Y)
se4=Entry(s5,insertwidth=3)
se4.pack(side=RIGHT,expand=YES,fill=Y)
se5=Entry(s6,insertwidth=3)
se5.pack(side=RIGHT,expand=YES,fill=Y)
se6=Entry(s7,insertwidth=3)
se6.pack(side=RIGHT,expand=YES,fill=Y)
se7=Entry(s8,insertwidth=3)
se7.pack(side=RIGHT,expand=YES,fill=Y)

#-------------------------------------------------------------------------------------------


#-----------------------------Buttons-------------------------------------------------------

bf1 = Frame(frame12,bg="black",width=100,height=50)
bf2 = Frame(frame12,bg="black",width=100,height=50)
bf3 = Frame(frame12,bg="black",width=100,height=50)
bf4 = Frame(frame12,bg="black",width=100,height=50)
bf5 = Frame(frame12,bg="black",width=100,height=50)
bf6 = Frame(frame12,bg="black",width=100,height=50)
bf7 = Frame(frame12,bg="black",width=100,height=50)
bf8 = Frame(frame12,bg="black",width=100,height=50)

bf1.grid(row=1,column=1,columnspan=1)
bf2.grid(row=1,column=2,columnspan=1)
bf3.grid(row=1,column=3,columnspan=1)
bf4.grid(row=1,column=4,columnspan=1)
bf5.grid(row=1,column=5,columnspan=1)
bf6.grid(row=1,column=6,columnspan=1)
bf7.grid(row=1,column=7,columnspan=1)
bf8.grid(row=1,column=8,columnspan=1)

bf1.pack_propagate(0)
bf2.pack_propagate(0)
bf3.pack_propagate(0)
bf4.pack_propagate(0)
bf5.pack_propagate(0)
bf6.pack_propagate(0)
bf7.pack_propagate(0)
bf8.pack_propagate(0)


butt1=Button(bf7,text="Save",font=("Arial",10,"bold"),width=8,height=4,bg='grey',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
butt2=Button(bf8,text="Edit",font=("Arial",10,"bold"),width=8,height=4,bg='grey',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')

butt1.pack(side=LEFT)
butt2.pack(side=LEFT)

#-------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------


def close():
    tim.destroy()

c=Button(frame1
         ,text="X",bg='red',fg='white',state='normal',relief='flat',activebackground='black',command=close,borderwidth=0,highlightbackground='black')
c.pack(side=RIGHT)

tim.mainloop()
