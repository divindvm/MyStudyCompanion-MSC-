from Tkinter import *
from PIL import ImageTk, Image
import os
import time

root=Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())



t = Toplevel(root)
t.overrideredirect(True)
t.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
t.focus_set()
t.bind("<Escape>", lambda e: e.widget.quit())
def closecalc():
                t.destroy()
#t.attributes("-fullscreen",1)
main_frame= Frame(t)
main_frame.grid(row=0)
frame1 = Frame(main_frame,bg="black",width=800,height=40)
frame2 = Frame(main_frame,bg="white",width=800,height=80)


frame1.grid(row=1,column=1,columnspan=5)
frame2.grid(row=2,column=1,columnspan=5)

frame1.pack_propagate(0)
frame2.pack_propagate(0)






operator=""
text_Input =StringVar()

txtDisplay =Entry(frame2,font=('arial',20,'bold'),textvariable=text_Input, bd=7 ,insertwidth=8,
                                bg="white",justify='right').pack(side=LEFT,expand=YES,fill=BOTH)




root.mainloop()
