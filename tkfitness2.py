import tkinter as tk
from tkinter import font as tkfont
from tkinter.ttk import *

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
        self.geometry("750x500")
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
        self.user_input = tk.Entry(dialog_frame, background='grey', width=24)
        self.user_input.grid(row=0, column=1, sticky='w')
        self.user_input.focus_set()


        button1 = tk.Button(self, text='Login', command=lambda: controller.show_frame("PageOne"))
        button1.pack()
        button2 = tk.Button(self, text='Cancel', command=self.click_cancel)
        button2.pack()

    def click_cancel(self, event=None):
        print("The user clicked 'Cancel'")


    admins = {'jasmine':'abc123','david':'ABC123'}

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.sp = StartPage

        label = tk.Label(self, text="Welcome to your Nutrition App", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="What would you like to do?" ,font=('Courier', 12))
        label2.pack()
        viewbutton = tk.Button(self, height=5,text='View Your Daily Nutrition Info', command=lambda: controller.show_frame("PageTwo"))
        viewbutton.pack()
        editbutton = tk.Button(self, height=5, text='Edit Your Daily Nutrition Info', command=lambda: controller.show_frame("PageThree"))
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

        self.CreateUI()
        self.LoadTable()
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

        button = tk.Button(self, text="Go back to Menu",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack(pady=100)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('calories', 'fat', 'carbs')
        tv.heading("#0", text='Food Item', anchor='w')
        tv.column("#0", anchor="w")

        tv.heading('calories', text='Calories')
        tv.column('calories', anchor='center', width=100)

        tv.heading('fat', text='Total Fat')
        tv.column('fat', anchor='center', width=100)

        tv.heading('carbs', text='Total Carbohydrates')
        tv.column('carbs', anchor='center', width=100)
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Edit Your Daily Nutrition Info", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back to Menu",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()
if __name__ == '__main__':
    
    app = TrishApp()
    app.mainloop()