#课程信息维护窗口
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import database_crud

#课程信息维护主窗口
def course_info_maintain():
    global w
    w = tk.Tk()
    w.title('课程信息维护窗口')
    w.geometry('600x400')
    frame_top = tk.Frame(width=600, height=90)
    frame_center = tk.Frame(width=600, height=200)
    lb_tip = tk.Label(w, text='记录总数', font=('黑体', 14)).place(x=200, y=25)
    num = tk.StringVar()
    lb_num = tk.Label(w, textvariable=num, font=('黑体', 14)).place(x=300, y=25)
    num.set(get_count())
    global tree
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

    # for i in range(20):
        # tree.insert('', i, values=[str(i)] * 7)

    # course_info = course_info_get()
    course_info = database_crud.get_all('c')
    i = 0
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

    add_button = tk.Button(w, width=7, text="新增", command=add_info)
    add_button.place(x=520, y=90)

    save_button = tk.Button(w, width=7, text="保存", command=lambda : save_info(tree=tree))
    save_button.place(x=520, y=130)

    delete_button = tk.Button(w, width=7, text="删除", command=delete_info)
    delete_button.place(x=520, y=170)

    exit_button = tk.Button(w, width=7, text="退出", command=w.quit)
    exit_button.place(x=520, y=210)

    w.mainloop()


def delButton(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)

#获取记录总数
def get_count():
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    cur_obj.execute("SELECT COUNT(*) FROM c")
    search_info = cur_obj.fetchall()
    cur_obj.close()
    conn.close()
    return search_info

#新增功能
def add_info():
    root = tk.Tk()
    root.title("增加课程信息")

    tk.Label(root, text="课程号：").grid(row=0, column=0)
    tk.Label(root, text="课程名：").grid(row=1, column=0)
    tk.Label(root, text="学分数：").grid(row=2, column=0)
    tk.Label(root, text="所在系：").grid(row=3, column=0)
    tk.Label(root, text="任课教师：").grid(row=4, column=0)

    e1 = tk.Entry(root)
    e2 = tk.Entry(root)
    e3 = tk.Entry(root)
    e4 = tk.Entry(root)
    e5 = tk.Entry(root)

    # 设置输入框的位置
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)

    # 输入内容获取函数print打印
    def show():
        info = [e1.get(), e2.get(), e3.get(), e4.get(), e5.get()]
        print(e1.get())
        print(e2.get())
        print(info)
        database_crud.insert('c',info)
        # root.quit()

    # 清除函数，清除输入框的内容
    def dele():
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e5.delete(0, tk.END)

    # 设置两个按钮，点击按钮执行命令 command= 命令函数
    theButton1 = tk.Button(root, text="确定", width=10, command=show)
    theButton2 = tk.Button(root, text="清除", width=10, command=dele)

    # 设置按钮的位置行列及大小
    theButton1.grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
    theButton2.grid(row=6, column=1, sticky=tk.E, padx=10, pady=5)

#删除功能
def delete_info():
    root = tk.Tk()
    root.title("删除课程信息")

    tk.Label(root, text="请输入要删除的课程号：").grid(row=0, column=0)

    e1 = tk.Entry(root)

    # 设置输入框的位置
    e1.grid(row=0, column=1)

    # 输入内容获取函数print打印
    def show():
        # 在这个函数里面，首先打印出来从删除框获取到的信息
        # 然后再调用crud里面的函数
        print(e1.get())
        database_crud.delete('c',e1.get())
        # root.quit()

    # 清除函数，清除输入框的内容
    def dele():
        e1.delete(0, tk.END)

    # 设置两个按钮，点击按钮执行命令 command= 命令函数
    theButton1 = tk.Button(root, text="确定", width=10, command=show)
    theButton2 = tk.Button(root, text="清除", width=10, command=dele)

    # 设置按钮的位置行列及大小
    theButton1.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    theButton2.grid(row=2, column=1, sticky=tk.E, padx=10, pady=5)

#保存功能
def save_info(tree):

    num = tk.StringVar()
    lb_num = tk.Label(w, textvariable=num, font=('黑体', 14)).place(x=300, y=25)
    num.set(get_count())

    # 首先，先清除表的内容，然后再获取更新
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    course_info = database_crud.get_all('c')
    i = 0
    for course in course_info:
        tree.insert('', i, values=(course[0], course[1], course[2], course[3], course[4]))
        i += 1

if __name__ == '__main__':
    course_info_maintain()
