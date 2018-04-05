from Tkinter import *


def nextwin():
        tim = Toplevel(root)
        tim.overrideredirect(True)
        tim.geometry("{0}x{1}+0+0".format(tim.winfo_screenwidth(),tim.winfo_screenheight()))
        tim.focus_set()
        tim.bind("<Escape>", lambda e: e.widget.quit())
        en=Entry(tim)
        en.pack()
        b=Button(tim,text="Exit",command=close)
        b.pack()
        def close():
                        tim.destroy()

root=Tk()
butt=Button(root,text="next window",command=nextwin)
butt.pack()
root.mainloop()

