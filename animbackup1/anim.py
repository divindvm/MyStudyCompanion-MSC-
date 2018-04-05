from Tkinter import *
from PIL import ImageTk, Image
import os
import time
from creds import *

running = True

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
	#Settings
	button = 12 #GPIO Pin with button connected
	lights = [24, 25] # GPIO Pins with LED's conneted
	device = "plughw:1" # Name of your microphone/soundcard in arecord -L

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
        	#GPIO.output(24, GPIO.HIGH)
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
        	#       GPIO.output(25, GPIO.LOW)
		        os.system('mpg123 -q {}1sec.mp3 {}response.mp3'.format(path, path))
        	#       GPIO.output(24, GPIO.LOW)
        	else:
        	#       GPIO.output(lights, GPIO.LOW)
                	for x in range(0, 3):
                        	time.sleep(.2)
        	#               GPIO.output(25, GPIO.HIGH)
        	#               time.sleep(.2)
        	#               GPIO.output(lights, GPIO.LOW)

		
	def start():
        	last = GPIO.input(button)
        	while True:
                	val = GPIO.input(button)
                	if val != last:
                        	last = val
                        	if val == 1 and recorded == True:
                                	rf = open(path+'recording.wav', 'w')
                                	rf.write(audio)
                                	rf.close()
                                	inp = None
                                	alexa()
                        	elif val == 0:
                                	GPIO.output(25, GPIO.HIGH)
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
                	GPIO.output(24, GPIO.HIGH)
                	time.sleep(.1)
                	GPIO.output(24, GPIO.LOW)
        	start()












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

        #l = tk.Label(t, text="This is window ")
        #l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        cbtn=Button(t,command=closecalc,bg='black',fg='grey',text="Back",state='normal',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
	cbtn.pack()
	
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
b2= Button(frame2,text="Calculator",width=7,height=7,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black',command=calculator)
b3= Button(frame2,text="3",width=7,height=6,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
b4= Button(frame6,text="Alexa",width=7,height=6,command=alexavoice,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
b5= Button(frame6,text="5",width=7,height=7,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')
b6= Button(frame6,text="6",width=7,height=6,bg='black',fg='grey',activebackground='black',relief='flat',borderwidth=0,highlightbackground='black')

b.pack(side=LEFT)
c.pack(side=RIGHT)
root.after(100,blink)
root.mainloop()

