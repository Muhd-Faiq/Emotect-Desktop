from tkinter import *
from PIL import Image, ImageTk
from deepfaceT.deepface.DeepFace import *
from auth import *
from tkinter.ttk import Progressbar

ws = Tk()
ws.geometry('750x550')
ws.title('Emotect Desktop')

#icon photo
ico = Image.open('Emotect.png')
photo = ImageTk.PhotoImage(ico)
ws.wm_iconphoto(False, photo)

f = ("Times bold", 14)
 
#deepface
def add_item():
    stream()



def cancel():
    print("yes")
    # cap.release()
    # cv2.destroyAllWindows()

def prevPage():
    ws.destroy()
    import tempemotect_desktop


def showpage2():
    #Buttons
    add_btn=Button(ws,text='Detect Emotion',width=12,command=add_item)
    add_btn.place(x=375,y=247.5, anchor=CENTER,width=300)

    #Buttons
    cancel_btn=Button(ws,text='Cancel',width=12,command=cancel)
    cancel_btn.place(x=375,y=330, anchor=CENTER,width=300)

    #Buttons
    next_btn=Button(ws,text='Previous Page',width=12,command=prevPage)
    next_btn.place(x=375,y=390, anchor=CENTER,width=300)


ws.mainloop()