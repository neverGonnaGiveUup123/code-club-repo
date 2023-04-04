import tkinter
from tkinter import ttk

class myGui(tkinter.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('My gui')
        self.geometry("100x100")

        self.my_label = ttk.Label(self, text='Hello world!')
        self.my_label.pack()
        
app = myGui()
app.mainloop()