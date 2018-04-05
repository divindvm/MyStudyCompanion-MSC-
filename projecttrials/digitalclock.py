from Tkinter import *
import time
from datetime import date
import datetime
my_date = date.today()
uu=my_date.weekday()
now = datetime.datetime.now()
root = Tk()
time1 = ''
clock = Label(root, font=('times', 150, 'bold'), bg='green')
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
print(uu)


print "Current date and time using str method of datetime object:"
print str(now)

print
print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day

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
    
print(m)
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond



root.mainloop(  )
