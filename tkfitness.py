import tkinter as tk


class App(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Fitness Pizza In My Mouth")
        
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='black')  # '#ececec' is the standard gray background of El Capitain

        self.master.bind('<Return>', self.click_login)
        self.master.bind('<Escape>', self.click_cancel)
        self.master.geometry("750x500")

        self.master.config(menu=tk.Menu(self))

        tk.Message(self, text="Please Login", font='System 14 bold', justify='left', aspect=800).pack()

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15, anchor='w')

        tk.Label(dialog_frame, text="Username:").grid(row=0, column=0, sticky='w')
        self.user_input = tk.Entry(dialog_frame, background='grey', width=24)
        self.user_input.grid(row=0, column=1, sticky='w')
        self.user_input.focus_set()

        tk.Label(dialog_frame, text="Password:").grid(row=1, column=0, sticky='w')
        self.pass_input = tk.Entry(dialog_frame, background='grey', width=24, show='*')
        self.pass_input.grid(row=1, column=1, sticky='w')

        tk.Button(self, text='Login', default='active', command=self.click_login).pack()
        tk.Button(self, text='Cancel', command=self.click_cancel).pack()
    
    
    def click_login(self, event=None):
        if self.user_input.get() in admins:
            if admins[self.user_input.get()] == self.pass_input.get():
                print("Welcome, ",self.user_input.get())
            else:
                print("Welcome to my Fitness App")

    def click_cancel(self, event=None):
        print("The user clicked 'Cancel'")
        self.master.destroy()

admins = {'jasmine':'abc123','david':'ABC123'}

class ListApp(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()