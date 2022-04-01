from tkinter import *
from PIL import Image, ImageTk
from cv2 import add
from pyparsing import col
from deepfaceT.deepface.DeepFace import stream
from auth import *
from tkinter.ttk import Progressbar

num=1

#deepface
def add_item():
    while(num==1):
        stream()

def cancel():
    print(password_input.get())
    # cap.release()
    # cv2.destroyAllWindows()
    # return

f = ("Times bold", 14)
 
def sign():
    error_label.place_forget()
    result=signin(email_input.get(),password_input.get())
    if result==201:
        print(result)
        nextPage()
    elif result==None:
        print(result)
        error_label.place(x=375,y=400, anchor=CENTER)
    else:
        print(result)
        print("yayay")

def nextPage():
    app.destroy()
    import temppage2

#create window object
app=Tk()


app.title('Emotect Desktop')
app.geometry('750x550')

#icon photo
# ico = Image.open('Emotect.png')
# photo = ImageTk.PhotoImage(ico)
# app.wm_iconphoto(False, photo)
app.iconbitmap('D:\myUTM\Sem 6\PSM 1\code\Emotect Desktop\Emotect.ico')




#Canvas
canvas = Canvas(app, width = 200, height = 210)      
# canvas.pack(side=TOP) 
canvas.place(x=375,y=82.5, anchor=CENTER)
# canvas.grid(row=0,column=1)
img = PhotoImage(file='D:\myUTM\Sem 6\PSM 1\code\Emotect Desktop\Emotect_200.png')      
canvas.create_image(20,20, anchor=NW, image=img)  

#Part Email
email_input=StringVar()
part_label=Label(app,text='Email',font=('bold',14)) #,pady=20,padx=330,justify="left", anchor="w"
part_label.place(x=262.5,y=220, anchor=CENTER)
# part_label.grid(row=1,column=1,sticky = W)
part_entry=Entry(app,textvariable=email_input)
part_entry.place(x=375,y=247.5, anchor=CENTER,width=300)
# part_entry.grid(row=2,column=1,pady=20)

#Part Password
password_input=StringVar()
part_label=Label(app,text='Password',font=('bold',14)) #,pady=20,padx=10
part_label.place(x=277.5,y=330, anchor=CENTER)
# part_label.grid(row=3,column=1)
part_entry=Entry(app,textvariable=password_input)
part_entry.place(x=375,y=357.5, anchor=CENTER,width=300)
# part_entry.grid(row=4,column=1,pady=20)

# #Buttons
# add_btn=Button(app,text='Detect Emotion',width=12,command=add_item)
# add_btn.grid(row=2,column=1,padx=(100, 10))

# #Buttons
# cancel_btn=Button(app,text='Cancel',width=12,command=cancel)
# cancel_btn.grid(row=2,column=2,padx=(100, 10))

# #Buttons
# next_btn=Button(app,text='Next Page',width=12,command=nextPage)
# next_btn.grid(row=2,column=3,padx=(100, 10))



#texterror
error_label=Label(app,text='Wrong Email or Password',font=('bold',10),fg='#FF0000') 
error_label.place(x=375,y=400, anchor=CENTER)
error_label.place_forget()

#Buttons
sign_btn=Button(app,text='Sign In',width=12,command=sign)
sign_btn.place(x=375, y=440, anchor=CENTER)
# sign_btn.grid(row=5,column=1,padx=10)


#start program
app.mainloop()
