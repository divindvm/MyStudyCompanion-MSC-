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


mv1=StringVar()
mv2=StringVar()
mv3=StringVar()
mv4=StringVar()
mv5=StringVar()
mv6=StringVar()
mv7=StringVar()

me1=Entry(m2,insertwidth=3,textvariable=mv1)
me1.pack(side=RIGHT,expand=YES,fill=Y)
me2=Entry(m3,insertwidth=3,textvariable=mv2)
me2.pack(side=RIGHT,expand=YES,fill=Y)
me3=Entry(m4,insertwidth=3,textvariable=mv3)
me3.pack(side=RIGHT,expand=YES,fill=Y)
me4=Entry(m5,insertwidth=3,textvariable=mv4)
me4.pack(side=RIGHT,expand=YES,fill=Y)
me5=Entry(m6,insertwidth=3,textvariable=mv5)
me5.pack(side=RIGHT,expand=YES,fill=Y)
me6=Entry(m7,insertwidth=3,textvariable=mv6)
me6.pack(side=RIGHT,expand=YES,fill=Y)
me7=Entry(m8,insertwidth=3,textvariable=mv7)
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

tv1=StringVar()
tv2=StringVar()
tv3=StringVar()
tv4=StringVar()
tv5=StringVar()
tv6=StringVar()
tv7=StringVar()

te1=Entry(t2,insertwidth=3,textvariable=tv1)
te1.pack(side=RIGHT,expand=YES,fill=Y)
te2=Entry(t3,insertwidth=3,textvariable=tv2)
te2.pack(side=RIGHT,expand=YES,fill=Y)
te3=Entry(t4,insertwidth=3,textvariable=tv3)
te3.pack(side=RIGHT,expand=YES,fill=Y)
te4=Entry(t5,insertwidth=3,textvariable=tv4)
te4.pack(side=RIGHT,expand=YES,fill=Y)
te5=Entry(t6,insertwidth=3,textvariable=tv5)
te5.pack(side=RIGHT,expand=YES,fill=Y)
te6=Entry(t7,insertwidth=3,textvariable=tv6)
te6.pack(side=RIGHT,expand=YES,fill=Y)
te7=Entry(t8,insertwidth=3,textvariable=tv7)
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

wv1=StringVar()
wv2=StringVar()
wv3=StringVar()
wv4=StringVar()
wv5=StringVar()
wv6=StringVar()
wv7=StringVar()

we1=Entry(w2,insertwidth=3,textvariable=wv1)
we1.pack(side=RIGHT,expand=YES,fill=Y)
we2=Entry(w3,insertwidth=3,textvariable=wv2)
we2.pack(side=RIGHT,expand=YES,fill=Y)
we3=Entry(w4,insertwidth=3,textvariable=wv3)
we3.pack(side=RIGHT,expand=YES,fill=Y)
we4=Entry(w5,insertwidth=3,textvariable=wv4)
we4.pack(side=RIGHT,expand=YES,fill=Y)
we5=Entry(w6,insertwidth=3,textvariable=wv5)
we5.pack(side=RIGHT,expand=YES,fill=Y)
we6=Entry(w7,insertwidth=3,textvariable=wv6)
we6.pack(side=RIGHT,expand=YES,fill=Y)
we7=Entry(w8,insertwidth=3,textvariable=wv7)
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

thv1=StringVar()
thv2=StringVar()
thv3=StringVar()
thv4=StringVar()
thv5=StringVar()
thv6=StringVar()
thv7=StringVar()

the1=Entry(th2,insertwidth=3,textvariable=thv1)
the1.pack(side=RIGHT,expand=YES,fill=Y)
the2=Entry(th3,insertwidth=3,textvariable=thv2)
the2.pack(side=RIGHT,expand=YES,fill=Y)
the3=Entry(th4,insertwidth=3,textvariable=thv3)
the3.pack(side=RIGHT,expand=YES,fill=Y)
the4=Entry(th5,insertwidth=3,textvariable=thv4)
the4.pack(side=RIGHT,expand=YES,fill=Y)
the5=Entry(th6,insertwidth=3,textvariable=thv5)
the5.pack(side=RIGHT,expand=YES,fill=Y)
the6=Entry(th7,insertwidth=3,textvariable=thv6)
the6.pack(side=RIGHT,expand=YES,fill=Y)
the7=Entry(th8,insertwidth=3,textvariable=thv7)
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

fv1=StringVar()
fv2=StringVar()
fv3=StringVar()
fv4=StringVar()
fv5=StringVar()
fv6=StringVar()
fv7=StringVar()

fe1=Entry(f2,insertwidth=3,textvariable=fv1)
fe1.pack(side=RIGHT,expand=YES,fill=Y)
fe2=Entry(f3,insertwidth=3,textvariable=fv2)
fe2.pack(side=RIGHT,expand=YES,fill=Y)
fe3=Entry(f4,insertwidth=3,textvariable=fv3)
fe3.pack(side=RIGHT,expand=YES,fill=Y)
fe4=Entry(f5,insertwidth=3,textvariable=fv4)
fe4.pack(side=RIGHT,expand=YES,fill=Y)
fe5=Entry(f6,insertwidth=3,textvariable=fv5)
fe5.pack(side=RIGHT,expand=YES,fill=Y)
fe6=Entry(f7,insertwidth=3,textvariable=fv6)
fe6.pack(side=RIGHT,expand=YES,fill=Y)
fe7=Entry(f8,insertwidth=3,textvariable=fv7)
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

sv1=StringVar()
sv2=StringVar()
sv3=StringVar()
sv4=StringVar()
sv5=StringVar()
sv6=StringVar()
sv7=StringVar()

se1=Entry(s2,insertwidth=3,textvariable=sv1)
se1.pack(side=RIGHT,expand=YES,fill=Y)
se2=Entry(s3,insertwidth=3,textvariable=sv2)
se2.pack(side=RIGHT,expand=YES,fill=Y)
se3=Entry(s4,insertwidth=3,textvariable=sv3)
se3.pack(side=RIGHT,expand=YES,fill=Y)
se4=Entry(s5,insertwidth=3,textvariable=sv4)
se4.pack(side=RIGHT,expand=YES,fill=Y)
se5=Entry(s6,insertwidth=3,textvariable=sv5)
se5.pack(side=RIGHT,expand=YES,fill=Y)
se6=Entry(s7,insertwidth=3,textvariable=sv6)
se6.pack(side=RIGHT,expand=YES,fill=Y)
se7=Entry(s8,insertwidth=3,textvariable=sv7)
se7.pack(side=RIGHT,expand=YES,fill=Y)

#-------------------------------------------------------------------------------------------


#------------------------------filemanagement--------------------------------------------------



timefile = "timefile.txt"
table=list()
with open(timefile) as f1:
	for  line in f1:
		row=line.split(",")
		table.append(row)
	mv1.set(table[0][0])
	mv2.set(table[0][1])
	mv3.set(table[0][2])
	mv4.set(table[0][3])
	mv5.set(table[0][4])
	mv6.set(table[0][5])
	mv7.set(table[0][6])

	tv1.set(table[1][0])
	tv2.set(table[1][1])
	tv3.set(table[1][2])
	tv4.set(table[1][3])
	tv5.set(table[1][4])
	tv6.set(table[1][5])
	tv7.set(table[1][6])


	wv1.set(table[2][0])
	wv2.set(table[2][1])
	wv3.set(table[2][2])
	wv4.set(table[2][3])
	wv5.set(table[2][4])
	wv6.set(table[2][5])
	wv7.set(table[2][6])

	thv1.set(table[3][0])
	thv2.set(table[3][1])
	thv3.set(table[3][2])
	thv4.set(table[3][3])
	thv5.set(table[3][4])
	thv6.set(table[3][5])
	thv7.set(table[3][6])

	fv1.set(table[4][0])
	fv2.set(table[4][1])
	fv3.set(table[4][2])
	fv4.set(table[4][3])
	fv5.set(table[4][4])
	fv6.set(table[4][5])
	fv7.set(table[4][6])

	sv1.set(table[5][0])
	sv2.set(table[5][1])
	sv3.set(table[5][2])
	sv4.set(table[5][3])
	sv5.set(table[5][4])
	sv6.set(table[5][5])
	sv7.set(table[5][6])
def save():
        butt1.pack_forget()
        timefile2 = "timefile.txt"
        with open(timefile2,'w') as f2:
        #        for t in table:
                        f2.write(mv1.get()+","+mv2.get()+","+mv3.get()+","+mv4.get()+","+mv5.get()+","+mv6.get()+","+mv7.get()+","+","+"\n")
                        f2.write(tv1.get()+","+tv2.get()+","+tv3.get()+","+tv4.get()+","+tv5.get()+","+tv6.get()+","+tv7.get()+","+","+"\n")
                        f2.write(wv1.get()+","+wv2.get()+","+wv3.get()+","+wv4.get()+","+wv5.get()+","+wv6.get()+","+wv7.get()+","+","+"\n")
                        f2.write(thv1.get()+","+thv2.get()+","+thv3.get()+","+thv4.get()+","+thv5.get()+","+thv6.get()+","+thv7.get()+","+","+"\n")
                        f2.write(fv1.get()+","+fv2.get()+","+fv3.get()+","+fv4.get()+","+fv5.get()+","+fv6.get()+","+fv7.get()+","+","+"\n")
                        f2.write(sv1.get()+","+sv2.get()+","+sv3.get()+","+sv4.get()+","+sv5.get()+","+sv6.get()+","+sv7.get()+","+","+"\n")


        savelabel.after(1000,lambda:savelabel.config(text="  Data Saved !"))   
        savelabel.after(5000,lambda:savelabel.config(text=""))                
def edit():
        butt1.pack(side=LEFT)

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


butt1=Button(bf7,text="Save",command=save,font=("Arial",10,"bold"),width=8,height=4,bg='grey',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
butt2=Button(bf8,text="Edit",command=edit,font=("Arial",10,"bold"),width=8,height=4,bg='grey',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')

butt1.pack_forget()
butt2.pack(side=LEFT)

savelabel=Label(bf1,text=" ",bg="black",fg="white")
savelabel.pack(side=LEFT)

#-------------------------------------------------------------------------------------------





def close():
    tim.destroy()

c=Button(frame1
         ,text="X",bg='red',fg='white',state='normal',relief='flat',activebackground='black',command=close,borderwidth=0,highlightbackground='black')
c.pack(side=RIGHT)

tim.mainloop()
