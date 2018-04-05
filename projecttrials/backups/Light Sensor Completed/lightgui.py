from Tkinter import *
from PIL import ImageTk, Image
import os
import time
import RPi.GPIO as GPIO
led1=0
led2=0
var=0
running=False
GPIO.setmode(GPIO.BOARD)
pin_to_circuit= 31
#GPIO.cleanup()
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setwarnings(False)


    
def scanning():
    
    if running:
        
        GPIO.setmode(GPIO.BOARD)
        pin_to_circuit= 31
        GPIO.setup(32,GPIO.OUT)
        GPIO.setup(36,GPIO.OUT)
        
        def rc_time(pin_to_circuit):
                count=0

                GPIO.setup(pin_to_circuit,GPIO.OUT)
                GPIO.output(pin_to_circuit,GPIO.LOW)
                time.sleep(0.1)
	
                GPIO.setup(pin_to_circuit,GPIO.IN)
	
                while(GPIO.input(pin_to_circuit)==GPIO.LOW):
                        count+=1
                return count

        try:
               
                if running:
                        #print rc_time(pin_to_circuit)
                        value= rc_time(pin_to_circuit)
                        val=str(value)
                        label1.config(text="Sensor Reading = "+val)
                        global var
                        if (var==0):
                            l3.config(image=img4)
                            var=1
                        else:
                            l3.config(image=img3)
                            var=0
                            
                        l4.config(text="Automatic Light Sensing ON")
                        
                        if(value>16000):
                                GPIO.output(32, GPIO.HIGH)
                                GPIO.output(36, GPIO.HIGH)
                                l1.config(image=img1)
                                l2.config(image=img1)

                        if(value<7800):
                                GPIO.output(32, GPIO.LOW)
                                GPIO.output(36, GPIO.LOW)
                                l1.config(image=img2)
                                l2.config(image=img2)
			
        except KeyboardInterrupt:
                pass
        #finally:
               #GPIO.cleanup()
    root.after(1000, scanning)

def start():
    global running
    running = True

def stop():
    global running
    running = False
    label1.config(text="Sensor Turned OFF")
    l4.config(text="Turn On Light Sensor")


#light=Tk()
#operator=" "
#light.attributes("-fullscreen",1)

root=Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

GPIO.output(32, GPIO.LOW)
GPIO.output(36, GPIO.LOW)

img1= PhotoImage(file="lighton.gif",format="gif -index 0")
img2= PhotoImage(file="lightoff.gif",format="gif -index 0")
img3= PhotoImage(file="senser.gif",format="gif -index 0")
img4= PhotoImage(file="senser.gif",format="gif -index 1")
img5= PhotoImage(file="senser.gif",format="gif -index 0")
#img5= PhotoImage(file="sens.jpg",format="jpeg")

main_frame= Frame(root)
main_frame.grid(row=0)




frame1 = Frame(main_frame,bg="black",width=800,height=30)
frame2 = Frame(main_frame,bg="grey",width=800,height=20)
frame3 = Frame(main_frame,bg="black",width=800,height=50)
frame4 = Frame(main_frame,bg="black",width=800,height=150)
frame5 = Frame(main_frame,bg="black",width=800,height=180)
frame6 = Frame(main_frame,bg="black",width=800,height=50)

frame1.pack_propagate(0)
frame2.pack_propagate(0)
frame3.pack_propagate(0)
frame4.pack_propagate(0)
frame5.pack_propagate(0)
frame6.pack_propagate(0)



frame1.grid(row=1,column=1,columnspan=5)
frame2.grid(row=2,column=1,columnspan=5)
frame3.grid(row=3,column=1,columnspan=5)
frame4.grid(row=4,column=1,columnspan=5)
frame5.grid(row=5,column=1,columnspan=5)
frame6.grid(row=6,column=1,columnspan=5)




frame7 = Frame(frame4,bg="blue",width=250,height=150)
frame8 = Frame(frame4,bg="black",width=300,height=150)
frame9 = Frame(frame4,bg="yellow",width=250,height=150)


frame7.grid(row=1,column=1)
frame8.grid(row=1,column=2)
frame9.grid(row=1,column=3)

frame10 = Frame(frame5,bg="black",width=250,height=180)
frame11 = Frame(frame5,bg="grey",width=300,height=180)
frame12 = Frame(frame5,bg="black",width=250,height=180)

frame10.grid(row=1,column=1)
frame11.grid(row=1,column=2)
frame12.grid(row=1,column=3)


frame7.pack_propagate(0)
frame8.pack_propagate(0)
frame9.pack_propagate(0)
frame10.pack_propagate(0)
frame11.pack_propagate(0)
frame12.pack_propagate(0)

led1lab=Label(frame10,text="                      LED 1 OFF",fg="grey",bg="black")
led2lab=Label(frame12,text="LED 2 OFF                      ",fg="grey",bg="black")
led1lab.pack(side=LEFT)
led2lab.pack(side=RIGHT)


def led1switch():
    global led1
    if(led1==0):
        led1=1
        l1.config(image=img1)
        led1lab.config(text="                      LED 1 ON",fg="White")
        GPIO.output(36, GPIO.HIGH)
        
    else:
        l1.config(image=img2)
        led1=0
        led1lab.config(text="                      LED 1 OFF",fg="grey")
        GPIO.output(36, GPIO.LOW)

def led2switch():
    global led2
    if(led2==0):
        l2.config(image=img1)
        led2=1
        led2lab.config(text="LED 2 ON                      ",fg="white")
        GPIO.output(32, GPIO.HIGH)
    else:
        l2.config(image=img2)
        led2=0
        led2lab.config(text="LED 2 OFF                      ",fg="grey")
        GPIO.output(32, GPIO.LOW)



l1=Button(frame7,bg='black',command=led1switch,fg='black',image=img1,state='normal',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
l1.pack()
l1.config(image=img2)


l2=Button(frame9,bg='black',command=led2switch,fg='black',image=img1,state='normal',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
l2.pack()
l2.config(image=img2)


l3=Button(frame11,bg='black',image=img4,command=stop,fg='Grey',state='normal',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
l3.pack()
#l3.config(image=img5)

l4=Button(frame6,bg='black',text="Turn On Light Sensor",command=start,fg='Grey',state='normal',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
l4.pack()

label1=Label(frame8,text="Sensor Turned OFF",bg="black",fg="grey")
label1.pack()

label2=Label(frame2,text="MSC LIGHTS",bg="grey",fg="White",font="Ariel 15")
label2.pack()

def close():
    root.destroy()

c=Button(frame1
         ,text="X",bg='red',fg='white',state='normal',relief='flat',activebackground='black',command=close,borderwidth=0,highlightbackground='black')
c.pack(side=RIGHT)

root.after(1000, scanning)
root.mainloop()


