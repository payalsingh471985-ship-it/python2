from tkinter import *
root = Tk()
root.geometrey("200x150")
def save():
    files = ["all files",'.*']
    ('python Files ', '*.py')
    ('Text document','*.txt')
     file = asksaveasfile(filetypes = files, deafaulttextension = files)
    btn = button(root, text = 'save', command = lambda : save())
mainloop