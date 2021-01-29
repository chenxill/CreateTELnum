import tkinter as tk
import sys

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        toolbar = tk.Frame(self)
        toolbar.pack(side="top", fill="x")
        b1 = tk.Button(self, text="print to stdout", command=self.print_stdout)
        b2 = tk.Button(self, text="print to stderr", command=self.print_stderr)
        b1.pack(in_=toolbar, side="left")
        b2.pack(in_=toolbar, side="left")
        # wrap="word:换行
        self.text = tk.Text(self, wrap="word")
        # fill填充（x:水平，y：垂直，both：水平和垂直填充）
        #expand:当设置为true时，小部件扩展以填充小部件父级中未使用的任何空间。
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("stderr", foreground="#b22222")

        '''
        对输出信息的重定向
        把文件的对象的引用赋给 sys.stdout，
        那么 print 调用的就是文件对象的 write 方法
        '''
        sys.stdout = TextRedirector(self.text, "stdout")
        sys.stderr = TextRedirector(self.text, "stderr")

    def print_stdout(self):
        '''Illustrate that using 'print' writes to stdout'''
        print ("this is stdout")

    def print_stderr(self):
        '''Illustrate that we can write directly to stderr'''
        sys.stderr.write("this is stderr\n")
        print("我是被临添加的")

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

app = ExampleApp()
app.mainloop()