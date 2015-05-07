from tkinter import *

fenetre = Tk()
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
label = Label(fenetre, text="Hello World")
label.pack()
fenetre.overrideredirect(1)
fenetre.geometry("%dx%d+0+0" % (w, h))

fenetre.mainloop()
