#source code
#user needs the following modules(from line 5 to 16) preinstalled in their sysytem in to compile the code without errors
#Anyone can analyze and rewrite the following code and please feel free to send a pull request.
#Explanation for the code will be added shortly.
#MUST READ LINE 192
#for queries contact me through my mail
# mynameisshrish@gmail.com



from tkinter import*
from tkinter import messagebox
import speech_recognition as sr
from cv2 import*
import numpy as np
import os
import time
import smtplib, ssl
import random
import pyttsx3
import wolframalpha
import webbrowser



engine=pyttsx3.init()
num=0
v_num=1
class app(Frame):
    def __init__ (self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.window()
    def window(self):
        self.master.title("DREAM")
        self.pack(fill=BOTH,expand=1)
        listen_button=Button(self,text="listen",width="50",command=self.process_command).pack(side=BOTTOM)
        lbl=Label(self,text="hi i'm dream").pack(side=TOP)
    def talk(self,saying):

        engine.say(saying)
        engine.runAndWait()
    def command(self):
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            out = r.listen(source, phrase_time_limit=5)
        try:
            output = r.recognize_google(out)
            return output
        except sr.UnknownValueError:
            self.talk("i'm sorry Try again")


    def greet(self):
        b = random.choice(["hi" ,"hey","hello there", "hi how are you"])
        self.talk(b)

    def tell_time(self):
        localtime = time.asctime(time.localtime(time.time()))
        a = localtime[11:16]
        self.talk(a)
    def tell_day(self):
        localtime= time.asctime(time.localtime(time.time()))
        day=localtime[0:3]
        if day =="Sun":
            self.talk("it's sunday")
        if day =="Mon":
            self.talk("it's monday")
        if day=="Tue":
            self.talk("it's tuesday")
        if day=="Wed":
            self.talk("it's wednesday")
        if day=="Thu":
            self.talk("it's thursday")
        if day=="Fri":
            self.talk("it's friday")
        if day=="Sat":
            self.talk("it's saturday")
    def tell_month(self):
        localtime = time.asctime(time.localtime(time.time()))
        m_onth=localtime[4:7]
        if m_onth == "Jan":
            self.talk("it's january")
        if m_onth=="Feb":
            self.talk("it's february")
        if m_onth=="Mar":
            self.talk("it's march")
        if m_onth=="Apr":
            self.talk("it's april")
        if m_onth=="May":
            self.talk("it's may")
        if m_onth=="Jun":
            self.talk("it's june")
        if m_onth=="Jul":
            self.talk("it's july")
        if m_onth=="Aug":
            self.talk("it's august")
        if m_onth=="Sep":
            self.talk("it's september")
        if m_onth=="Oct":
            self.talk("it's october")
        if m_onth=="Nov":
            self.talk("it's november")
        if m_onth =="Dec":
            self.talk("it's december")
    def functions(self):
        self.talk("here is a list of what i can do")
        messagebox.showinfo("DREAM functions","1.Try saying 'Hi','Hello'"+
                                              "\n2.Try asking 'What day is this?'"+
                                              "\n3.Try asking 'What month is it?'"+
                                              "\n4.Try asking 'What time is it?'"+
                                              "\n5.You search in google by saying...'Search (or) Google <anything>'"+
                                              "\n6.Play youtube by saying'YouTube... <video_name>'"+
                                              "\n7.Search in Wikipedia by saying...'wikipedia...<anything>'"+
                                              "\n8.You can get answers for mathematical calculations by asking 'Calculate ...<math_problem>'"+
                                              "\n9.You can convert units by saying...'convert...<units to be converted>'"+
                                              "\n10.You can take a picture by saying...'shoot' or 'take a picture'"+
                                              "\n11.You can record video by saying...'capture' or 'record a video'"+
                                              "\n12.You can send a mail by saying...'send mail'"+
                                              "\n13.To close say 'Bye' or 'Sleep' or 'See you later'")

    def search(self,web_name):
        a = "https://google.com/?#q="
        b = a + web_name
        self.talk("searching now")
        webbrowser.open(b, new=2)
    def open_chrome(self):
        self.talk("opening chrome")
    def mailing(self):
        master1 = Tk()
        Label(master1, text="recever").grid(row=0, column=0)
        Label(master1, text="sender").grid(row=1, column=0)
        Label(master1, text="password").grid(row=2, column=0)
        a = Entry(master1)
        a.grid(row=0, column=1)
        b = Entry(master1)
        b.grid(row=1, column=1)
        c = Entry(master1, show="*")
        c.grid(row=2, column=1)
        message_box = Text(master1, height=20, width=40)
        message_box.grid(row=3, column=1)

        def send_mail():
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = str(a.get())  # Enter your address
            receiver_email = str(b.get())  # Enter receiver address
            password = str(c.get())
            message = str(message_box.get("1.0", END))

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

        Button(master1, text="send mail", command=send_mail).grid(row=4, column=1)
        Label(master1, text="message").grid(row=3, column=0)

        mainloop()


    def calc_alpha(self,query):
        app_id="KVL9TA-YHEAR986WP"
        client=wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        self.talk(answer)



    def play_tube(self,vid_name):
        link_tube = "https://www.youtube.com/results?search_query="
        search_vid = link_tube + vid_name
        self.talk("opening youtube")
        webbrowser.open(search_vid, new=2)
    def search_wiki(self,article):
        web_url="https://en.wikipedia.org/wiki/"
        search_query=web_url+article
        self.talk("opening wikipedia")
        webbrowser.open(search_query,new=2)
    def capture(self):
        self.talk("say cheese")
        global num
        num+=1
        cam = VideoCapture(0, cv2.CAP_DSHOW)
        s, img = cam.read()
        if s:
            file_name="F://new"+str(num)+".jpg"
            imshow("cam-test", img)
            waitKey(0)
            destroyWindow("cam-test")
            imwrite(file_name, img)
            
            
#The follwing function (capture_video()) (from line 198 to line 245) is taken from a website.My bad that i dont remember the website
#iam commiting this project after a long time,nearly six months.I will make sure that i eill add credits to 
#that website soon.
     
     
   
    def capture_video(self):
        global v_num
        self.talk("recording now")
        v_num+=1
        video_name = "F://video" + str(v_num) + ".avi"
        frames_per_second = 24.0
        res = '720p'

        # Set resolution for the video capture
        # Function adapted from https://kirr.co/0l6qmh
        def change_res(cap, width, height):
            cap.set(3, width)
            cap.set(4, height)

        # Standard Video Dimensions Sizes
        STD_DIMENSIONS = {
            "480p": (640, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080),
            "4k": (3840, 2160),
        }

        # grab resolution dimensions and set video capture to it.
        def get_dims(cap, res='1080p'):
            width, height = STD_DIMENSIONS["480p"]
            if res in STD_DIMENSIONS:
                width, height = STD_DIMENSIONS[res]
            ## change the current caputre device
            ## to the resulting resolution
            change_res(cap, width, height)
            return width, height

        # Video Encoding, might require additional installs
        # Types of Codes: http://www.fourcc.org/codecs.php
        VIDEO_TYPE = {
            'avi': cv2.VideoWriter_fourcc(*'XVID'),
            # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
            'mp4': cv2.VideoWriter_fourcc(*'XVID'),
        }

        def get_video_type(filename):
            filename, ext = os.path.splitext(filename)
            if ext in VIDEO_TYPE:
                return VIDEO_TYPE[ext]
            return VIDEO_TYPE['avi']

        cap = cv2.VideoCapture(0)
        out = cv2.VideoWriter( video_name, get_video_type(video_name), 25, get_dims(cap, res))
        
        
        
        

        while True:
            ret, frame = cap.read()
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):

                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
    def shut(self):
        end_greet=random.choice(["bye","good bye","take care bye"])
        self.talk(end_greet)
        exit()
    def process_command(self):
        main=self.command()
        if ("hi"== main):
            self.greet()
        if ("quit" == main):
            self.shut()
        if (main=="who are you"):
            self.talk("i am dream, your personal assistant")
        if (main =="what day is this"):
            self.tell_day()
        if (main=="what day is today"):
            self.tell_day()
        if (main=="what day is it"):
            self.tell_day()
        if ("what can you do"==main):
            self.functions()
            self.talk("opening mail")
        if("send mail"==main):
            self.mailing()
            self.tak("opening mail")
        if (main == "what is the  month "):
            self.tell_month()
        if (main=="what is the time"):
            self.tell_time()
        if (main=="what month is it"):
            self.tell_month()
        if (main=="what time is it"):
            self.tell_time()
        if ("Wikipedia" in main):
            self.search_wiki(main[10:])
        if (main=="time please"):
            self.tell_time()
        if (main=="month please"):
            self.tell_month()
        if (main=="what is the month please"):
            self.tell_month()
        if ("search" in main):
            self.search(main[7:])
        if("Google" in main):
            self.search(main[7:])
        if("YouTube" in main):
            self.play_tube(main[8:])
        if ("calculate" in main):
            self.calc_alpha(main[10:])
        if("convert" in main):
            self.calc_alpha(main[8:])
        if("shoot"==main):
            self.capture()
        if("take a picture"==main):
            self.capture()
        if("record a video"==main):
            self.capture_video()
        if("capture"==main):
            self.capture_video()
        if (main=="hello"):
            self.greet()
        if (main=="hey"):
            self.greet()
        if (main=="hey dream"):
            self.greet()
        if(main=="sleep dream"):
            self.shut()
        if(main=="what is the moto of cryptera 2k19"):
            self.talk(" challenge your limits")
        if(main=="bye"):
            self.shut()
        if(main=="bye dream"):
            self.shut()
        if(main=="see you later"):
            self.shut()
        if(main=="shutdown"):
            self.shut()




root=Tk()

main_app=app(root)

main_app.mainloop()
