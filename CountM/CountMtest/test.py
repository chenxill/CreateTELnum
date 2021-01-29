from tkinter import *
import random
# from tkinter import


# 生成一个随机的定长字符串
from tkinter import filedialog, dialog


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

    # 第二次更改需要直接路径
    # filepath=saveinput.get()
    # fo = open(filepath, "w")
    # fo.write(showTel.get('0.0','end'))
    ####################################
    file_path=filedialog.asksaveasfilename(title="保存文件")
    file_text=showTel.get('0.0','end')
    if file_path is not None:
        with open(file=file_path,mode='a+',encoding='utf-8') as file:
            file.write(file_text)
        # 保存之后就清空
        # showTel.delete(1.0,"end")
        dialog.Dialog(None, {'title': 'File Modified', 'text': '保存完成', 'bitmap': 'warning', 'default': 0,
                             'strings': ('OK', 'Cancle')})
        print("保存完成")
btn=Button(f5,text="保存",command=savelocaol)
btn.pack(side=RIGHT)

def delele_text():
    showTel.delete(1.0,"end")
btnclear=Button(f5,text="清空",command=delele_text)
btnclear.pack()
f5.pack()
f6.pack(pady=5)


top.mainloop()
