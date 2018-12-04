import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from tkinter.ttk import *
import sqlite3 as sq
from tkinter import ttk

class TrishApp(tk.Tk):
    def __init__(self, master=None, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(font=("Courier", 20), weight="bold")
        self.tk_setPalette(background="black")
        

        container = tk.Frame(self)
        container.pack(side="top", fill="y", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Fitness Pizza in My Mouth")
        self.geometry("800x700+0+0")
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
        dialog_frame.pack(padx=300, pady=15, anchor='w')

        tk.Label(dialog_frame, text="Username:")
        self.name = tk.Entry(self, background='black', width=24).pack()

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

        label = tk.Label(self, text=" - View Your Daily Nutrition Info -", font=controller.title_font)        
        label.pack(side="top", fill="x", pady=10)

        
        button = tk.Button(self, text="Go back to Menu",
                        command=lambda: controller.show_frame("PageOne"))
        button.pack(pady=100)

        def connect():
            conn = sq.connect('nutrition.db') #dB browser for sqlite needed
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS breakfast(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
            conn.commit()
            conn.close()
        def view():
            conn = sq.connect("nutrition.db")
            c = conn.cursor()
            c.execute("SELECT * FROM Breakfast")
            rows = c.fetchall()
            for row in rows:
                print(row) # it print all records in the database
                bftree.insert("", tk.END, values=row)

            c.execute("SELECT * FROM Lunch")
            rows = c.fetchall()
            for row in rows:
                print(row) # it print all records in the database
                ltree.insert("", tk.END, values=row)

            c.execute("SELECT * from Dinner")
            rows = c.fetchall()
            for row in rows:
                print(row) # it print all records in the database
                dtree.insert("", tk.END, values=row)
            
            c.execute("SELECT * FROM Snack")
            rows = c.fetchall()
            for row in rows:
                print(row) # it print all records in the database
                stree.insert("", tk.END, values=row)
            
            find_calories = ("SELECT SUM(calories), SUM(totalfat),SUM(calories)+ SUM(totalfat) as 'Total' FROM Breakfast")
            c.execute(find_calories)
            print(c.fetchone()[0])

            conn.close()

        bflabel = tk.Label(self, font=controller.title_font, text="Breakfast")
        bflabel.pack()
        bftree = ttk.Treeview(self,height=5,column=("column1", "column2", "column3","column4","column5","column6","column7","column8","column9"), show='headings')
        
        bftree.heading("#1", text="Brand Name")
        bftree.heading( "#2", text="Item Name")
        bftree.heading("#3", text="Calories")
        bftree.heading("#4", text="Fat")
        bftree.heading("#5", text="Protein")
        bftree.heading("#6", text="Total Carbs")
        bftree.heading("#7", text="Dietary Fiber")
        bftree.heading("#8", text="Sugars")
        bftree.heading("#9", text="Sodium")
        bftree.pack()

        llabel = tk.Label(self, font=controller.title_font, text="Lunch")
        llabel.pack()
        ltree = ttk.Treeview(self,height=5,column=("column1", "column2", "column3","column4","column5","column6","column7","column8","column9"), show='headings')
        
        ltree.heading("#1", text="Brand Name")
        ltree.heading( "#2", text="Item Name")
        ltree.heading("#3", text="Calories")
        ltree.heading("#4", text="Fat")
        ltree.heading("#5", text="Protein")
        ltree.heading("#6", text="Total Carbs")
        ltree.heading("#7", text="Dietary Fiber")
        ltree.heading("#8", text="Sugars")
        ltree.heading("#9", text="Sodium")
        ltree.pack()

        dlabel = tk.Label(self, font=controller.title_font, text="Dinner")
        dlabel.pack()
        dtree = ttk.Treeview(self,height=5,column=("column1", "column2", "column3","column4","column5","column6","column7","column8","column9"), show='headings')
        dtree.heading("#1", text="Brand Name")
        dtree.heading( "#2", text="Item Name")
        dtree.heading("#3", text="Calories")
        dtree.heading("#4", text="Fat")
        dtree.heading("#5", text="Protein")
        dtree.heading("#6", text="Total Carbs")
        dtree.heading("#7", text="Dietary Fiber")
        dtree.heading("#8", text="Sugars")
        dtree.heading("#9", text="Sodium")
        dtree.pack()

        slabel = tk.Label(self, font=controller.title_font, text="Snacks")
        slabel.pack()
        stree = ttk.Treeview(self,height=5,column=("column1", "column2", "column3","column4","column5","column6","column7","column8","column9"), show='headings')
        stree.heading("#1", text="Brand Name")
        stree.heading( "#2", text="Item Name")
        stree.heading("#3", text="Calories")
        stree.heading("#4", text="Fat")
        stree.heading("#5", text="Protein")
        stree.heading("#6", text="Total Carbs")
        stree.heading("#7", text="Dietary Fiber")
        stree.heading("#8", text="Sugars")
        stree.heading("#9", text="Sodium")
        stree.pack()

        b2 = tk.Button(self,text="view data", command=view)
        b2.pack()
    


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=" - Add Your Daily Nutrition Info - ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        conn = sq.connect('nutrition.db') #dB browser for sqlite needed
        c = conn.cursor()

        # labels for data entry
        L1 = tk.Label(self, text = "Selct Meal",font=controller.title_font).place(x=10,y=100)
        L2 = tk.Label(self, text = "Brand Name", font=controller.title_font).place(x=10,y=150)
        L3 = tk.Label(self, text = "Item Name", font=controller.title_font).place(x=10,y=200)
        L4 = tk.Label(self, text = "Calories", font=controller.title_font).place(x=10,y=250)
        L5 = tk.Label(self, text = "Total Fat (g)", font=controller.title_font).place(x=10,y=300)
        L6 = tk.Label(self, text = "Protein (g)", font=controller.title_font).place(x=10,y=350)
        L7 = tk.Label(self, text = "Total Carbohydrates (g)", font=controller.title_font).place(x=10,y=400)
        L8 = tk.Label(self, text = "Dietary Fiber (g)", font=controller.title_font).place(x=10,y=450)
        L9 = tk.Label(self, text = "Sugars (g)", font=controller.title_font).place(x=10,y=500)
        L10 = tk.Label(self, text = "Sodium (mg)", font=controller.title_font).place(x=10,y=550)

        #Create variables for each list
  
        comp = StringVar() #For 1st dd
        comp.set('----')
        brand = StringVar()
        item = StringVar()
        calories = StringVar()
        fat = StringVar()
        protein = StringVar()
        carbs = StringVar()
        fiber = StringVar()
        sugar = StringVar()
        sodium = StringVar()

        # values for meal dropdown list of meals
        compoundlist = {'Breakfast', 'Lunch', 'Dinner','Snack'}
        compd = tk.OptionMenu(self, comp, *compoundlist)#For 1st drop down list 
        compd.place(x=400,y=105)

        # entry box for input
        brandT = tk.Entry(self, textvariable=brand)
        brandT.place(x=400,y=155)

        itemT = tk.Entry(self, textvariable=item)
        itemT.place(x=400,y=205)

        caloriesT = tk.Entry(self, textvariable=calories)
        caloriesT.place(x=400,y=255)

        fatT = tk.Entry(self, textvariable=fat)
        fatT.place(x=400,y=305)

        proteinT = tk.Entry(self, textvariable=protein)
        proteinT.place(x=400,y=355)

        carbsT = tk.Entry(self, textvariable=carbs)
        carbsT.place(x=400,y=405)

        fiberT = tk.Entry(self, textvariable=fiber)
        fiberT.place(x=400,y=455)

        sugarT = tk.Entry(self, textvariable=sugar)
        sugarT.place(x=400,y=505)

        sodiumT = tk.Entry(self, textvariable=sodium)
        sodiumT.place(x=400,y=555)

        button = tk.Button(self, text="Go back to Menu",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()


        def clear():
            comp.set('----')
            brand.set('')
            item.set('')
            calories.set('')
            fat.set('')
            protein.set('')
            carbs.set('')
            fiber.set('')
            sugar.set('')
            sodium.set('')
        def post():
            print("You have submitted a record of nutrition")
            c.execute('CREATE TABLE IF NOT EXISTS ' +comp.get()+ '(BrandName TEXT, FoodItem TEXT, Calories INTEGER, TotalFat INTEGER, Protein INTEGER, TotalCarbohydrates INTEGER, DietaryFiber INTEGER, Sugar INTEGER, Sodium INTEGER)')
            c.execute('INSERT INTO ' +comp.get()+ ' (BrandName, FoodItem, Calories, TotalFat, Protein, TotalCarbohydrates, DietaryFiber, Sugar, Sodium) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',(brand.get(), item.get(), calories.get(), fat.get(), protein.get(), carbs.get(), fiber.get(), sugar.get(), sodium.get()))
            conn.commit()


            comp.set('----')
            brand.set('')
            item.set('')
            calories.set('')
            fat.set('')
            protein.set('')
            carbs.set('')
            fiber.set('')
            sugar.set('')
            sodium.set('')

        
        button_1 = tk.Button(self,text="Submit", command=post)
        button_1.place(x=400,y=650)

        button_2 = tk.Button(self,text= "Clear",command=clear)
        button_2.place(x=500,y=650)



if __name__ == '__main__':
    
    app = TrishApp()
    app.mainloop()