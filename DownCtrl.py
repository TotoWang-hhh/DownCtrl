#2020 By 人工智障
#未经准许，禁止改编
#仅适用于Python 3.x

import requests
import tkinter as tk
import tkinter.ttk as ttk
import ui_components.dialog as dialog
import tkinter.filedialog as filedialog
import hashlib
import os

tasks=[]

class Task():
    def __init__(self,url,md5,path,status):
        self.url=url
        self.md5=md5
        self.path=path
        self.status=status

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'}

def func_new_path_insert():
    path=filedialog.asksaveasfilename(title='保存路径')
    path_enter.insert(tk.END,path)

def get_md5(url):
    res=requests.get(url,headers=header)
    print(res)
    data=res.content
    print('data getted')
    md5=hashlib.md5(data).hexdigest()
    print(md5)
    md5_enter.insert(tk.END,md5)

def add(url,md5,path):
    tasks.insert(0,Task(url,md5,path,'等待'))
    tree.insert("",0,0,values=(tasks[0].url,tasks[0].status))

def start():
    for i in tasks:
        os.system("python {0} {1} {2}".format(i.url,i.md5,i.path))

def new():
    global path_enter
    global md5_enter
    print('new')
    add_win=dialog.Dialog('新任务',300,300)
    main=tk.Frame(add_win.top,width=280,height=260)
    main.place(x=10,y=30)
    ttk.Label(main,text='文件URL').pack()
    url_enter=ttk.Entry(main,width=48)
    url_enter.pack()
    ttk.Label(main,text='MD5').pack()
    md5_enter=ttk.Entry(main,width=48)
    md5_enter.pack()
    ttk.Button(main,text='自动获取',command=lambda:get_md5(url_enter.get())).pack()
    ttk.Label(main,text='目标路径').pack()
    path_enter=ttk.Entry(main,width=48)
    path_enter.pack()
    ttk.Button(main,text='浏览',command=func_new_path_insert).pack()
    ttk.Button(main,text='添加任务',command=lambda:add(url_enter.get(),md5_enter.get(),path_enter.get())).pack()

win=tk.Tk()
win.title('DownCtrl')

top=win

menubar=tk.Menu(win)
menu1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='操作', menu=menu1)
menu1.add_command(label='新建任务', command=new)
menu1.add_command(label='全部开始', command=start)
menu1.add_command(label='退出', command=exit)
win.config(menu=menubar)

tree=ttk.Treeview(win,show="headings")#表格
tree["columns"]=("URL","状态")
tree.column("URL",width=100) #表示列,不显示
tree.column("状态",width=70)
tree.heading("URL",text="URL") #显示表头
tree.heading("状态",text="状态")
tree.pack(fill=tk.BOTH)

win.mainloop()

#
