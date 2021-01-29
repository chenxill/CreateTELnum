from tkinter import *
from tkinter import messagebox

top=Tk()
def test():
    # 点击显示文本
    # messagebox.showinfo("hello python","这是python")
    messagebox.askokcancel("这是titilt","这是内容")
# 按钮：按钮上显示的内容，以及绑定的事件
btn=Button(top,text="点击",command=test)
btn1=Button(top,text="cancel",command=test)
# 将主键放入主窗口
btn1.pack()
# 进入消息循环
top.mainloop()