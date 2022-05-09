from tkinter import *
from typing import Tuple
from PIL import Image, ImageTk
from cv2 import add
# from matplotlib.pyplot import fill
from numpy import angle
from pyparsing import col
from deepfaceT.deepface.DeepFace import stream
from auth import *
from tkinter.ttk import Progressbar
from tkcalendar import *
import datetime
# from page5 import *
import sign_in
from manage_user import *
import json

import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

import threading

from EmotionObj import EmotionObj
import tkinter.font as font






class pageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.emoobj=EmotionObj()
        

        global numangry,numhappy,numneutral,numsad,numdisgust,numsurprise,numfear
        
        
        self.myFont = font.Font(size=16)
        
        
        
        # b1 = Button(self, text = "go home", command = lambda: self.controller.show_frame(sign_in.startPage))
        # b1.pack()

        # b2 = Button(self, text = "print", command = lambda: self.print_it())
        # b2 = Button(self, text = "print", command = lambda: self.getEmotionData)
        # b2.pack()
        
        # self.startpage = self.controller.get_page("startPage")
        # value = self.startpage.password_input.get()
        # print(value)

        #Pie Chart
        # canvas = Canvas(self, width = 200, height = 200)
        # canvas.place(x=375,y=152.5, anchor=CENTER)
        # canvas.create_arc((2,2,150,150),fill="red",outline="red",start=self.angle(0),extent=self.angle(200))
        # canvas.create_arc((2,2,150,150),fill="yellow",outline="yellow",start=self.angle(200),extent=self.angle(200))
        # canvas.create_arc((2,2,150,150),fill="green",outline="green",start=self.angle(400),extent=self.angle(200))
        # canvas.create_arc((2,2,150,150),fill="black",outline="black",start=self.angle(600),extent=self.angle(200))
        # canvas.create_arc((2,2,150,150),fill="orange",outline="orange",start=self.angle(800),extent=self.angle(200))
        # canvas.create_arc((2,2,150,150),fill="orange",outline="orange",start=self.angle(800),extent=self.angle(200))


        #Buttons
        datepicker_btn=Button(self,text='Filter',bg='yellow', fg='black',width=12,command= lambda: self.show_calendar())
        datepicker_btn.place(x=600,y=160.5, anchor=CENTER,width=100) 

        
        #Buttons
        add_btn=Button(self,text='Detect Emotion',width=12,command=self.add_item)
        add_btn.place(x=375,y=300, anchor=CENTER,width=200)
        



    def showmanageuserbutton(self):
        print(type(returnDecoded()))
        self.decodedvalue=returnDecoded()
        #Buttons
        if "admin" in self.decodedvalue:
            if self.decodedvalue["admin"]==True:
                manage_user_btn=Button(self,text='Manage User',width=12,command=self.manageUsershow)
                manage_user_btn.place(x=375,y=350, anchor=CENTER,width=200)
                #Buttons
                manage_dectection_btn=Button(self,text='Manage Detection',width=12,command=self.manageDetectshow)
                manage_dectection_btn.place(x=375,y=400, anchor=CENTER,width=200)

    def getEmotionData(self):
        numangry=0
        numhappy=0
        numneutral=0
        numsad=0
        numdisgust=0
        numsurprise=0
        numfear=0
        self.result=getEmotion()
        if self.result.status_code==200:
            print(self.result.status_code)
            json_data = json.loads(self.result.text)
            for value in json_data:
                for valueEmo in value["emotion"]:
                    if "Happy" in valueEmo:
                        numhappy=numhappy+1
                    elif "Neutral" in valueEmo:
                        numneutral=numneutral+1
                    elif "Angry" in valueEmo:
                        numangry=numangry+1
                    elif "Sad" in valueEmo:
                        numsad=numsad+1
                    elif "Disgust" in valueEmo:
                        numdisgust=numdisgust+1
                    elif "Surprise" in valueEmo:
                        numsurprise=numsurprise+1
                    elif "Fear" in valueEmo:
                        numfear=numfear+1
                    else:
                        print(valueEmo)
            
            
            self.emoobj.happy=numhappy
            self.emoobj.neutral=numneutral
            self.emoobj.angry=numangry
            self.emoobj.sad=numsad
            self.emoobj.disgust=numdisgust
            self.emoobj.surprise=numsurprise
            self.emoobj.fear=numfear
            cond='False'
            self.show_canvas()
            


            # self.labeljson_data = Entry(self)
            # self.labeljson_data.delete(0,END)
            # # self.labeljson_data.insert(0,json_data["idToken"])
            # self.labeljson_data.insert(0,decoded)
            
            # controller.show_frame(pageOne)
            
        elif self.result.status_code==None:
            print(self.result.status_code)
        else:
            print(self.result.status_code)
            print("yayay")

    def show_canvas(self):
        sizeangry=self.emoobj.angry
        sizehappy=self.emoobj.happy
        sizeneutral=self.emoobj.neutral
        sizesad=self.emoobj.sad
        sizedisgust=self.emoobj.disgust
        sizesurprise=self.emoobj.surprise
        sizefear=self.emoobj.fear

        fig=plt.figure(figsize=(3,2),dpi=100)
        # fig.set_size_inches=(6,4)
        labels=tuple()
        sizes=[]
        colors=[]
        explode=[]
        if sizeangry != 0:
            labelsangry='angry',
            labels=labels+labelsangry
            sizes.append(sizeangry)
            colors.append('red')
            explode.append(0)
        if sizehappy != 0:
            labelshappy='happy',
            labels=labels+labelshappy
            sizes.append(sizehappy)
            colors.append('blue')
            explode.append(0)
        if sizeneutral != 0:
            labelsneutral='neutral',
            labels=labels+labelsneutral
            sizes.append(sizeneutral)
            colors.append('yellow')
            explode.append(0)
        if sizesad != 0:
            labelssad='sad',
            labels=labels+labelssad
            sizes.append(sizesad)
            colors.append('green')
            explode.append(0)
        if sizedisgust != 0:
            labelsdisgust='disgust',
            labels=labels+labelsdisgust
            sizes.append(sizedisgust)
            colors.append('orange')
            explode.append(0)
        if sizesurprise != 0:
            labelssurprise='surprise',
            labels=labels+labelssurprise
            sizes.append(sizesurprise)
            colors.append('black')
            explode.append(0)
        if sizefear != 0:
            labelsfear='fear',
            labels=labels+labelsfear
            sizes.append(sizefear)
            colors.append('white')
            explode.append(0)
            

        # labels='angry','happy','neutral','sad','disgust','surprise','fear'
        # sizes=[sizeangry,sizehappy,sizeneutral,sizesad,sizedisgust,sizesurprise,sizefear]
        # colors=['red','blue','yellow','green','orange','black','white']
        # explode=[0,0,0,0,0,0,0]

        plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)

        fig.set_facecolor('#f0f0f0')

        plt.axis('equal')
        canvasbar=FigureCanvasTkAgg(fig,master=self)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=375,y=152.5, anchor=CENTER)
        
    #deepface
    def add_item(self):
        stream()
    
    
    def show_calendar(self):
        print("asdasdasds")
        datem = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        #Buttons
        self.framecalendar=Frame(self,width=380,height=300,highlightbackground='black',highlightthickness=3)
        self.framecalendar.place(x=375,y=152.5, anchor=CENTER)
        #last7 widget
        self.lastseven_label=Button(self.framecalendar,text='Last 7 Days',command=self.last_seven)
        self.lastseven_label.place(x=45,y=45, anchor=CENTER,width=80)
        #month dropdown widget
        self.monthOpt = [
            "Month",
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec"
        ] 
        self.variable = StringVar(self.framecalendar)
        self.variable.set(self.monthOpt[0]) # default value
        #to get is print self.variable.get()
        self.dropdown = OptionMenu(self.framecalendar, self.variable, *self.monthOpt,command=self.choose_month)
        self.dropdown.place(x=45,y=80, anchor=CENTER,width=80)
        #calendar widget
        self.cal=Calendar(self.framecalendar,selectmode="day",year=datem.year,month=datem.month,day=datem.day)
        self.cal.place(x=230,y=125, anchor=CENTER,)
        #choose date widget
        getdate_btn=Button(self.framecalendar,text='Choose Date',width=12,command=self.choose_date)
        getdate_btn.place(x=180,y=250, anchor=CENTER,width=100)
        #choose date widget
        backfromcal_btn=Button(self.framecalendar,text='Back',width=12,command=self.back_from_cal)
        backfromcal_btn.place(x=280,y=250, anchor=CENTER,width=100)

    def last_seven(self):
        curdate=datetime.date.today()
        print(curdate)
        print(curdate-datetime.timedelta(days=7))
        numhappy=0
        numneutral=0
        numangry=0
        numsad=0
        numdisgust=0
        numsurprise=0
        numfear=0
        json_data = json.loads(self.result.text)
        
        for value in json_data:
            tempdate=datetime.datetime.strptime(value["date"], "%d/%m/%Y").date()
            print(tempdate)
            print("curdate")
            
            for x in range(7): 
                print(curdate-datetime.timedelta(days=x))
                if(tempdate==(curdate-datetime.timedelta(days=x))):
                    print("samedate")
                    for valueEmo in value["emotion"]:
                        if "Happy" in valueEmo:
                            numhappy=numhappy+1
                            # self.emoobj.happy=numhappy
                        elif "Neutral" in valueEmo:
                            numneutral=numneutral+1
                            # self.emoobj.neutral=numneutral
                        elif "Angry" in valueEmo:
                            numangry=numangry+1
                            # self.emoobj.angry=numangry
                        elif "Sad" in valueEmo:
                            numsad=numsad+1
                            # self.emoobj.sad=numsad
                        elif "Disgust" in valueEmo:
                            numdisgust=numdisgust+1
                            # self.emoobj.disgust=numdisgust
                        elif "Surprise" in valueEmo:
                            numsurprise=numsurprise+1
                            # self.emoobj.surprise=numsurprise
                        elif "Fear" in valueEmo:
                            numfear=numfear+1
                            # self.emoobj.fear=numfear
                        else:
                            print(valueEmo)

        
        self.emoobj.happy=numhappy
        self.emoobj.neutral=numneutral
        self.emoobj.angry=numangry
        self.emoobj.sad=numsad
        self.emoobj.disgust=numdisgust
        self.emoobj.surprise=numsurprise
        self.emoobj.fear=numfear
        self.framecalendar.place_forget()
        self.show_canvas()


    def choose_month(self,args):
        print(self.variable.get())
        chosendate=datetime.datetime.strptime(self.cal.get_date(), "%m/%d/%y").date()
        tempmonth=self.variable.get()
        chosenmonth=0
        if(tempmonth=='Jan'):
            chosenmonth=1
        elif(tempmonth=='Feb'):
            chosenmonth=2
        elif(tempmonth=='Mar'):
            chosenmonth=3
        elif(tempmonth=='Apr'):
            chosenmonth=4
        elif(tempmonth=='May'):
            chosenmonth=5
        elif(tempmonth=='Jun'):
            chosenmonth=6
        elif(tempmonth=='Jul'):
            chosenmonth=7
        elif(tempmonth=='Aug'):
            chosenmonth=8
        elif(tempmonth=='Sep'):
            chosenmonth=9
        elif(tempmonth=='Oct'):
            chosenmonth=10
        elif(tempmonth=='Nov'):
            chosenmonth=11
        elif(tempmonth=='Dec'):
            chosenmonth=12
            
        numhappy=0
        numneutral=0
        numangry=0
        numsad=0
        numdisgust=0
        numsurprise=0
        numfear=0
        json_data = json.loads(self.result.text)
        print(chosenmonth)
        print(tempmonth)
        for value in json_data:
            tempdate=datetime.datetime.strptime(value["date"], "%d/%m/%Y").date()
            print(tempdate.month)
            if(tempdate.month==chosenmonth):
                print("samedate")
                for valueEmo in value["emotion"]:
                    if "Happy" in valueEmo:
                        numhappy=numhappy+1
                        # self.emoobj.happy=numhappy
                    elif "Neutral" in valueEmo:
                        numneutral=numneutral+1
                        # self.emoobj.neutral=numneutral
                    elif "Angry" in valueEmo:
                        numangry=numangry+1
                        # self.emoobj.angry=numangry
                    elif "Sad" in valueEmo:
                        numsad=numsad+1
                        # self.emoobj.sad=numsad
                    elif "Disgust" in valueEmo:
                        numdisgust=numdisgust+1
                        # self.emoobj.disgust=numdisgust
                    elif "Surprise" in valueEmo:
                        numsurprise=numsurprise+1
                        # self.emoobj.surprise=numsurprise
                    elif "Fear" in valueEmo:
                        numfear=numfear+1
                        # self.emoobj.fear=numfear
                    else:
                        print(valueEmo)

        
        self.emoobj.happy=numhappy
        self.emoobj.neutral=numneutral
        self.emoobj.angry=numangry
        self.emoobj.sad=numsad
        self.emoobj.disgust=numdisgust
        self.emoobj.surprise=numsurprise
        self.emoobj.fear=numfear
        self.framecalendar.place_forget()
        self.show_canvas()

    def choose_date(self):
        print(self.cal.get_date())
        chosendate=datetime.datetime.strptime(self.cal.get_date(), "%m/%d/%y").date()
        numhappy=0
        numneutral=0
        numangry=0
        numsad=0
        numdisgust=0
        numsurprise=0
        numfear=0
        json_data = json.loads(self.result.text)
        print(chosendate)
        for value in json_data:
            tempdate=datetime.datetime.strptime(value["date"], "%d/%m/%Y").date()
            print(tempdate)
            if(tempdate==chosendate):
                print("samedate")
                for valueEmo in value["emotion"]:
                    if "Happy" in valueEmo:
                        numhappy=numhappy+1
                        # self.emoobj.happy=numhappy
                    elif "Neutral" in valueEmo:
                        numneutral=numneutral+1
                        # self.emoobj.neutral=numneutral
                    elif "Angry" in valueEmo:
                        numangry=numangry+1
                        # self.emoobj.angry=numangry
                    elif "Sad" in valueEmo:
                        numsad=numsad+1
                        # self.emoobj.sad=numsad
                    elif "Disgust" in valueEmo:
                        numdisgust=numdisgust+1
                        # self.emoobj.disgust=numdisgust
                    elif "Surprise" in valueEmo:
                        numsurprise=numsurprise+1
                        # self.emoobj.surprise=numsurprise
                    elif "Fear" in valueEmo:
                        numfear=numfear+1
                        # self.emoobj.fear=numfear
                    else:
                        print(valueEmo)

        
        self.emoobj.happy=numhappy
        self.emoobj.neutral=numneutral
        self.emoobj.angry=numangry
        self.emoobj.sad=numsad
        self.emoobj.disgust=numdisgust
        self.emoobj.surprise=numsurprise
        self.emoobj.fear=numfear
        self.framecalendar.place_forget()
        self.show_canvas()
        

    def back_from_cal(self):
        self.framecalendar.place_forget()
    
    def manageDetectshow(self):
        self.controller.show_frame(manageUserPage)

        
    def manageUsershow(self):
        self.controller.show_frame(manageUserPage)
            

    def print_it(self):
        # startpage = self.controller.get_page("startPage")
        # value = startpage.labeljson_data.get()
        value=self.emoobj.happy
        print(value)

    def angle(self,n):
        return 360*n/1000

    