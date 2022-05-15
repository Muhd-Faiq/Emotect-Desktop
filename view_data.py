from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from cv2 import add
from pyparsing import col
from deepfaceT.deepface.DeepFace import stream
from auth import *
from tkinter.ttk import Progressbar
import json
import jwt
import home
from UserObj import UserObj
from sign_in import *

class viewData(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.userobj=UserObj()

    def showTable(self):
        #retrieve data
        # startpage = self.controller.get_page("startPage")
        # value = startpage.labeljson_data.get()
        # print("self.labeljson_data")
        # print(value)
        # print(value[0]['aud'])
        # print(value['user_id'])
        # self.result=getSpecificDecision(value['user_id'])
        self.result=getEmotion()
        
        if self.result.status_code==200:
            print(self.result.status_code)
            self.json_data = json.loads(self.result.text)
            
            
            
            # self.userobj.name=numhappy
            # self.userobj.email=numneutral
            # self.userobj.role=numangry


        #start
        self.game_frame = Frame(self)
        self.game_frame.pack()

        #scrollbar
        self.game_scroll = Scrollbar(self.game_frame)
        self.game_scroll.pack(side=RIGHT, fill=Y)

        self.game_scroll = Scrollbar(self.game_frame,orient='horizontal')
        self.game_scroll.pack(side= BOTTOM,fill=X)

        self.my_game = ttk.Treeview(self.game_frame,yscrollcommand=self.game_scroll.set, xscrollcommand =self.game_scroll.set)


        self.my_game.pack()

        self.game_scroll.config(command=self.my_game.yview)
        self.game_scroll.config(command=self.my_game.xview)

        #define our column
        # self._happy = None
        # self._angry = None
        # self._neutral = None
        # self._sad = None
        # self._disgust = None
        # self._surprise = None
        # self._fear = None
        
        self.my_game['columns'] = ('player_Date','player_StartTime','player_EndTime', 'player_Happy','player_Angry','player_Neutral','player_Sad','player_Disgust','player_Surprise','player_Fear', 'player_Id')

        # format our column
        self.my_game.column("#0", width=0,  stretch=NO)
        self.my_game.column("player_Date",anchor=CENTER, width=90)
        self.my_game.column("player_StartTime",anchor=CENTER, width=90)
        self.my_game.column("player_EndTime",anchor=CENTER, width=90)
        self.my_game.column("player_Happy",anchor=CENTER,width=50)
        self.my_game.column("player_Angry",anchor=CENTER,width=50)
        self.my_game.column("player_Neutral",anchor=CENTER,width=50)
        self.my_game.column("player_Sad",anchor=CENTER,width=50)
        self.my_game.column("player_Disgust",anchor=CENTER,width=50)
        self.my_game.column("player_Surprise",anchor=CENTER,width=50)
        self.my_game.column("player_Fear",anchor=CENTER,width=50)
        self.my_game.column("player_Id",anchor=CENTER,width=90)


        #Create Headings 
        self.my_game.heading("#0",text="",anchor=CENTER)
        self.my_game.heading("player_Date",text="Date",anchor=CENTER)
        self.my_game.heading("player_StartTime",text="StartTime",anchor=CENTER)
        self.my_game.heading("player_EndTime",text="EndTime",anchor=CENTER)
        self.my_game.heading("player_Happy",text="Happy",anchor=CENTER)
        self.my_game.heading("player_Angry",text="Angry",anchor=CENTER)
        self.my_game.heading("player_Neutral",text="Neutral",anchor=CENTER)
        self.my_game.heading("player_Sad",text="Sad",anchor=CENTER)
        self.my_game.heading("player_Disgust",text="Disgust",anchor=CENTER)
        self.my_game.heading("player_Surprise",text="Surprise",anchor=CENTER)
        self.my_game.heading("player_Fear",text="Fear",anchor=CENTER)
        self.my_game.heading("player_Id",text="Id",anchor=CENTER)


        

        ##loop
        num=1
        for userdata in self.json_data:
            print(userdata)
            self.numtemphappy = 0
            self.numtempangry = 0
            self.numtempneutral = 0
            self.numtempsad = 0
            self.numtempdisgust = 0
            self.numtempsurprise = 0
            self.numtempfear = 0
            for objemotion in userdata['emotion']:
                print(objemotion)
                if 'Happy' in objemotion:
                    print(objemotion)
                    self.numtemphappy=self.numtemphappy+1
                if 'Angry' in objemotion:
                    self.numtempangry=self.numtempangry+1
                if 'Neutral' in objemotion:
                    self.numtempneutral=self.numtempneutral+1
                if 'Sad' in objemotion:
                    self.numtempsad=self.numtempsad+1
                if 'Disgust' in objemotion:
                    self.numtempdisgust=self.numtempdisgust+1
                if 'Surprise' in objemotion:
                    self.numtempsurprise=self.numtempsurprise+1
                if 'Fear' in objemotion:
                    self.numtempfear=self.numtempfear+1
            self.my_game.insert(parent='',index='end',iid=num,text='',
            values=(userdata['date'],userdata['starttime'],userdata['endtime'],self.numtemphappy,self.numtempangry,self.numtempneutral,self.numtempsad,self.numtempdisgust,self.numtempsurprise,self.numtempfear,userdata['id']))
            num=num+1


        self.my_game.pack()

        self.frame2 = Frame(self)
        self.frame2.pack(pady=20)

        #labels for entry
        # self.playername= Label(self.frame2,text = "player_name")
        # self.playername.grid(row=0,column=0 )

        # self.playeremail = Label(self.frame2,text="player_email")
        # self.playeremail.grid(row=0,column=1)

        # self.playerid = Label(self.frame2,text="player_Id")
        # self.playerid.grid(row=0,column=2)

        #Entry boxes
        self.playername_entry= Entry(self.frame2)
        # self.playername_entry.grid(row= 1, column=0,ipadx=30)

        self.playeremail_entry = Entry(self.frame2)
        # self.playeremail_entry.grid(row=1,column=1,ipadx=30)

        # self.playerid_entry = Entry(self.frame2)
        # self.playerid_entry.grid(row=1,column=2,ipadx=30)
        
        #Select Record
        def select_record():
            # self.edit_button.pack(pady = 10)
            # self.edit_button.place(x=375,y=380, anchor=CENTER)
            #clear entry boxes
            self.playername_entry.delete(0,END)
            self.playeremail_entry.delete(0,END)
            # self.playerid_entry.delete(0,END)
            
            #grab record
            selected=self.my_game.focus()
            #grab record values
            values = self.my_game.item(selected,'values')
            #self.temp_label.config(text=selected)

            #output to entry boxes
            self.playername_entry.insert(0,values[0])
            self.playeremail_entry.insert(0,values[1])
            # self.playerid_entry.insert(0,values[2])
            self.tempplayerid_entry=values[2]
            print(self.tempplayerid_entry)

        #save Record
        def update_record():
            selected=self.my_game.focus()
            #save new data 
            result=updateDataUser(self.playeremail_entry.get(),self.playername_entry.get(),self.tempplayerid_entry)
            if result.status_code==200:
                print(result.status_code)


                json_data = json.loads(result.text)
                self.my_game.item(selected,text="",values=(self.playername_entry.get(),self.playeremail_entry.get(),self.tempplayerid_entry))
                print(self.tempplayerid_entry)

            elif result.status_code==None:
                print("signinNone")
            else:
                print(result.status_code)

            # self.edit_button.forget()
            self.edit_button.place_forget()
            
            
            # self.my_game.item(selected,text="",values=(self.playername_entry.get(),self.playeremail_entry.get(),self.playerid_entry.get()))

        def backPage():
            self.controller.show_frame(home.pageOne)
            
        #clear entry boxes
            self.playername_entry.delete(0,END)
            self.playeremail_entry.delete(0,END)
            # self.playerid_entry.delete(0,END)

        #Buttons
        # self.select_button = Button(self,text="Select Record", command=select_record)
        # self.select_button.pack(pady =10)
        # self.select_button.place(x=375,y=340, anchor=CENTER)

        # self.edit_button = Button(self,text="Edit ",command=update_record)
        # self.edit_button.pack(pady = 10)
        # self.edit_button.place(x=375,y=380, anchor=CENTER)

        self.back_button = Button(self,text="Back ",command=backPage)
        # self.back_button.pack(pady = 10)
        self.back_button.place(x=375,y=380, anchor=CENTER)

        self.temp_label =Label(self,text="")
        self.temp_label.pack()

        #end

        
        
    # def make_widget(self, controller):
    #     some_input = "test input widget"
    #     self.some_entry = Entry(self, textvariable=some_input, width=8)
    #     self.some_entry.pack()
    #     button1 = Button(self, text='Confirm and go to next page', command=lambda: controller.show_frame(pageOne))
    #     button1.pack()



