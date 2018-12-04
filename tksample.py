<<<<<<< HEAD
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
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
=======
from tkinter import*
from tkinter import ttk
import sqlite3

class Product:

    db_name = 'database.db'

    def __init__(self,wind):
        self.wind=wind
        self.wind.title('IT products')

        frame = LabelFrame(self.wind, text='Add new record')
        frame.grid(row=0, column=1)

        Label(frame, text='Name:').grid(row=1, column=1)
        self.name = Entry(frame)
        self.name.grid(row=1, column =2)

        Label(frame, text = 'Price:').grid(row=2, column=1)
        self.price=Entry(frame)
        self.price.grid(row=2, column=2)

        ttk.Button(frame, text='Add record').grid (row=3,column=2)
        self.message=Label(text='', fg='red')
        self.message.grid(row=3, column=0)

        self.tree = ttk.Treeview (height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0',text = 'Name', anchor=W)
        self.tree.heading(2, text='Price', anchor=W)
>>>>>>> cf772eed6bf3adf5c0fdfd2b4e04e3c7450929b5

        ttk.Button(text= 'Delete record').grid (row=5, column=0)
        ttk.Button(text= 'Edit record').grid(row=5, column=1)

<<<<<<< HEAD
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
=======
        self.viewing_records()


    def run_query(self, query, parameters =()):
        with sqlite3.connect (self.db_name) as conn:
            cursor = conn.cursor()
            query_result=cursor.execute(query, parameters)
            conn.commit()
        return query_result()



    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query= 'SELECT * FROM product ORDER BY name DESC'
        db_rows=self.run_query(query)
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = row[2])


if __name__ == '__main__':
    wind=Tk()
    application = Product(wind)
    wind.mainloop()
>>>>>>> cf772eed6bf3adf5c0fdfd2b4e04e3c7450929b5
