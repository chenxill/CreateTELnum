from tkinter import *
import random
from tkinter import messagebox


LastSet = set()


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


# # 生成想要的字符串
# def combineStr(cbset):
#     LastSet=set()
#     for item in cbset:
#        # TELnum=head+item+tail
#        TELnum = head + item + str(tail)
#        LastSet.add(TELnum)
#     return LastSet

top=Tk()

f1=Frame(top)
f2=Frame(top)
f3=Frame(top)
f4=Frame(top)
f5=Frame(top)

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
        LastSet.add(TELnum)

    print(LastSet)



btn=Button(f5,text="生成",command=submitbtn)
btn.pack(side=LEFT)


#保存结果到本地
def savelocaol():
    #######################
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
        LastSet.add(TELnum)


    #######################
    filepath=saveinput.get()
    fo = open(filepath, "w")
    for item in LastSet:
        fo.write(str(item) + "\n")
btn=Button(f5,text="保存",command=savelocaol)
btn.pack(side=RIGHT)
f5.pack()

aset={1,2,3,4}


last=Label(top,text=LastSet)
last.pack()

top.mainloop()
