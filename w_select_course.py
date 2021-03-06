#学生选课主窗口
import sqlite3
import tkinter as tk
from tkinter import messagebox
import w_select_student_score_report as score

conn = sqlite3.connect('student2.db')#若文件不存在，会自动在当前目录创建
cursor = conn.cursor()#创建一个cursor

# 根据用户名获取学生学号
def get_sno(usr_name):
    cursor.execute('select sno from s where logn=?',(usr_name,))
    temp = cursor.fetchall()
    temp = temp[0]
    sno = temp[0]
    print('sno:',sno)
    return sno

#学生详细信息
def student_info(t1,usr_name):
    sno = get_sno(usr_name)
    cursor.execute('select * from s where sno=?',(sno,))
    temp = cursor.fetchall()
    temp = temp[0]
    print('学生详细信息：',temp)
    t1.insert('end', ' 学号  姓名  年龄  性别   所在系 \n')
    t1.insert('end', ' ' + temp[0] + '  ' + temp[1] + '  ' + temp[2] + '  ' + temp[3] + '  ' + temp[4] + '\n')

#返回已修课程的课程号，课程名，成绩
def selected_course(usr_name):
    sno=get_sno(usr_name)
    cursor.execute('select * from sc where sno=?', (sno,))
    temp = cursor.fetchall()
    cno_list = [x[1] for x in temp]  # 已修课程的课程号列表
    grade_list = [x[2] for x in temp]  # 已修课程的成绩列表
    cname_list = []
    for i in range(len(cno_list)):
        cursor.execute('select cname from c where cno=?', (cno_list[i],))
        temp = cursor.fetchall()
        temp=temp[0]
        cname_list += [temp[0]]  # 已修课程的课程名列表
    print('已修课程成绩:',cno_list,cname_list,grade_list)
    return cno_list, cname_list, grade_list

def selected_course_t3(t3,usr_name):
    values=selected_course(usr_name)
    cno_list=values[0]
    cname_list = values[1]
    grade_list = values[2]
    t3.insert('end', ' 课程号   课程名   成绩\n')
    for i in range(len(cno_list)):
        t3.insert('end', cno_list[i] + '  ' + cname_list[i] + '  ' + str(grade_list[i]) + '\n')


#将可选课程插入表nsc中
#全部课程除去已修课程，即为可选课程
def insert_table_nsc(usr_name):
    sno = get_sno(usr_name)
    values = selected_course(usr_name)
    selected_cno_list = values[0]  # 已修课程号

    cursor.execute('select * from c')
    temp = cursor.fetchall()
    cno_list = [x[0] for x in temp]  # 全部课程号
    print('cno:',cno_list)
    print('sno:',sno)
    cursor.execute('select cno from nsc where sno=?', (sno,))
    temp = cursor.fetchall()
    print('nsc:',temp)
    choose_cno_list=[x[0] for x in temp]
    print('已插入nsc表中的:',choose_cno_list)

    for i in range(len(cno_list)):
        if cno_list[i] not in selected_cno_list and cno_list[i] not in choose_cno_list:
            cursor.execute("insert into nsc "
                            "values (?, ?, ?)", (sno, cno_list[i], 0))
            conn.commit()

#根据课程号获取课程详细信息
def get_course_info(cno):
    cursor.execute('select * from c where cno=?', (cno,))
    temp = cursor.fetchall()
    return temp[0]


#可选课程（从nsc表中选取可选课程）
def course_available(t2,usr_name):
    sno = get_sno(usr_name)
    insert_table_nsc(usr_name)
    cursor.execute('select cno from nsc where sno=? and tag=?', (sno,0,))
    values = cursor.fetchall()
    not_select_cno_list = [x[0] for x in values]
    not_select_course_info=[]
    for i in range(len(not_select_cno_list)):
        temp=get_course_info(not_select_cno_list[i])
        not_select_course_info+=[temp]
    print('可选课程：',not_select_course_info)
    t2.insert('end', ' 课程号  课程名  学分  开课系  任课教师\n')
    for i in range(len(not_select_course_info)):
        temp = not_select_course_info[i]
        t2.insert('end', temp[0] + '  ' + temp[1] + '  ' + str(temp[2]) + '  ' + temp[3] + '  ' + temp[4] + '\n')
    #return not_select_course_info

#已选课程（从nsc表中选取已选课程）
def choosed_course(t4,usr_name):
    sno = get_sno(usr_name)
    cursor.execute('select cno from nsc where sno=? and tag=?', (sno, 1,))
    values = cursor.fetchall()
    choosed_cno_list = [x[0] for x in values]
    choosed_course_info = []
    for i in range(len(choosed_cno_list)):
        temp = get_course_info(choosed_cno_list[i])
        choosed_course_info += [temp]
    print('已选课程：',choosed_course_info)

    # 测试已选课程
    #t4.insert('end', ' 课程号  课程名  学分  开课系  任课教师\n')
    t4.insert('end', ' 课程号  课程名  学分  开课系  任课教师\n')
    for i in range(len(choosed_course_info)):
        temp = choosed_course_info[i]
        t4.insert('end', temp[0] + '  ' + temp[1] + '  ' + str(temp[2]) + '  ' + temp[3] + '  ' + temp[4] + '\n')
    #return choosed_course_info

#创建文本框
def create_text(win, w, h, p_x, p_y):
    t = tk.Text(win,width=w,height=h, wrap='none')
    t.propagate(False)
    t.place(x=p_x, y=p_y)
    s1 = tk.Scrollbar(t)
    s1.pack(side=tk.RIGHT,fill=tk.Y)
    s2 = tk.Scrollbar(t, orient=tk.HORIZONTAL)
    s2.pack(side=tk.BOTTOM,fill=tk.X)
    t.config(yscrollcommand=s1.set, xscrollcommand=s2.set)
    s1.config(command=t.yview)
    s2.config(command=t.xview)
    return t

#学生选课主窗口
def student_select_course(usr_name):
    sno = get_sno(usr_name)
    w2 = tk.Tk()
    w2.title('学生选课')
    w2.geometry('850x400')
    tk.Label(w2, text='学生详细信息:', font=('黑体', 14)).place(x=10, y=15)
    tk.Label(w2, text='可选课程:', font=('黑体', 14)).place(x=320, y=15)
    tk.Label(w2, text='请输入课程号:', font=('黑体', 14)).place(x=590, y=15)
    tk.Label(w2, text='已修课程成绩:', font=('黑体', 14)).place(x=10, y=170)
    tk.Label(w2, text='已选课程:', font=('黑体', 14)).place(x=320, y=170)

    t1 = create_text(w2, 40, 8, 10, 50)
    t2 = create_text(w2, 35, 8, 320, 50)
    t3 = create_text(w2, 40, 10, 10, 205)  #已修课程成绩小窗口
    t4 = create_text(w2, 45, 10, 320, 205)

    #学生成绩单跳转
    def handler(event, usr_name):
        score.select_student_score(usr_name)
    def handler_adaptor(fun, **kwds):
        return lambda event, fun=fun, kwds=kwds:fun(event, **kwds)
    t3.bind('<Button-1>',handler_adaptor(handler, usr_name=usr_name))  #控件绑定函数

    course_number = tk.StringVar()
    course_number.set('')
    course_number = tk.Entry(w2, textvariable=course_number, font=('Arial', 14), width=7)
    course_number.place(x=625, y=80)

    #选课按钮
    def choose_course(usr_name):
        choose_cno = course_number.get()
        cursor.execute('select cno from nsc where sno=? and tag=?', (sno,0))
        temp = cursor.fetchall()
        not_choose_cno_list=[x[0] for x in temp]
        cursor.execute('select cno from nsc where sno=? and tag=?', (sno, 1))
        temp = cursor.fetchall()
        choosed_cno_list = [x[0] for x in temp]
        if choose_cno not in not_choose_cno_list and choose_cno not in choosed_cno_list:
            messagebox.showwarning('警告！', '课程名错误！选课失败！')
        elif choose_cno in choosed_cno_list:
            messagebox.showwarning('警告！', '此课程已选！选课失败！')
        else:
            cursor.execute('update nsc set tag=? where sno=? and cno=?', (1, sno,choose_cno))
            conn.commit()
            t2.delete('1.0', 'end')
            course_available(t2, usr_name)
            t4.delete('1.0', 'end')
            choosed_course(t4, usr_name)
        course_number.delete(0, 'end')

    # 退课按钮
    def drop_course(usr_name):
        choose_cno = course_number.get()
        cursor.execute('select cno from nsc where sno=? and tag=?', (sno, 1))
        temp = cursor.fetchall()
        choosed_cno_list = [x[0] for x in temp]
        cursor.execute('select cno from nsc where sno=? and tag=?', (sno, 0))
        temp = cursor.fetchall()
        not_choose_cno_list = [x[0] for x in temp]
        if choose_cno not in choosed_cno_list and choose_cno not in not_choose_cno_list:
            messagebox.showwarning('警告！', '课程名错误！退课失败！')
        elif choose_cno in not_choose_cno_list:
            messagebox.showwarning('警告！', '未选此课程！退课失败！')
        else:
            cursor.execute('update nsc set tag=? where sno=? and cno=?', (0, sno, choose_cno))
            conn.commit()
            t2.delete('1.0', 'end')
            course_available(t2, usr_name)
            t4.delete('1.0', 'end')
            choosed_course(t4, usr_name)
        course_number.delete(0, 'end')

    btn_choose = tk.Button(w2, text='选课', width=7,command=lambda :choose_course(usr_name))
    btn_choose.place(x=750, y=80)
    btn_drop = tk.Button(w2, text='退课', width=7,command=lambda :drop_course(usr_name))
    btn_drop.place(x=750, y=160)
    btn_quit = tk.Button(w2, text='关闭', width=7, command=w2.quit)
    btn_quit.place(x=750, y=240)

    student_info(t1, usr_name)
    course_available(t2, usr_name)
    selected_course_t3(t3, usr_name)
    choosed_course(t4, usr_name)

    w2.mainloop()
