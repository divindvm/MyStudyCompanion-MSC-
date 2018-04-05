from Tkinter import *
from PIL import ImageTk, Image
import os
import time

root=Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())


img1= PhotoImage(file="senser.gif",format="gif -index 0")
img2= PhotoImage(file="senser.gif",format="gif -index 1")



main_frame= Frame(root)
main_frame.grid(row=0)
frame1 = Frame(main_frame,bg="black",width=800,height=480)
frame1.pack_propagate(0)
frame1.grid(row=1,column=1,columnspan=5)


l3=Button(frame1,bg='red',image=img1,fg='Grey',state='normal',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
l3.pack()



#root.config(image=img1)
#root.configure(background='black')

def scanning():
    if True:
    
        l3.after(1000,lambda:l3.config(image=img2))
        l3.after(1000,lambda:l3.config(image=img1))
        l3.after(1000,lambda:l3.config(image=img2))
        l3.after(1000,lambda:l3.config(image=img1))

    root.after(1000, scanning)

root.after(1000, scanning)
root.mainloop()
