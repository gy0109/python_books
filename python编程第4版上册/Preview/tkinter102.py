
from tkinter import *
from tkinter.messagebox import showinfo


class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed!')


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()

"""
单击按钮: button (按钮名称 text, 执行函数)
pack: 预设配置
mainloop: 调用启动事件处理
"""
