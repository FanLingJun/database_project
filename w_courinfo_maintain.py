import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk

conn = sqlite3.connect('student2.db')#若文件不存在，会自动在当前目录创建
cursor = conn.cursor()#创建一个cursor

def course_info_maintain():
    w = tk.Tk()
    w.title('课程信息维护窗口')
    w.geometry('600x400')
    frame_top = tk.Frame(width=600, height=90)
    frame_center = tk.Frame(width=600, height=200)
    lb_tip = tk.Label(w, text='记录总数', font=('黑体', 14)).place(x=240, y=25)

    tree = ttk.Treeview(frame_center, show="headings", height=8, columns=("a", "b", "c", "d","e"))
    vbar = ttk.Scrollbar(frame_center, orient=tk.VERTICAL, command=tree.yview)
    vbar_b = ttk.Scrollbar(frame_center, orient=tk.HORIZONTAL, command=tree.xview)
    # 定义树形结构与滚动条
    tree.configure(yscrollcommand=vbar.set)
    tree.configure(xscrollcommand=vbar_b.set)

    # 表格的标题
    tree.column("a", width=40, anchor="center")
    tree.column("b", width=60, anchor="center")
    tree.column("c", width=40, anchor="center")
    tree.column("d", width=40, anchor="center")
    tree.column("e", width=100, anchor="center")
    tree.heading("a", text="课程号")
    tree.heading("b", text="课程名")
    tree.heading("c", text="学分数")
    tree.heading("d", text="所在系")
    tree.heading("e", text="任课教师")
    # 调用方法获取表格内容插入及树基本属性设置

    for i in range(20):
        tree.insert('', i, values=[str(i)] * 7)

    course_info = course_info_get()
    i = 21
    for course in course_info:
        tree.insert('', i, values=(course[0],course[1],course[2],course[3],course[4]))
        i += 1


    tree["selectmode"] = "browse"
    tree.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10)
    vbar.grid(row=0, column=1, sticky=tk.NS)
    vbar_b.grid(row=1, column=0, sticky=tk.EW)

    frame_top.grid(row=0, column=0, padx=60)
    frame_center.grid(row=1, column=0, padx=60, ipady=1)
    #frame_top.grid_propagate(0)
    frame_center.grid_propagate(0)

    add_button = tk.Button(w, width=7, text="新增", command=helloCallBack)
    add_button.place(x=520, y=90)

    save_button = tk.Button(w, width=7, text="保存", command=helloCallBack)
    save_button.place(x=520, y=130)

    delete_button = tk.Button(w, width=7, text="删除", command=helloCallBack)
    delete_button.place(x=520, y=170)

    exit_button = tk.Button(w, width=7, text="退出", command=w.quit)
    exit_button.place(x=520, y=210)

    tk.mainloop()


def helloCallBack():
    messagebox.showinfo("Now you can see me")


def course_info_get():
    cursor.execute('select * from c',)
    course_info = cursor.fetchall() #元组列表，此处正常情况下列表中仅有一个元素
    return course_info

def add_info():
    return

def save_info():
    return

def delete_info():
    return

if __name__ == '__main__':
    course_info_maintain()
