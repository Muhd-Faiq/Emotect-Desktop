from tkinter import *
from PIL import Image, ImageTk
from cv2 import add
from pyparsing import col
from deepfaceT.deepface.DeepFace import stream
from auth import *
from tkinter.ttk import Progressbar
from home import *
import register
from manage_user import *
import json
import jwt

class startPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        # self.make_widget(controller)

        # label = Label(self, text = "StartPage")
        # label.pack(pady = 10, padx = 10)
        
        # b1 = Button(self, text = "Page One", command = lambda: controller.show_frame(pageOne))
        # b1.pack()

        def nextPage():
            import temppage2


        self.tempvalue = Entry(self)
        self.tempvalue.delete(0,END)
        self.tempvalue.insert(0,'False')

        self.labeljson_data = Entry(self)

        def sign():
            error_label.place_forget()
            result=signin(email_input.get(),password_input.get())
            if result.status_code==201:
                print(result.status_code)
                error_label.place_forget()


                json_data = json.loads(result.text)
                # print(json_data["idToken"])

                key='super-secret'
                # payload={"id":"1","email":"myemail@gmail.com" }
                # token = jwt.encode(payload, key)
                # print (token)
                decoded = jwt.decode(json_data["idToken"], options={"verify_signature": False}) # works in PyJWT >= v2.0

                
                self.labeljson_data.delete(0,END)
                # self.labeljson_data.insert(0,json_data["idToken"])
                self.labeljson_data.insert(0,decoded)

                print(decoded)
                self.tempvalue.delete(0,END)
                self.tempvalue.insert(0,'True')

                
                
                # pageOne.getEmotionData()
                self.decodedvalue=returnDecoded()
                if "admin" in self.decodedvalue:
                    if self.decodedvalue["admin"]==True:
                        self.controller.get_page("manageUserPage").showTable()
                        self.controller.get_page("pageOne").showmanageuserbutton()
                        self.controller.get_page("manageDetectionPage").showDetectionTable()
                self.controller.get_page("pageOne").getEmotionData()
                # controller.destroy_frame(pageOne)
                controller.show_frame(pageOne)
                # Page2(self).show
                # nextPage()
            elif result.status_code==None:
                print("signinNone")
                error_label.place(x=375,y=400, anchor=CENTER)
            else:
                error_label.place(x=375,y=400, anchor=CENTER)
                print(result.status_code)
        
        f = ("Times bold", 14)
        def cancel():
            print(password_input.get())
        
        num=1
        
        def add_item():
            while(num==1):
                stream()
        
        def registerfunction():
            self.controller.show_frame(register.registerPage)
        
        canvas = Canvas(self, width = 200, height = 210)
        canvas.place(x=375,y=82.5, anchor=CENTER)
        self.img=img = PhotoImage(file='D:\myUTM\Sem 6\PSM 1\code\Emotect Desktop\Emotect_200.png')
        canvas.create_image((20,20), image=img, anchor='nw')
        # canvas.pack()

        email_input=StringVar()
        part_label=Label(self,text='Email',font=('bold',14))
        part_label.place(x=262.5,y=220, anchor=CENTER)
        # part_label.pack()

        self.email_input=Entry(self,textvariable=email_input)
        self.email_input.place(x=375,y=247.5, anchor=CENTER,width=300)
        # self.email_input.pack()

        password_input=StringVar()
        part_label=Label(self,text='Password',font=('bold',14))
        part_label.place(x=277.5,y=330, anchor=CENTER)
        # part_label.pack()
        
        self.password_input=Entry(self,textvariable=password_input,show="\u2022")
        self.password_input.place(x=375,y=357.5, anchor=CENTER,width=300)
        # self.password_input.pack()

        error_label=Label(self,text='Wrong Email or Password',font=('bold',10),fg='#FF0000')
        # error_label.pack()
        error_label.place_forget()
        

        sign_btn=Button(self,text='Sign In',width=12,command=sign)
        sign_btn.place(x=320, y=440, anchor=CENTER)
        # sign_btn.pack()

        register_btn=Button(self,text='Register',width=12,command=registerfunction)
        register_btn.place(x=415, y=440, anchor=CENTER)
        
        
    def make_widget(self, controller):
        some_input = "test input widget"
        self.some_entry = Entry(self, textvariable=some_input, width=8)
        self.some_entry.pack()
        button1 = Button(self, text='Confirm and go to next page', command=lambda: controller.show_frame(pageOne))
        button1.pack()



