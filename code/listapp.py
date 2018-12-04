import tkinter as tk


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()

        tk.Label(self, text="What would you like to do?").pack()

        list_items = ["View Your Daily Nutrition Info", 'Edit Your Daily Nutrition Info']

        self.listbox = tk.Listbox(self, selectmode='extended', bg='white')
        self.listbox.pack(padx=10, pady=10)

        for l in list_items:
            self.listbox.insert('end', l)

        tk.Button(self, text='OK', command=self.ok).pack()

    def ok(self):
        selection = self.listbox.curselection()
        value = ', '.join(self.listbox.get(x) for x in selection)
        print('Listbox Selection: {} "{}"'.format(selection, value))

if __name__ == '__main__':
    root = tk.Tk()
    app = PageOne(root)
    app.mainloop()