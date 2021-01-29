#单行文本输入——entry
from tkinter import *
from tkinter import messagebox
top=Tk()
L1=Label(top,text="请输入")
L1.pack(side=LEFT)
e1=Entry(top,bd=5)
e1.pack(side=RIGHT)

print(e1.get())

# 获取输入框的内容
def test():
    # 点击显示文本
    a=e1.get()
    str=a+" 我是后面加上的内容"
    print(str)
# 按钮：按钮上显示的内容，以及绑定的事件
btn=Button(top,text="获取",command=test)
btn.pack()


top.mainloop()