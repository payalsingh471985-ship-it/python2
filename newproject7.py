root = Tk()
root.geometry("200x300")
root.title("main")
l1 = Label(root, text = "This is root window")

top = Toplevel()
top.geometry("180x100")
top.title("toplevel")
l2 = Label(top, text = "This is toplevel window")