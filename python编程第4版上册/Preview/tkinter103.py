
from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='Reply', message='hello %s !' % name)


top = Tk()              # Tk() 主页面的设置
top.title('Echo')       # 头部
# top.iconbitmap('py-blue-trans-out.ico')  # 更换logo图片 加载文件系统内容
Label(top, text='Enter your name:').pack(side=TOP)    # 布局管理 text 文本信息 side 格式设置

ent = Entry(top)     # 写入的地方
ent.pack(side=TOP)

btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))   # 按钮设置
btn.pack(side=TOP)

top.mainloop()

"""
单击按钮: button (按钮名称 text, 执行函数)
pack: 预设配置
mainloop: 调用启动事件处理
"""
