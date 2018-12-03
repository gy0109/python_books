
from tkinter import *
import random

fontsize = 30
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan', 'purple']


def onSpam():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg='black', fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)


def onFilp():
    mainLabel.config(fg=random.choice(colors))
    main.after(250, onFilp)


def onGrow():
    global fontsize
    fontsize += 2
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(100, onGrow)


main = Tk()
mainLabel = Label(main, text='Fun Gui!', relief=RAISED)
mainLabel.config(font=('arial', fontsize, 'italic'), fg='cyan', bg='navy')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text='spam', command=onSpam).pack(fill=X)
Button(main, text='filp', command=onFilp).pack(fill=X)
Button(main, text='grow', command=onGrow).pack(fill=X)
main.mainloop()
