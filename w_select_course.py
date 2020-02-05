import sqlite3
import tkinter as tk
from tkinter import scrolledtext
from tkinter import Spinbox

conn = sqlite3.connect('student2.db')#若文件不存在，会自动在当前目录创建
cursor = conn.cursor()#创建一个cursor

#学生详细信息
def student_info(usr_name):
    cursor.execute('select * from s where logn=?', (usr_name,))
    stu_info = cursor.fetchall() #元组列表，此处正常情况下列表中仅有一个元素
    temp = stu_info[0]  #取第一个元组，此处即将元组列表数据类型转换为元组类型
    return temp

# 根据用户名获取学生学号
def get_sno(usr_name):
    cursor.execute('select sno from s where logn=?', (usr_name,))
    sno = cursor.fetchall()
    temp = sno[0]  # 转换数据类型作用，数据类型已转换为元组
    sno = temp[0]  # 数据类型转换为str
    return sno

#返回已修课程的课程号，课程名，成绩
def selected_course(usr_name):
    sno=get_sno(usr_name)
    cursor.execute('select cno,grade from sc where sno=?', (sno,))  # 从学习表中根据学号获取已修课程号及成绩
    values = cursor.fetchall()
    cno_list = [x[0] for x in values]  # 已修课程的课程号列表
    grade_list = [x[1] for x in values]  # 已修课程的成绩列表
    cname_list = []
    for i in range(len(cno_list)):
        cursor.execute('select cname from c where cno=?', (cno_list[i],))  # 由课程号获取课程名
        cname = cursor.fetchall()
        temp = cname[0]  # 数据类型转换到str
        cname_list += [temp[0]]  # 已修课程的课程名列表
    return cno_list,cname_list,grade_list

#将可选课程插入表nsc中（重复插入数据会报错！每个学生未选课情况只需插入一次 有点小问题）
#全部课程除去已修课程，即为可选课程
def insert_table_nsc(usr_name):
    sno = get_sno(usr_name)
    values = selected_course(usr_name)
    selected_cno_list = values[0]  # 已修课程号

    cursor.execute('select cno from c ')
    values = cursor.fetchall()
    cno_list = [x[0] for x in values]  # 全部课程号

    for i in range(len(cno_list)):
        if cno_list[i] not in selected_cno_list:
            cursor.execute('insert into nsc values (\'{}\', \'{}\', 0)'.format(sno, cno_list[i]))
            conn.commit()

#根据课程号获取课程详细信息
def get_course_info(cno):
    cursor.execute('select * from c where cno=?',(cno,))
    values=cursor.fetchall()
    return values[0]

#可选课程（从nsc表中选取可选课程）
def course_available(usr_name):
    sno=get_sno(usr_name)
    cursor.execute('select cno from nsc where sno=? and tag=? ',(sno,0,))
    values=cursor.fetchall()
    not_select_cno_list = [x[0] for x in values]
    not_select_course_info=[]
    for i in range(len(not_select_cno_list)):
        temp=get_course_info(not_select_cno_list[i])
        not_select_course_info+=[temp]
    return not_select_course_info

#已选课程（从nsc表中选取已选课程）
def choosed_course(usr_name):
    sno = get_sno(usr_name)
    cursor.execute('select cno from nsc where sno=? and tag=? ', (sno, 1,))
    values = cursor.fetchall()
    choosed_cno_list = [x[0] for x in values]
    choosed_course_info = []
    for i in range(len(choosed_cno_list)):
        temp = get_course_info(choosed_cno_list[i])
        choosed_course_info += [temp]
    return choosed_course_info

#选课系统主窗口
def student_select_course(usr_name):
    w2=tk.Tk()
    w2.title('学生选课')
    w2.geometry('800x400')
    tk.Label(w2, text='学生详细信息:', font=('黑体', 14)).place(x=10, y=15)
    tk.Label(w2, text='可选课程:', font=('黑体', 14)).place(x=300, y=15)
    tk.Label(w2, text='请输入课程号:', font=('黑体', 14)).place(x=550, y=15)
    tk.Label(w2, text='已修课程成绩:', font=('黑体', 14)).place(x=10, y=160)
    tk.Label(w2, text='已选课程:', font=('黑体', 14)).place(x=300, y=160)

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

    # 选课按钮(课号输入框置空报错)
    def choose_course():
        choose_cno = course_number.get()
        cursor.execute('update nsc set tag=? where cno=?', (1, choose_cno,))
        conn.commit()

    # 退课按钮
    def drop_course():
        choose_cno = course_number.get()
        cursor.execute('update nsc set tag=? where cno=?', (0, choose_cno,))
        conn.commit()

    btn_choose = tk.Button(w2, text='选课',width=7, command=choose_course)
    btn_choose.place(x=700, y=80)
    btn_drop = tk.Button(w2, text='退课',width=7, command=drop_course)
    btn_drop.place(x=700, y=160)
    btn_quit = tk.Button(w2, text='关闭',width=7)
    btn_quit.place(x=700, y=240)

    #测试学生详细信息
    temp = student_info(usr_name)
    t1.insert('end', ' 学号  姓名  年龄  性别   所在系 \n')
    t1.insert('end', ' ' + temp[0] + '  ' + temp[1] + '  ' + temp[2] + '  ' + temp[3] + '  ' + temp[4] + '\n')

    #测试可选课程
    values=course_available(usr_name)
    t2.insert('end', ' 课程号  课程名  学分  开课系  任课教师\n')
    for i in range(len(values)):
        temp=values[i]
        t2.insert('end', temp[0]+'  '+temp[1]+'  '+str(temp[2])+'  '+temp[3]+'  '+temp[4]+'\n')

    #测试已修课程成绩
    values=selected_course(usr_name)
    cno_list=values[0]
    cname_list=values[1]
    grade_list=values[2]
    t3.insert('end', ' 课程号   课程名   成绩\n')
    for i in range(len(cno_list)):
        t3.insert('end', cno_list[i] + '  ' + cname_list[i] + '  ' + str(grade_list[i]) + '\n')

    #测试已选课程
    values = choosed_course(usr_name)
    t4.insert('end', ' 课程号  课程名  学分  开课系  任课教师\n')
    for i in range(len(values)):
        temp = values[i]
        t4.insert('end', temp[0] + '  ' + temp[1] + '  ' + str(temp[2]) + '  ' + temp[3] + '  ' + temp[4] + '\n')

    w2.mainloop()

student_select_course('s3')

cursor.close()
conn.close()

#说明
#基本功能暂时完成
#需要改成多线程 实现实时更新
#关闭按钮功能的实现还没写
#每位学生只能往nsc表中插入一次数据（因为插重复数据会报错），需要修改
#显示格式需要修改（表格+滚动条）

#遇到的问题
#1.需要新建一张表保存可选课程，并带有标记项，来标记是否已选(实现了）
#2.insert不报错，但是数据插不进   database is locked???(暂时没问题了）

