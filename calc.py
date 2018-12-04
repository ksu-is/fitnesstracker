import tkinter as tk
class Main(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.lbl = tk.Label(self.master)
        self.entry = tk.Entry(self.master)
        self.btn = tk.Button(text='Calculate!', command=self.calc)
        self.lbl.pack()
        self.entry.pack()
        self.btn.pack()
        self.calculator = Calculator()

    def calc(self):
        data = self.entry.get()
        self.lbl['text'] = self.calculator.do_math(data)

class Calculator:
    def do_math(self, input):
        return int(input) * 2

if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.mainloop()