from tkinter import *

# 创建窗口对象的背景颜色
root=Tk()

li=['c','python','java','sql']
movie=['css','jQuery','bootstrap']
# 创建两个列表组件
listb=Listbox(root)
lista=Listbox(root)

# 在部件插入数据
for item in li:
    listb.insert(0,item)

for item in movie:
    lista.insert(0,item)

# 将部件放置到主窗口中
listb.pack()
lista.pack()
# 进入消息循环
root.mainloop()

#################结果：两个方框中分别显示list中的内容

