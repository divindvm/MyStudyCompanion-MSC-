from Tkinter import *

cal=Tk()
cal.title("Calculator")
operator=" "
text_Input =StringVar()

txtDisplay =Entry(cal,font=('arial',20,'bold'),textvariable=text_Input, bd=30 ,insertwidth=4,
		  bg="powder blue",justify='right').grid(columnspan=4)

cal.mainloop()
