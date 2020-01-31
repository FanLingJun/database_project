import tkinter as tk
from tkinter import scrolledtext
from tkinter import Spinbox



def student_grade():
    w3=tk.Tk()
    w3.title('学生成绩单')
    w3.geometry('600x600')
    w3.mainloop()

def student_select_course():
    w2=tk.Tk()
    w2.title('学生选课')
    w2.geometry('800x400')
    tk.Label(w2, text='学生详细信息:', font=('黑体', 14)).place(x=10, y=15)
    tk.Label(w2, text='可选课程:', font=('黑体', 14)).place(x=300, y=15)
    tk.Label(w2, text='请输入课程号:', font=('黑体', 14)).place(x=550, y=15)
    tk.Label(w2, text='已修课程成绩:', font=('黑体', 14)).place(x=10, y=160)
    tk.Label(w2, text='已选课程:', font=('黑体', 14)).place(x=300, y=160)

    '''#利用循环 能显示出表格的样子
    for r in range(3):
        for c in range(3):
            t1=tk.Text(w2,width=10,height=2)
            t1.grid(row=r,column=c)
    '''

    '''#有问题 会报错
    scroll = tk.Scrollbar(w2)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    t1 = tk.Text(w2, width=20, height=10, yscrollcommand=scroll.set)
    scroll.config(command=t1.yview)
    '''

    '''#滑动条位置不对
    scroll_vertical = tk.Scrollbar(w2, orient=tk.VERTICAL)  # 文本框-竖向滚动条
    scroll_horizontal = tk.Scrollbar(w2, orient=tk.HORIZONTAL)  # 文本框-横向滚动条
    t1=tk.Text(w2,width=40,height=10,yscrollcommand=scroll_vertical.set,xscrollcommand=scroll_horizontal.set,wrap='none')

    scroll_vertical.config(command=t1.yview)
    scroll_horizontal.config(command=t1.xview)
    # 布局
    scroll_vertical.pack(fill=tk.Y, expand=0, side=tk.RIGHT, anchor=tk.N)
    scroll_horizontal.pack(fill=tk.X, expand=0, side=tk.BOTTOM, anchor=tk.N)
    t1.pack(fill="x", expand=1, side=tk.LEFT)
    t1.place(x=10,y=35)
    '''

    t1=scrolledtext.ScrolledText(w2, width=35, height=7)
    t1.grid(column=0, row=0, columnspan=3)
    t1.pack()
    t1.place(x=10,y=50)

    t2=scrolledtext.ScrolledText(w2, width=30, height=7)
    t2.grid(column=0, row=0, columnspan=3)
    t2.pack()
    t2.place(x=300,y=50)

    t3=scrolledtext.ScrolledText(w2, width=35, height=10)
    t3.grid(column=0, row=0, columnspan=3)
    t3.place(x=10,y=195)

    t4=scrolledtext.ScrolledText(w2, width=45, height=10)
    t4.grid(column=0, row=0, columnspan=3)
    t4.pack()
    t4.place(x=300,y=195)

    course_number = tk.StringVar()
    course_number.set('')
    course_number = tk.Entry(w2, textvariable=course_number, font=('Arial', 14),width=7)
    course_number.place(x=570,y=80)

    btn_choose = tk.Button(w2, text='选课',width=7)
    btn_choose.place(x=700, y=80)
    btn_drop = tk.Button(w2, text='退课',width=7)
    btn_drop.place(x=700, y=160)
    btn_quit = tk.Button(w2, text='关闭',width=7)
    btn_quit.place(x=700, y=240)
    w2.mainloop()
