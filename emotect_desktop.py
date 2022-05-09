import tkinter as tk
from cv2 import add
from pyparsing import col
from deepfaceT.deepface.DeepFace import stream
from auth import *
from tkinter.ttk import Progressbar
# import ttk
from sign_in import *
from home import *
from manage_user import *
from register import *



class myFrame1(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        self.visible_frame = "StartPage"

        for F in (startPage,registerPage, pageOne, manageUserPage):
            frame = F(container, self)  #startPage继承了container
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[F] = frame

        self.show_frame(startPage)

    def show_frame(self, page_name):
        print(page_name.__name__)
        frame = self.frames[page_name]
        self.visible_frame = page_name
        frame.tkraise()


    def get_page(self, page_name):
        for page in self.frames.values():
            if str(page.__class__.__name__) == page_name:
                return page
        return None     


# class startPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.make_widget(controller)

#         label = tk.Label(self, text = "StartPage")
#         label.pack(pady = 10, padx = 10)

#         b1 = tk.Button(self, text = "Page One", command = lambda: controller.show_frame(pageOne))
#         b1.pack()


#     def make_widget(self, controller):
#         some_input = "test input widget"
#         self.some_entry = tk.Entry(self, textvariable=some_input, width=8)
#         self.some_entry.pack()
#         button1 = tk.Button(self, text='Confirm and go to next page', command=lambda: controller.show_frame(pageOne))
#         button1.pack()

# class pageOne(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller

#         label = tk.Label(self, text = "Page one")
#         label.pack(pady = 10, padx = 10)

#         b1 = tk.Button(self, text = "go home", command = lambda: self.controller.show_frame(startPage))
#         b1.pack()

#         b2 = tk.Button(self, text = "print", command = lambda: self.print_it())
#         b2.pack()

#     def print_it(self):
#         startpage = self.controller.get_page("startPage")
#         value = startpage.some_entry.get()
#         print(value)



app1 = myFrame1()
app1.wm_geometry("750x550")
app1.title('Emotect Desktop')
app1.iconbitmap('D:\myUTM\Sem 6\PSM 1\code\Emotect Desktop\Emotect.ico')
app1.mainloop()