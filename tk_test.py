from tkinter import *

fenetre = Tk()
# label = Label(fenetre, text="Hello World")
# label.pack()

# fullscreen
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
# fenetre.overrideredirect(1)
# fenetre.geometry("%dx%d+0+0" % (w, h))

# canvas
def make_canvas(w, h):
    w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
    canvas = Canvas(fenetre, width=w, height=h, background='#660066')
    i = 0
    up = 40
    down = 1040
    right = 300
    left = 420
    while (i <= 5):
           line0 = canvas.create_line(right, up, w - right, up)
           line1 = canvas.create_line(right, 40, right, 420)
           line2 = canvas.create_line(right, 660, right, 1040)
           line3 = canvas.create_line(w - right, 660, w - right, 1040)
           line4 = canvas.create_line(w -right, up, w - right, 420)
           line5 = canvas.create_line(right, down, w - right, down)
           i = i + 1
           up = up + 1
           down = down - 1
           left = left - 1
           right = right + 1
    bim = PhotoImage(file="de")
    canvas.create_image(5, 10, anchor=NW, image=bim)
    #ligne1 = canvas.create_line(75, 0, 75, 120)
    #ligne2 = canvas.create_line(0, 60, 150, 60)
#    txt = canvas.create_text(500, 500, text="attendre", font="Arial 16 italic", fill="blue")
    canvas.pack()


make_canvas(w, h)
fenetre.mainloop()
