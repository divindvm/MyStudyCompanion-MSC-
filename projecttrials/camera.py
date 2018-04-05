from picamera import PiCamera
from time import sleep
from Tkinter import *
from PIL import ImageTk, Image
import os
import time
import RPi.GPIO as GPIO
from PIL import ImageTk,Image



img = ImageTk.PhotoImage(Image.open('/home/pi/Desktop/image.jpg'))
def click():
    
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/projecttrials/image.jpg')
    camera.stop_preview()
def exiting():
    root.destroy()

root=Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

butt=Button(root,text="Click",command=click)
butt.pack()
butt=Button(root,text="Exit",command=exiting)
butt.pack()


root.mainloop()
