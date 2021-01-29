from tkinter import *
import random
import sys

'''
输出重定向函数
把文件的对象的引用赋给 sys.stdout，
那么 print 调用的就是文件对象的 write 方法
sys.stdout=TextRedirector(showTel,"stdout")————见下
'''
class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")


# 生成一个随机的定长字符串
def Nstr(lenx):
    randomstr=""
    for item in range(0,lenx):
        randomNum = random.randint(0, 9)
        randomstr=randomstr+str(randomNum)
    return randomstr

# 生成指定数额的字符串（且不能重复）-->返回的字符串集合
def UniqueStr(Unum,Nlen):
    # 申明一个空的set必须使用set（），否则会被默认为声明为字典
    uniset=set()
    while(len(uniset)<Unum):
        uniset.add(Nstr(Nlen))
    return uniset

top=Tk()

f1=Frame(top)
f2=Frame(top)
f3=Frame(top)
f4=Frame(top)
f5=Frame(top)
f6=Frame(top)

head=Label(f1,text="请输号码头")
head.pack(side=LEFT)
headinput=Entry(f1)
headinput.pack(side=RIGHT)

tail=Label(f2,text="请输入尾号")
tail.pack(side=LEFT)
tailinput=Entry(f2)
tailinput.pack(side=RIGHT)

TELnum=Label(f3,text="请输号码数")
TELnum.pack(side=LEFT)
TELnuminput=Entry(f3)
TELnuminput.pack(side=RIGHT)

savepathlabel=Label(f4,text="请输入地址")
savepathlabel.pack(side=LEFT)
saveinput=Entry(f4)
saveinput.pack(side=RIGHT)

showTel=Text(f6,wrap="word")
showTel.pack(fill="both")

f1.pack(pady=5)
f2.pack(pady=5)
f3.pack(pady=5)
f4.pack(pady=5)

# 提交用户键入的信息
def submitbtn():
    head=headinput.get()
    tail=tailinput.get()
    TOTAL=TELnuminput.get()

    lenhead = len(head)
    lentail = len(tail)
    lenlast = 11 - lenhead - lentail
    Uset = UniqueStr(int(TOTAL), lenlast)
    LastSet = set()
    for item in Uset:
        TELnum = head + item + tail
        # LastSet.add(TELnum)
        showTel.insert("end","".join(TELnum)+"\n")
        # 输出
        print(TELnum)

btn=Button(f5,text="生成",command=submitbtn)
btn.pack(side=LEFT)


#保存结果到本地
def savelocaol():
    #######################
    # head=headinput.get()
    # tail=tailinput.get()
    # TOTAL=TELnuminput.get()
    #
    # lenhead = len(head)
    # lentail = len(tail)
    # lenlast = 11 - lenhead - lentail
    # Uset = UniqueStr(int(TOTAL), lenlast)
    # LastSet = set()
    # for item in Uset:
    #     TELnum = head + item + tail
    #     LastSet.add(TELnum)


    #######################
    filepath=saveinput.get()
    fo = open(filepath, "w")
    fo.write(showTel.get('0.0','end'))
    print(showTel.get('0.0','end'))
    print(type(showTel.get('0.0','end')))
btn=Button(f5,text="保存",command=savelocaol)
btn.pack(side=RIGHT)

def delele_text():
    showTel.delete(1.0,"end")
btnclear=Button(f5,text="清空",command=delele_text)
btnclear.pack()
f5.pack()
f6.pack(pady=5)



'''
对输出信息的重定向
把文件的对象的引用赋给 sys.stdout，
那么 print 调用的就是文件对象的 write 方法
'''

top.mainloop()
