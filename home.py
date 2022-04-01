from tkinter import *
from PIL import Image, ImageTk
from cv2 import add
from pyparsing import col
from deepfaceT.deepface.DeepFace import stream
from auth import *
from tkinter.ttk import Progressbar
# from page5 import *
import sign_in

class pageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # label = Label(self, text = "Page one")
        # label.pack(pady = 10, padx = 10)
        
        # b1 = Button(self, text = "go home", command = lambda: self.controller.show_frame(sign_in.startPage))
        # b1.pack()

        # b2 = Button(self, text = "print", command = lambda: self.print_it())
        b2 = Button(self, text = "print", command = lambda: getEmotion())
        b2.pack()
        
        self.startpage = self.controller.get_page("startPage")
        value = self.startpage.password_input.get()
        print(value)

        
        #Buttons
        add_btn=Button(self,text='Detect Emotion',width=12,command=self.add_item)
        add_btn.place(x=375,y=247.5, anchor=CENTER,width=300)
        
        #Buttons
        cancel_btn=Button(self,text='Cancel',width=12,command=self.cancel)
        cancel_btn.place(x=375,y=330, anchor=CENTER,width=300)
        
        #Buttons
        next_btn=Button(self,text='Previous Page',width=12,command=self.prevPage)
        next_btn.place(x=375,y=390, anchor=CENTER,width=300)
        
    #deepface
    def add_item(self):
        stream()
    
    def cancel(self):
        print("yes")
        # cap.release()
        # # cv2.destroyAllWindows()
        #
    def prevPage(self):
        self.destroy()
            

    def print_it(self):
        startpage = self.controller.get_page("startPage")
        value = startpage.labeljson_data.get()
        print(value)