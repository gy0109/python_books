
from tkinter import *
from tkinter.messagebox import showerror
import shelve

shelvename = 'people_shelve'
fieldnames = ('name', 'age', 'job', 'pay')
entries = {}

def makeWidgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()

    for (ix, lable) in enumerate(('key', ) + fieldnames):
        lab = Label(form, text=lable)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[Label] = ent

    Button(window, text='Fetch', command=fetchRecord).pack(side=LEFT)
    Button(window, text='Updata', command=UpdateRecord).pack(side=LEFT)
    Button(window, text='Quit', command=quit).pack(side=RIGHT)
    return window


def fetchRecord():
    key = entries['key'].get()
    try:
        record = entries[key]
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def UpdateRecord():
    key = entries['key'].get()
    # record = None
    if key in entries:
        record = entries[key]
    else:
        from person_start import Person
        record = Person(name='?', age='?')
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    entries[key] = record


db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()
