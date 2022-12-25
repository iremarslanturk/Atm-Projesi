from tkinter import *
from tkinter import ttk


class Printer:
    def __init__(self, parent):
        self.parent = parent

        self.title = Label(self.parent, text='Fatura ister misiniz?', font=('Helvetica 10 bold'))
        self.title.pack()

        def print_text(text):
            Label(root, text=text, font=('Helvetica 10 bold')).pack()

        self.btn1 = ttk.Button(self.parent, text="Evet", command=lambda:
        print_text("Faturanız verilmiştir."))

        self.btn1.pack(pady=10)
        btn2 = ttk.Button(self.parent, text="Çıkış",command=root.destroy)

        btn2.pack(pady=10)


    def start(self):
        self.parent.mainloop()


root = Tk()
root.geometry("750x250")

app = Printer(root)
app.start()