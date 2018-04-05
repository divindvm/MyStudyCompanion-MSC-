from Tkinter import *
import time
from datetime import date
import datetime
my_date = date.today()
u=my_date.weekday()
now = datetime.datetime.now()

if u==0:
    dname="Sunday"
elif u==1:
    dname="Monday"
elif u==2:
    dname="Tuesday"
elif u==3:
    dname="Wednesday"
elif u==4:
    dname="Thursday"
elif u==5:
    dname="Friday"
else:
    dname="Saturday"
day=now.day
year=now.year
i=now.month
if i==1:
    m="January"
elif i==2:
    m="February"
elif i==3:
    m="March"
elif i==4:
    m="April"
elif i==5:
    m="May"
elif i==6:
    m="June"
elif i==7:
    m="July"
elif i==8:
    m="August"
elif i==9:
    m="September"
elif i==10:
    m="October"
elif i==11:
    m="November"
else:
    m="December"



root = Tk()

root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
root.config(background="black")


main_frame= Frame(root)
main_frame.grid(row=0)




frame1 = Frame(main_frame,bg="black",width=800,height=50)
frame2 = Frame(main_frame,bg="black",width=800,height=50)
frame3 = Frame(main_frame,bg="black",width=800,height=20)
frame4 = Frame(main_frame,bg="black",width=800,height=200)
frame5 = Frame(main_frame,bg="black",width=800,height=20)
frame6 = Frame(main_frame,bg="black",width=800,height=90)
#frame7 = Frame(main_frame,bg="blue",width=800,height=30)


frame1.pack_propagate(0)
frame2.pack_propagate(0)
frame3.pack_propagate(0)
frame4.pack_propagate(0)
frame5.pack_propagate(0)
frame6.pack_propagate(0)
#frame7.pack_propagate(0)



frame1.grid(row=1,column=1,columnspan=5)
frame2.grid(row=2,column=1,columnspan=5)
frame3.grid(row=3,column=1,columnspan=5)
frame4.grid(row=4,column=1,columnspan=5)
frame5.grid(row=5,column=1,columnspan=5)
frame6.grid(row=6,column=1,columnspan=5)
#frame7.grid(row=6,column=1,columnspan=5)




frame8 = Frame(frame6,bg="black",width=300,height=90)
frame9 = Frame(frame6,bg="black",width=200,height=90)
frame10 = Frame(frame6,bg="black",width=300,height=90)


frame8.pack_propagate(0)
frame9.pack_propagate(0)
frame10.pack_propagate(0)



frame8.grid(row=1,column=1)
frame9.grid(row=1,column=2)
frame10.grid(row=1,column=3)




l1 = Label(frame8, font=('gothic', 20, 'bold'), bg='black',fg='gray',text=""+dname)
l1.pack()


l2 = Label(frame10, font=('gothic', 20, 'bold'), bg='black',fg='gray',text=str(day)+"-"+m+"-"+str(year))
l2.pack()

#l3 = Label(frame10, font=('gothic', 45, 'bold'), bg='black',fg='gray',text=m)
#l3.pack()

#l4 = Label(frame11, font=('gothic', 40, 'bold'), bg='black',fg='gray',text="- "+str(year))
#l4.pack(side=LEFT)




time1 = ''
clock = Label(frame4, font=('times', 140, 'bold'), bg='black',fg='snow2')
clock.pack(fill=BOTH, expand=1)



def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
    
def close():
    root.destroy()

c=Button(frame1
         ,text="X",bg='red',fg='white',state='normal',relief='flat',activebackground='black',command=close,borderwidth=0,highlightbackground='black')
c.pack(side=RIGHT)

root.mainloop(  )
