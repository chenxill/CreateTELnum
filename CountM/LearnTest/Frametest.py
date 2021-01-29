from tkinter import *

root=Tk()

f1=Frame(root,relief=SUNKEN,bd=5)
f2=Frame(root,relief=GROOVE,bd=5)
root.title("框架测试")

l=Label(f1,text="标签中的内容1",justify=LEFT)
l.pack()
l1=Label(f2,text="标签中的内容2",justify=LEFT)
l1.pack()
f1.pack(padx=100,pady=100,)
f2.pack(padx=0,pady=100)
root.mainloop()