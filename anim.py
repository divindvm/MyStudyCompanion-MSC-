from Tkinter import *
from PIL import ImageTk, Image
import os
import time
from creds import *
import RPi.GPIO as GPIO

running = True
operator=""

led1=0
led2=0
var=0
alexavar=0
ale=True
runningg=False
def eye():
        b.config(image=img1)
	root.configure(background='black')
	b.after(100,lambda:b.config(image=img2))
	c.config(image=img1)
        root.configure(background='black')
        c.after(100,lambda:c.config(image=img2))

	b.config(image=img2)
	root.configure(background='black')
	b.after(150,lambda:b.config(image=img3))
	c.config(image=img1)
        root.configure(background='black')
        c.after(100,lambda:c.config(image=img3))


	b.config(image=img3)
	root.configure(background='black')
	b.after(150,lambda:b.config(image=img4))
	c.config(image=img1)
        root.configure(background='black')
        c.after(150,lambda:c.config(image=img4))


	b.config(image=img4)
	root.configure(background='black')
	b.after(200,lambda:b.config(image=img5))
	c.config(image=img1)
        root.configure(background='black')
        c.after(200,lambda:c.config(image=img5))


	b.config(image=img5)
        root.configure(background='black')
        b.after(200,lambda:b.config(image=img6))
	c.config(image=img1)
        root.configure(background='black')
        c.after(200,lambda:c.config(image=img6))


        b.config(image=img6)
        root.configure(background='black')
        b.after(250,lambda:b.config(image=img7))
	c.config(image=img1)
        root.configure(background='black')
        c.after(250,lambda:c.config(image=img7))


        b.config(image=img7)
        root.configure(background='black')
        b.after(250,lambda:b.config(image=img8))
	c.config(image=img1)
        root.configure(background='black')
        c.after(250,lambda:c.config(image=img8))


	b.config(image=img8)
        root.configure(background='black')
        b.after(300,lambda:b.config(image=img9))
	c.config(image=img1)
        root.configure(background='black')
        c.after(300,lambda:c.config(image=img9))


        b.config(image=img9)
        root.configure(background='black')
        b.after(300,lambda:b.config(image=img10))
	c.config(image=img9)
        root.configure(background='black')
        c.after(300,lambda:c.config(image=img10))


        b.config(image=img10)
        root.configure(background='black')
        b.after(350,lambda:b.config(image=img11))
	c.config(image=img10)
        root.configure(background='black')
        c.after(350,lambda:c.config(image=img11))


        b.config(image=img11)
        root.configure(background='black')
        b.after(350,lambda:b.config(image=img12))
	c.config(image=img11)
        root.configure(background='black')
        c.after(350,lambda:c.config(image=img12))

        b.config(image=img12)
        root.configure(background='black')
        b.after(400,lambda:b.config(image=img13))
	c.config(image=img12)
        root.configure(background='black')
        c.after(400,lambda:c.config(image=img13))

        b.config(image=img13)
        root.configure(background='black')
        b.after(400,lambda:b.config(image=img14))
	c.config(image=img13)
        root.configure(background='black')
        c.after(400,lambda:c.config(image=img14))

        b.config(image=img14)
        root.configure(background='black')
        b.after(450,lambda:b.config(image=img15))
	c.config(image=img14)
        root.configure(background='black')
        c.after(450,lambda:c.config(image=img15))

	b.config(image=img15)
        root.configure(background='black')
        b.after(450,lambda:b.config(image=img16))
	c.config(image=img15)
        root.configure(background='black')
        c.after(450,lambda:c.config(image=img16))


        b.config(image=img16)
	root.configure(background='black')
        b.after(500,lambda:b.config(image=img1))
	c.config(image=img16)
        root.configure(background='black')
        c.after(500,lambda:c.config(image=img1))

#---------------------------------------------Alexa----------------------------------------------




def alexastart():
        from PIL import ImageTk, Image
        al = Toplevel(root)
        al.overrideredirect(True)
        al.geometry("{0}x{1}+0+0".format(al.winfo_screenwidth(),al.winfo_screenheight()))
        al.focus_set()
        al.bind("<Escape>", lambda e: e.widget.quit())
        def close():
                al.destroy()
        al.attributes("-fullscreen",1)

        main_frame= Frame(al)
        main_frame.grid(row=0)


        frame1 = Frame(main_frame,width=800,height=480)
        frame1.pack_propagate(0)
        frame1.grid(row=1,column=1)

       
        def alexavoice():
                import os
                import random
                import time
                import RPi.GPIO as GPIO
                import alsaaudio
                import wave
                import random
                import requests
                import json
                import re
                from memcache import Client
                from PIL import ImageTk, Image
                

	
                #Settings
                button = 21 #GPIO for button
                lights = [13, 19] # GPIO Pins for red and green LED
                device = "plughw:1" # Name of mic/soundcard in arecord -L 

                #Setup
                recorded = False
                servers = ["127.0.0.1:11211"]
                mc = Client(servers, debug=1)
                path = os.path.realpath(__file__).rstrip(os.path.basename(__file__))

                def internet_on():
                        print "Checking Internet Connection"
                        try:
                        	r =requests.get('https://api.amazon.com/auth/o2/token')
    
                        	print "Connection OK"
                        	for x in range(0, 2):
                                        time.sleep(.2)
                                        GPIO.output(19, GPIO.HIGH)
                                        GPIO.output(13, GPIO.HIGH)
                                        time.sleep(.2)
                                        GPIO.output(lights, GPIO.LOW)
        		
                                return True
                        except:
                                print "Connection Failed"
                                return False
	
                def gettoken():
                        token = mc.get("access_token")
                        refresh = refresh_token
                        if token:
                        	return token
                        elif refresh:
                                payload = {"client_id" : Client_ID, "client_secret" : Client_Secret, "refresh_token" : refresh, "grant_type" : "refresh_token", }

                                url = "https://api.amazon.com/auth/o2/token"
                                r = requests.post(url, data = payload)
                                resp = json.loads(r.text)
                                mc.set("access_token", resp['access_token'], 3570)
                                return resp['access_token']

                        else:
                                return False

                        


                def alexa():
                        #GPIO.output(13, GPIO.HIGH)
                        #imgg2= PhotoImage(file="think.gif",format="gif -index 1")
                        #al1.config(image=imgg2)
                        url = 'https://access-alexa-na.amazon.com/v1/avs/speechrecognizer/recognize'
                        headers = {'Authorization' : 'Bearer %s' % gettoken()}
                        d = {
                                "messageHeader": {
                                "deviceContext": [
                                        {
                                        "name": "playbackState",
                                        "namespace": "AudioPlayer",
                                        "payload": {
                                                "streamId": "",
                                                	"offsetInMilliseconds": "0",
                                                "playerActivity": "IDLE"
                                        }
                                        }
                                ]
                                },
                                "messageBody": {
                                "profile": "alexa-close-talk",
                                "locale": "en-us",
                                "format": "audio/L16; rate=16000; channels=1"
                                }
                        }
                        with open(path+'recording.wav') as inf:
                                files = [
                                        	('file', ('request', json.dumps(d), 'application/json; charset=UTUTF-8')),
                                        	('file', ('audio', inf, 'audio/L16; rate=16000; channels=1'))
                                        	]
                                r = requests.post(url, headers=headers, files=files)
                        if r.status_code == 200:
                                for v in r.headers['content-type'].split(";"):
                                        if re.match('.*boundary.*', v):
                                        	boundary =  v.split("=")[1]
                        	data = r.content.split(boundary)
                        	for d in data:
                                        if (len(d) >= 1024):
                                        	audio = d.split('\r\n\r\n')[1].rstrip('--')
                                with open(path+"response.mp3", 'wb') as f:
                                        f.write(audio)
                                        GPIO.output(19, GPIO.HIGH)
                                GPIO.output(19, GPIO.LOW)
                                GPIO.output(13, GPIO.HIGH)
                                os.system('mpg123 -q {}1sec.mp3 {}response.mp3'.format(path, path))
                                GPIO.output(13, GPIO.LOW)
                        else:
                                GPIO.output(lights, GPIO.LOW)
                                for x in range(0, 3):
                                        time.sleep(.2)
                                        GPIO.output(19, GPIO.HIGH)
                                        time.sleep(.2)
                                        GPIO.output(lights, GPIO.LOW)
                       

		
                def start():
                        last = GPIO.input(button)
 
                        while True:
                                val = GPIO.input(button)
                                #GPIO.output(19, GPIO.HIGH)
                                if val != last:
                                        last = val
                                        if val == 1 and recorded == True:
                                                rf = open(path+'recording.wav', 'w')
                                                rf.write(audio)
                                                rf.close()
                                                inp = None
                                                alexa()
                                        elif val == 0:
                                                GPIO.output(19, GPIO.HIGH)
                                                inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NORMAL, device)

                                                inp.setchannels(1)
                                                inp.setrate(16000)
                                                inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
                                                inp.setperiodsize(500)
                                                audio = ""
                                                l, data = inp.read()
                                                if l:
                                                        audio += data
                                                recorded = True
                                                #GPIO.output(13, GPIO.LOW)
                                elif val == 0:
                                        l, data = inp.read()
                                        if l:
                                        	audio += data

                
                if __name__ == "__main__":
                
                        GPIO.setwarnings(False)
                        GPIO.cleanup()
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
                        GPIO.setup(lights, GPIO.OUT)
                        GPIO.output(lights, GPIO.LOW)
                        while internet_on() == False:
                                print "."
                        token = gettoken()
                        os.system('mpg123 -q {}1sec.mp3 {}hello.mp3'.format(path, path))
                        for x in range(0, 3):
                                time.sleep(.1)
                                GPIO.output(19, GPIO.HIGH)
                                time.sleep(.1)
                                GPIO.output(19, GPIO.LOW)
                        
                        start()
        def startstop():
                global alexavar
                if (alexavar==0):
                        alexavar=1
                        al1.config(text="stop")
                        alexavoice()
                else:
                        alexavar=0
                        al1.config(text="start")
                        GPIO.cleanup()
                        close()

  
                        

        al1=Button(frame1,bg='black',width=800,height=480,command=startstop,fg='black',image=imgg1,state='normal',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
        al1.pack()
        al1.config(image=imgg2)



        
        #butt=Button(frame1,bg='black',fg='black',image=img2,state='normal',activebackground='black',relief='flat',command=startstop,borderwidth=0,highlightbackground='black')
        #butt=Button(frame1,text="start",command=startstop)
        #butt.pack()
        
        #butt.config(image=img3)





#-----------------------------------------------------------------------------------------------



def blink():
   if running:
	b.config(image=img1)
	root.configure(background='black')
	b.after(100,lambda:b.config(image=img2))
	c.config(image=img1)
        root.configure(background='black')
        c.after(100,lambda:c.config(image=img2))

	b.config(image=img2)
	root.configure(background='black')
	b.after(150,lambda:b.config(image=img3))
	c.config(image=img1)
        root.configure(background='black')
        c.after(100,lambda:c.config(image=img3))


	b.config(image=img3)
	root.configure(background='black')
	b.after(150,lambda:b.config(image=img4))
	c.config(image=img1)
        root.configure(background='black')
        c.after(150,lambda:c.config(image=img4))


	b.config(image=img4)
	root.configure(background='black')
	b.after(200,lambda:b.config(image=img5))
	c.config(image=img1)
        root.configure(background='black')
        c.after(200,lambda:c.config(image=img5))


	b.config(image=img5)
        root.configure(background='black')
        b.after(200,lambda:b.config(image=img6))
	c.config(image=img1)
        root.configure(background='black')
        c.after(200,lambda:c.config(image=img6))


        b.config(image=img6)
        root.configure(background='black')
        b.after(250,lambda:b.config(image=img7))
	c.config(image=img1)
        root.configure(background='black')
        c.after(250,lambda:c.config(image=img7))


        b.config(image=img7)
        root.configure(background='black')
        b.after(250,lambda:b.config(image=img8))
	c.config(image=img1)
        root.configure(background='black')
        c.after(250,lambda:c.config(image=img8))


	b.config(image=img8)
        root.configure(background='black')
        b.after(300,lambda:b.config(image=img9))
	c.config(image=img1)
        root.configure(background='black')
        c.after(300,lambda:c.config(image=img9))


        b.config(image=img9)
        root.configure(background='black')
        b.after(300,lambda:b.config(image=img10))
	c.config(image=img9)
        root.configure(background='black')
        c.after(300,lambda:c.config(image=img10))


        b.config(image=img10)
        root.configure(background='black')
        b.after(350,lambda:b.config(image=img11))
	c.config(image=img10)
        root.configure(background='black')
        c.after(350,lambda:c.config(image=img11))


        b.config(image=img11)
        root.configure(background='black')
        b.after(350,lambda:b.config(image=img12))
	c.config(image=img11)
        root.configure(background='black')
        c.after(350,lambda:c.config(image=img12))

        b.config(image=img12)
        root.configure(background='black')
        b.after(400,lambda:b.config(image=img13))
	c.config(image=img12)
        root.configure(background='black')
        c.after(400,lambda:c.config(image=img13))

        b.config(image=img13)
        root.configure(background='black')
        b.after(400,lambda:b.config(image=img14))
	c.config(image=img13)
        root.configure(background='black')
        c.after(400,lambda:c.config(image=img14))

        b.config(image=img14)
        root.configure(background='black')
        b.after(450,lambda:b.config(image=img15))
	c.config(image=img14)
        root.configure(background='black')
        c.after(450,lambda:c.config(image=img15))

	b.config(image=img15)
        root.configure(background='black')
        b.after(450,lambda:b.config(image=img16))
	c.config(image=img15)
        root.configure(background='black')
        c.after(450,lambda:c.config(image=img16))


        b.config(image=img16)
	root.configure(background='black')
        b.after(500,lambda:b.config(image=img1))
	c.config(image=img16)
        root.configure(background='black')
        c.after(500,lambda:c.config(image=img1))

   root.after(5000,blink)
def start():
	global running
	running=True
	b1.pack_forget()
        b2.pack_forget()
        b3.pack_forget()
        b4.pack_forget()
        b5.pack_forget()
        b6.pack_forget()

def stop():
	global running
	running= False
	b1.pack(side=TOP)
	b2.pack(side=TOP)
	b3.pack(side=TOP)
	b4.pack(side=TOP)
	b5.pack(side=TOP)
	b6.pack(side=TOP)

def close():
	root.destroy()


def calculator():
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
        frame3 = Frame(main_frame,bg="black",width=800,height=90)
        frame4 = Frame(main_frame,bg="white",width=800,height=90)
        frame5 = Frame(main_frame,bg="black",width=800,height=90)
        frame6 = Frame(main_frame,bg="white",width=800,height=90)

        frame1.grid(row=1,column=1,columnspan=5)
        frame2.grid(row=2,column=1,columnspan=5)
        frame3.grid(row=3,column=1,columnspan=5)
        frame4.grid(row=4,column=1,columnspan=5)
        frame5.grid(row=5,column=1,columnspan=5)
        frame6.grid(row=6,column=1,columnspan=5)

        frame1.pack_propagate(0)
        frame2.pack_propagate(0)
        frame3.pack_propagate(0)
        frame4.pack_propagate(0)
        frame5.pack_propagate(0)
        frame6.pack_propagate(0)

        def btnClick(numbers):
                global operator
                operator=operator+str(numbers)
                text_Input.set(operator)

        def btnClearDisplay():
                global operator
                operator=""
                text_Input.set("")

        def btnEqualsInput():
                global operator
                sumup=str(eval(operator))
                text_Input.set(sumup)    
                operator=sumup
        def delete_entries():
                global operator
                temp=text_Input.get()
                temp=temp[:-1]
                operator=str(temp)
                text_Input.set(temp)



        operator=""
        text_Input =StringVar()

        txtDisplay =Entry(frame2,font=('arial',20,'bold'),textvariable=text_Input, bd=7 ,insertwidth=8,
                          bg="white",justify='right').pack(side=LEFT,expand=YES,fill=BOTH)



        l= Label(frame1,text='MSC Calculator',font=("Arial",12,"bold"),bg='black',fg='grey')
        l.pack(side=LEFT)







        def callback():
            print e.get()










        b1=Button(frame3,text="7",command=lambda:btnClick(7),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
        b2=Button(frame3,text="8",command=lambda:btnClick(8),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
        b3=Button(frame3,text="9",command=lambda:btnClick(9),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',borderwidth=0,relief='flat',highlightbackground='grey')
        b4=Button(frame3,text="/",command=lambda:btnClick("/"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
        b5=Button(frame3,text="C",command=delete_entries,font=("Arial",10,"bold"),width=20,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
        b6=Button(frame4,text="4",command=lambda:btnClick(4),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
        b7=Button(frame4,text="5",command=lambda:btnClick(5),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
        b8=Button(frame4,text="6",command=lambda:btnClick(6),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
        b9=Button(frame4,text="x",command=lambda:btnClick("*"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
        b10=Button(frame4,text="AC",command=btnClearDisplay,font=("Arial",10,"bold"),width=20,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')

        b11=Button(frame5,text="1",command=lambda:btnClick(1),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
        b12=Button(frame5,text="2",command=lambda:btnClick(2),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
        b13=Button(frame5,text="3",command=lambda:btnClick(3),font=("Arial",10,"bold"),width=16,height=9,bg='black',fg='white',state='normal',activebackground='grey',relief='flat',borderwidth=0,highlightbackground='grey')
        b14=Button(frame5,text="-",command=lambda:btnClick("-"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
        b15=Button(frame5,text="v",command=lambda:btnClick("**0.5"),font=("Arial",10,"bold"),width=20,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
        b16=Button(frame6,text="0",command=lambda:btnClick(0),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
        b17=Button(frame6,text=".",command=lambda:btnClick("."),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
        b18=Button(frame6,text="%",command=lambda:btnClick("%"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
        b19=Button(frame6,text="+",command=lambda:btnClick("+"),font=("Arial",10,"bold"),width=16,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')
        b20=Button(frame6,text="=",command=btnEqualsInput,font=("Arial",10,"bold"),width=20,height=9,bg='grey',fg='white',state='normal',activebackground='white',relief='flat',borderwidth=0,highlightbackground='black')

        b1.pack(side=LEFT)
        b2.pack(side=LEFT)
        b3.pack(side=LEFT)
        b4.pack(side=LEFT)
        b5.pack(side=LEFT)
        b6.pack(side=LEFT)
        b7.pack(side=LEFT)
        b8.pack(side=LEFT)
        b9.pack(side=LEFT)
        b10.pack(side=LEFT)

        b11.pack(side=LEFT)
        b12.pack(side=LEFT)
        b13.pack(side=LEFT)
        b14.pack(side=LEFT)
        b15.pack(side=LEFT)
        b16.pack(side=LEFT)
        b17.pack(side=LEFT)
        b18.pack(side=LEFT)
        b19.pack(side=LEFT)
        b20.pack(side=LEFT)


        def click(key):
            print key.char


        def close():
            t.destroy()

        c=Button(frame1,text="X",bg='red',fg='white',state='normal',relief='flat',activebackground='black',command=close,borderwidth=0,highlightbackground='black')
        c.pack(side=RIGHT)
        #root1.mainloop()


def timetable():
        
        tim = Toplevel(root)
        tim.overrideredirect(True)
        tim.geometry("{0}x{1}+0+0".format(tim.winfo_screenwidth(),tim.winfo_screenheight()))
        tim.focus_set()
        tim.bind("<Escape>", lambda e: e.widget.quit())
	def closecalc():
                tim.destroy()
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

        me1=Entry(m2,insertwidth=3,textvariable=mv1,state=NORMAL)
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

        me1.focus()



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

        #t.mainloop()



#----------------------------------------------LED Lights-----------------------------------------



def lightcontrol():

        #from Tkinter import *
        from PIL import ImageTk, Image
        import os
        import time
        import RPi.GPIO as GPIO
        #led1=0
        #led2=0
        #var=0
        #running=False
        GPIO.setmode(GPIO.BOARD)
        pin_to_circuit= 31
        #GPIO.cleanup()
        GPIO.setup(32,GPIO.OUT)
        GPIO.setup(36,GPIO.OUT)
        GPIO.setwarnings(False)


    
        def scanning():
    
            if runningg:
        
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
               
                        if runningg:
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
            lig.after(1000, scanning)

        def start():
            global runningg
            runningg = True

        def stop():
            global runningg
            runningg = False
            label1.config(text="Sensor Turned OFF")
            l4.config(text="Turn On Light Sensor")


        #light=Tk()
        #operator=" "
        #light.attributes("-fullscreen",1)

        #root=Tk()
        #root.overrideredirect(True)
        #root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
        #root.focus_set()
        #root.bind("<Escape>", lambda e: e.widget.quit())


        lig = Toplevel(root)
        lig.overrideredirect(True)
        lig.geometry("{0}x{1}+0+0".format(lig.winfo_screenwidth(),lig.winfo_screenheight()))
        lig.focus_set()
        lig.bind("<Escape>", lambda e: e.widget.quit())
	#def closecalc():
                #tim.destroy()
        lig.attributes("-fullscreen",1)
        main_frame= Frame(lig)
        main_frame.grid(row=0)

        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        
        img1= PhotoImage(file="lighton.gif",format="gif -index 0")
        img2= PhotoImage(file="lightoff.gif",format="gif -index 0")
        img3= PhotoImage(file="senser.gif",format="gif -index 0")
        img4= PhotoImage(file="senser.gif",format="gif -index 1")
        img5= PhotoImage(file="senser.gif",format="gif -index 0")
        #img5= PhotoImage(file="sens.jpg",format="jpeg")

        #main_frame= Frame(root)
        #main_frame.grid(row=0)




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
            lig.destroy()
            GPIO.output(36, GPIO.LOW)
            GPIO.output(32, GPIO.LOW)


            

        c=Button(frame1
                 ,text="X",bg='red',fg='white',state='normal',relief='flat',activebackground='black',command=close,borderwidth=0,highlightbackground='black')
        c.pack(side=RIGHT)

        lig.after(1000, scanning)
        #lig.mainloop()




	
root=Tk()
#root.configure(background='black')
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
#top=Frame(root,background='black',height=1000,width=2000)
#bottom=Frame(root,background='black',height=1000,width=2000)
#bottom.pack(fill="both",expand=True,padx=20,pady=20)
#top.place(in_=bottom,anchor="c",relx=0.5,rely=0.5)
img1= PhotoImage(file="round.gif",format="gif -index 0")
img2= PhotoImage(file="round.gif",format="gif -index 0")
img3= PhotoImage(file="round.gif",format="gif -index 1")
img4= PhotoImage(file="round.gif",format="gif -index 1")
img5= PhotoImage(file="round.gif",format="gif -index 2")
img6= PhotoImage(file="round.gif",format="gif -index 2")
img7= PhotoImage(file="round.gif",format="gif -index 3")
img8= PhotoImage(file="round.gif",format="gif -index 3")
img9= PhotoImage(file="round.gif",format="gif -index 4")
img10= PhotoImage(file="round.gif",format="gif -index 4")
img11= PhotoImage(file="round.gif",format="gif -index 5")
img12= PhotoImage(file="round.gif",format="gif -index 5")
img13= PhotoImage(file="round.gif",format="gif -index 6")
img14= PhotoImage(file="round.gif",format="gif -index 6")
img15= PhotoImage(file="round.gif",format="gif -index 7")
img16= PhotoImage(file="round.gif",format="gif -index 7")





imgg1= PhotoImage(file="think.gif",format="gif -index 0")
imgg2= PhotoImage(file="think.gif",format="gif -index 1")

imgg3= PhotoImage(file="think.gif",format="gif -index 2")
imgg4= PhotoImage(file="think.gif",format="gif -index 3")
imgg5= PhotoImage(file="think.gif",format="gif -index 4")
imgg6= PhotoImage(file="think.gif",format="gif -index 5")
imgg7= PhotoImage(file="think.gif",format="gif -index 6")
imgg8= PhotoImage(file="think.gif",format="gif -index 7")
imgg9= PhotoImage(file="senser.gif",format="gif -index 1")

#panel=Label(root, image=img1)
#panel.pack(side="bottom",fill="both",expand="yes")
main_frame= Frame(root)
main_frame.grid(row=3)

frame1 = Frame(main_frame,bg="black",width=800,height=90)
frame2 = Frame(main_frame,bg="black",width=70,height=300)
frame3 = Frame(main_frame,bg="black",width=300,height=300)
frame4 = Frame(main_frame,bg="black",width=60,height=300)
frame5 = Frame(main_frame,bg="black",width=300,height=300)
frame6 = Frame(main_frame,bg="black",width=70,height=300)
frame7 = Frame(main_frame,bg="black",width=800,height=90)

frame1.grid(row=1,column=1,columnspan=5)
frame2.grid(row=2,column=1)
frame3.grid(row=2,column=2)
frame4.grid(row=2,column=3)
frame5.grid(row=2,column=4)
frame6.grid(row=2,column=5)
frame7.grid(row=3,column=1,columnspan=5)
frame3.pack_propagate(0)
frame5.pack_propagate(0)
frame2.pack_propagate(0)
frame6.pack_propagate(0)


b=Button(frame3,bg='black',fg='black',image=img1,state='normal',activebackground='black',relief='flat',command=start,borderwidth=0,highlightbackground='black')
c=Button(frame5,bg='black',fg='black',state='normal',relief='flat',activebackground='black',image=img1,command=stop,borderwidth=0,highlightbackground='black')
#b.config(height=200,width=200)

#b.place(relx=0.5,rely=0.5,anchor=CENTER)
#c.place(relx=0.5,rely=0.5,anchor=CENTER)
b1= Button(frame2,text="Exit",width=7,height=6,command=close,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
b2= Button(frame2,text="Calculator",command=calculator,width=7,height=7,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
b3= Button(frame2,text="Lights",command=lightcontrol,width=7,height=6,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
b4= Button(frame6,text="Alexa",width=7,height=6,command=alexastart,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
b5= Button(frame6,text="5",width=7,height=7,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
b6= Button(frame6,text="Time Table",command=timetable,width=7,height=6,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')

b.pack(side=LEFT)
c.pack(side=RIGHT)
root.after(100,blink)
root.mainloop()

