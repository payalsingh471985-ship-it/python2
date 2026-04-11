from tkinter import *
from datetime import date
root = Tk()
root.title("Getting started with widgets")
root.geometry("400x320")
lbl = Label(text = "hi there", fg="white", bg="#072f5f", height=1, width=300 )
name_lbl = Label(text="full name", bg="#389503")
name_entry = Entry()
def display():
    name = name_entry.get()
    global meassage
    meassage = "welcome to the apllication \nToday's date is:"
    greet = "Hello" +name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, meassage)
    text_box.insert(END, date.today())
text_box = Text(height=3)
btn = Button(text="Begin", command = display, height = 1, bg="#126140", fg="white")
lbl.pack_lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()
