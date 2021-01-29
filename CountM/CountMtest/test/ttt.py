from tkinter import *
import sys

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

def print_stdout():
    '''Illustrate that using 'print' writes to stdout'''
    print("this is stdout")
top=Tk()
b1 = Button(top, text="print to stdout", command=print_stdout)
b1.pack()

text=Text(top,wrap="word")
text.pack(fill="both")
text.tag_configure("stdout",foreground="#b22222")
sys.stdout = TextRedirector(text, "stdout")

top.mainloop()