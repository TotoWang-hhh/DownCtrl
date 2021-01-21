import tkinter as tk
import tkinter
from tkinter.commondialog import Dialog

root=tk.Tk()
root.withdraw()

top=root

class Dialog:
    def __init__(self, title,width,height):
        # 弹出式窗口中信息内容的宽度和高度
        # 创建顶层组件，不允许改变大小，顶层显示
        self.width=width
        self.height=height
        self.top = tkinter.Toplevel(root)
        self.top.resizable(False,False)
        self.top['bg'] = 'gainsboro'
        # 不显示标题栏
        self.top.overrideredirect(True)
        # 显示伪标题，使用Label组件模拟
        # 使用默认字体，一个汉字约占15个像素位置
        self.lbTitle = tkinter.Label(self.top, text=title)
        self.lbTitle['fg'] = 'black'
        self.lbTitle['bg'] = 'deepskyblue'
        self.lbTitle.place(x=5,
                           y=5,
                           width=len(title)*15,
                           height=20)
        # 关闭按钮，使用英语字母X模拟
        # 根据message长度动态估算起始位置
        def onbtnCloseClick():
            self.top.destroy()
            return 'Close'
        self.btnClose = tkinter.Button(self.top,
                                       text='X',
                                       command=onbtnCloseClick,
                                       bd=0)
        self.btnClose['bg'] = '#b91140'
        self.btnClose.place(x=self.width+20,
                            y=5,
                            width=30,
                            height=20)
        g = str(self.width+60)+'x'+str(self.height+80)+'+500+300'
        self.top.geometry(g)

        # 鼠标左键按下，允许拖动弹出式窗口位置
        self.X = 0
        self.Y = 0
        self.canMove = False
        def onLeftButtonDown(event):
            self.X = event.x
            self.Y = event.y
            self.canMove = True
        self.top.bind('<Button-1>', onLeftButtonDown)
        # 鼠标抬起
        def onLeftButtonUp(event):
          self.canMove = False
        self.top.bind('<ButtonRelease-1>', onLeftButtonUp)
        # 鼠标移动，改变弹出式窗口位置
        def onLeftButtonMove(event):
            if not self.canMove:
                return
            newX = self.top.winfo_x() + (event.x-self.X)
            newY = self.top.winfo_y() + (event.y-self.Y)
            g = str(self.width+60)+'x'+str(self.height+80)+'+'+str(newX)+'+'+str(newY)
            self.top.geometry(g)
        self.top.bind('<B1-Motion>', onLeftButtonMove)
