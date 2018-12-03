
from tkinter import *
from tkinter.messagebox import showinfo


def reply():
    showinfo(title='popup', message='Button pressed!')


window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()

"""
单击按钮: button (按钮名称 text, 执行函数)
pack: 预设配置
mainloop: 调用启动事件处理
"""
