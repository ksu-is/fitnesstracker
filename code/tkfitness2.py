import tkinter as tk
from tkinter import font as tkfont
from tkinter.ttk import *
import sqlite3 as sq

class TrishApp(tk.Tk):
    def __init__(self, master=None, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(font=("Courier", 20), weight="bold")
        self.tk_setPalette(background="black")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Fitness Pizza in My Mouth")
        self.geometry("900x750")
        self.bind('<Escape>', StartPage.click_cancel)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Message(self, text="Please Login: ", font=('Courier', 16), justify="left", aspect=800).pack()

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=250, pady=15, anchor='w')

        tk.Label(dialog_frame, text="Username:").grid(row=0, column=0, sticky='w',)
        self.name = Entry(dialog_frame, background='grey', width=24)
        self.name.grid(row=0, column=1, sticky='w')
        self.name.focus_set()


        button1 = tk.Button(self, text='Login', command=lambda: controller.show_frame("PageOne"))
        button1.pack()
        button2 = tk.Button(self, text='Cancel', command=self.click_cancel)
        button2.pack()

        

    def get_user(self):
        return (self.name.get())

    def click_cancel(self, event=None):
        print("The user clicked 'Cancel'")
        print(self.name.get())

    admins = {'jasmine':'abc123','david':'ABC123'}

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.sp = StartPage

        label = tk.Label(self, text="Welcome to your Nutrition App!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="What would you like to do?" ,font=('Courier', 12))
        label2.pack()
        viewbutton = tk.Button(self, height=5,text='View Your Daily Nutrition Info', command=lambda: controller.show_frame("PageTwo"))
        viewbutton.pack()
        editbutton = tk.Button(self, height=5, text='Add Your Daily Nutrition Info', command=lambda: controller.show_frame("PageThree"))
        editbutton.pack()


        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=100)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="View Your Daily Nutrition Info", font=controller.title_font)        
        label.pack(side="top", fill="x", pady=10)



        button = tk.Button(self, text="Go back to Menu",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack(pady=100)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=" - Add Your Daily Nutrition Info - ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        conn = sq.connect('Gym.db') #dB browser for sqlite needed
        c = conn.cursor()

        L1 = tk.Label(self, text = "Selct Meal",font=controller.title_font).place(x=10,y=100)
        L2 = tk.Label(self, text = "Brand Name", font=controller.title_font).place(x=10,y=150)
        L3 = tk.Label(self, text = "Item Name", font=controller.title_font).place(x=10,y=200)
        L4 = tk.Label(self, text = "Calories", font=controller.title_font).place(x=10,y=250)
        L5 = tk.Label(self, text = "Total Fat", font=controller.title_font).place(x=10,y=350)
        L6 = tk.Label(self, text = "Protein (g)", font=controller.title_font).place(x=10,y=300)
        L7 = tk.Label(self, text = "Total Carbohydrates (g)", font=controller.title_font).place(x=10,y=350)
        L8 = tk.Label(self, text = "Dietary Fiber (g)", font=controller.title_font).place(x=10,y=350)
        L9 = tk.Label(self, text = "Sugars (g)", font=controller.title_font).place(x=10,y=350)
        L10 = tk.Label(self, text = "Sodium (mg)", font=controller.title_font).place(x=10,y=350)

        # values for meal dropdown list

        button = tk.Button(self, text="Go back to Menu",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()

if __name__ == '__main__':
    
    app = TrishApp()
    app.mainloop()