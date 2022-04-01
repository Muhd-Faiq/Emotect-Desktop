from tkinter import *
from PIL import Image, ImageTk
from cv2 import add
from pyparsing import col
from deepfaceT.deepface.DeepFace import stream
from auth import *
from tkinter.ttk import Progressbar



class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self)
       label.pack(side="top", fill="both", expand=True)

       def nextPage():
            import temppage2

       def sign():
            error_label.place_forget()
            result=signin(email_input.get(),password_input.get())
            if result==201:
                print(result)
                return
                # Page2(self).show
                # nextPage()
            elif result==None:
                print(result)
                error_label.place(x=375,y=400, anchor=CENTER)
            else:
                print(result)
                print("yayay")

       f = ("Times bold", 14)
       
       def cancel():
            print(password_input.get())

       num=1
       def add_item():
           while(num==1):
               stream()
        
        
       canvas = Canvas(label, width = 200, height = 210)
       canvas.place(x=375,y=82.5, anchor=CENTER)
       self.img=img = PhotoImage(file='D:\myUTM\Sem 6\PSM 1\code\Emotect Desktop\Emotect_200.png')
       canvas.create_image((20,20), image=img, anchor='nw')
       email_input=StringVar()
       part_label=Label(label,text='Email',font=('bold',14))
       part_label.place(x=262.5,y=220, anchor=CENTER)
       part_entry=Entry(label,textvariable=email_input)
       part_entry.place(x=375,y=247.5, anchor=CENTER,width=300)
       
       password_input=StringVar()
       part_label=Label(label,text='Password',font=('bold',14))
       part_label.place(x=277.5,y=330, anchor=CENTER)
       part_entry=Entry(label,textvariable=password_input)
       part_entry.place(x=375,y=357.5, anchor=CENTER,width=300)
       error_label=Label(label,text='Wrong Email or Password',font=('bold',10),fg='#FF0000')
       error_label.place_forget()
       
       sign_btn=Button(label,text='Sign In',width=12,command=sign)
       sign_btn.place(x=375, y=440, anchor=CENTER)

