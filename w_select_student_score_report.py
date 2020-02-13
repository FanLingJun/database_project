'''学生成绩单'''
import tkinter as tk
import sqlite3
from tkinter import scrolledtext

conn = sqlite3.connect('student2.db')#若文件不存在，会自动在当前目录创建
cursor = conn.cursor()#创建一个cursor

# 根据用户名获取学生学号
def get_sno(usr_name):
    cursor.execute('select sno from s where logn=?', (usr_name,))
    sno = cursor.fetchall()
    temp = sno[0]  # 转换数据类型作用，数据类型已转换为元组
    sno = temp[0]  # 数据类型转换为str
    return sno

# 根据用户名获取学生姓名
def get_name(usr_name):
    cursor.execute('select sname from s where logn=?', (usr_name,))
    name = cursor.fetchall()
    print(name)
    temp = name[0]  # 转换数据类型作用，数据类型已转换为元组
    name = temp[0]  # 数据类型转换为str
    return name

#返回已修课程的课程号，课程名，成绩
def selected_course(usr_name):
    sno=get_sno(usr_name)
    cursor.execute('select cno,grade from sc where sno=?', (sno,))  # 从学习表中根据学号获取已修课程号及成绩
    values = cursor.fetchall()
    cno_list = [x[0] for x in values]  # 已修课程的课程号列表
    grade_list = [x[1] for x in values]  # 已修课程的成绩列表

    cname_list=[]
    tname_list=[]
    credit_list=[]
    for i in range(len(cno_list)):
        cursor.execute('select credit from c where cno=?', (cno_list[i],))  # 由课程号获取学分
        credit=cursor.fetchall()
        temp=credit[0]
        credit_list += [temp[0]]

    for i in range(len(cno_list)):
        cursor.execute('select cname from c where cno=?', (cno_list[i],))  # 由课程号获取课程名
        cname = cursor.fetchall()
        temp = cname[0]  # 数据类型转换到str
        cname_list += [temp[0]]  # 已修课程的教师

    for i in range(len(cno_list)):
        cursor.execute('select tname from c where cno=?', (cno_list[i],))  # 由课程号获取教师名
        tname = cursor.fetchall()
        temp = tname[0]  # 数据类型转换到str
        tname_list += [temp[0]]  # 已修课程的课程名列表


    print('已修课程成绩:',cno_list,cname_list,grade_list,credit_list,tname_list,)
    return cno_list,cname_list,grade_list,credit_list,tname_list,

#学生成绩单主窗口
def select_student_score(usr_name):
    w3 = tk.Tk()
    w3.title('学生成绩单')
    w3.geometry('800x400')
    t = scrolledtext.ScrolledText(w3, width=90, height=20)
    t.grid(column=0, row=0, columnspan=3)
    t.pack()
    t.place(x=80, y=50)

    name=get_name(usr_name)
    t.insert('end', usr_name+'      '+name+'      '+'学生成绩单'+'\n')

    # 测试已修课程成绩
    values = selected_course(usr_name)
    cno_list = values[0]
    cname_list = values[1]
    grade_list = values[2]
    credit_list=values[3]
    tname_list=values[4]

    t.insert('end', ' 课程号   课程名   成绩   学分   教师\n')
    for i in range(len(cno_list)):
        t.insert('end', cno_list[i] + '     ' + cname_list[i] + '  ' + str(grade_list[i]) + '     ' + str(credit_list[i]) +'     ' + str(tname_list[i]) +'\n')

    total_grade=0
    for i in range(len(cno_list)):
        total_grade += grade_list[i]
    average_grade=total_grade/(len(cno_list))
    #print(average_grade)
    #平均成绩
    t.insert('end', '平均成绩:'+'          '+str(average_grade)+'\n')

    w3.mainloop()

#select_student_score('s3')

