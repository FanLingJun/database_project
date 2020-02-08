'''成绩管理'''
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Spinbox

temp=None

w4=tk.Tk()
w4.title('成绩管理')
w4.geometry('800x400')

#维护的下拉框#############################################################
#def goto_w_create_stu():  # 跳转至学生表 暂时不写
#def goto_w_create_cou():  # 跳转至课程表 暂时不写

#Menu 的给定参数是所创建菜单的父窗口控件。菜单控件 menubar 将是 w4 框架的顶层。
menubar=tk.Menu(w4)

#maintainmenu 是 menubar 控件的菜单，或 w4的子菜单
maintainmenu=tk.Menu(menubar,tearoff=0)

#add_command 将命令添加到菜单 filemenu。label 是子菜单中显示的文本。
maintainmenu.add_command(label="学生表")
#maintainmenu.add_command(label="学生表",command=goto_w_create_stu)
maintainmenu.add_command(label="课程表")
#maintainmenu.add_command(label="学生表",command=goto_w_create_cou)

#使用命令 add_cascade 将 filemenu 添加到 menubar。维护 是显示在 app 框架顶部的菜单标签
menubar.add_cascade(label='维护',menu=maintainmenu)

runmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='运行',menu=runmenu)

menubar.add_radiobutton(label='关闭',command=w4.quit)

w4.config(menu=menubar)  #配置menubar成为 w4 的 menu。否则，GUI 中不会显示任何菜单栏

def alter():
 temp=comboxlist.get()

comvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(w4, textvariable=comvalue)  # 初始化
###########之后改成用select语句选择出所有课程
comboxlist["values"] = ("1", "2", "3", "4")
comboxlist.pack()
comboxlist.current(2)
comboxlist.bind("<<ComoboxSelected>>",alter)
comboxlist.grid(padx=20, pady=80)

######无法实时将课程的值传递
tk.Label(w4, text='课程:', font=('黑体', 14)).place(x=20, y=15)
tk.Label(w4, text=str(temp), font=('黑体', 14)).place(x=100, y=15)
tk.Label(w4, text='任课教师:', font=('黑体', 14)).place(x=400, y=15)
tk.Label(w4, text='请选择课程名:', font=('黑体', 13)).place(x=20, y=50)
tk.Label(w4, text='已选修次课程的学生:', font=('黑体', 13)).place(x=300, y=50)

t4=scrolledtext.ScrolledText(w4, width=45, height=20)
t4.grid(column=0, row=0, columnspan=3)
t4.place(x=300,y=80)

btn_choose = tk.Button(w4, text='查询',width=7)
btn_choose.place(x=700, y=80)
btn_drop = tk.Button(w4, text='输入成绩',width=7)
btn_drop.place(x=700, y=160)
btn_quit = tk.Button(w4, text='成绩分布',width=7)
btn_quit.place(x=700, y=240)
btn_quit = tk.Button(w4, text='退出',width=7)
btn_quit.place(x=700, y=320)

w4.mainloop()  # 进入消息循环



