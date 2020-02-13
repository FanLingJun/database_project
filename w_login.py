import sqlite3
import tkinter as tk
from tkinter import messagebox
import database_crud as op
import w_select_course as stu
import w_teacher_manage as tea


#系统登录
w1=tk.Tk()
w1.title('系统登录')
w1.geometry('400x300')

#用户名/口令提示
tk.Label(w1, text='用户名:', font=('黑体', 14)).place(x=10, y=100)
tk.Label(w1, text='口令:', font=('黑体', 14)).place(x=10, y=140)
# 用户名输入框
var_usr_name = tk.StringVar()
var_usr_name.set('')
entry_usr_name = tk.Entry(w1, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=100)
# 口令输入框
var_usr_pwd = tk.StringVar()
var_usr_pwd.set('')
entry_usr_pwd = tk.Entry(w1, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120, y=140)


#用户登录
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    if usr_name=='':      #！！！待添加光标定位语句！！！
        messagebox.showinfo('提醒', '请输入用户名！')
    if usr_pwd=='':
        messagebox.showinfo('提醒', '请输入密码！')
    usr_name=usr_name.lower()
    usr_pwd=usr_pwd.lower()
    if usr_name=='system' and usr_pwd=='system':
        w1.destroy()
        tea.teacher_manage()
    else:
        temp=op.get_all('s')
        logn_list=[x[5] for x in temp]
        temp=op.search(table_name='s',arr6=usr_name)
        temp=temp[0]
        temp=[x for x in temp]
        print(type(temp))
        pswd=temp[6]
        print(logn_list)
        print(pswd)
        if usr_name not in logn_list:
            messagebox.showwarning('警告！' ,'用户名错！')
            var_usr_pwd.set('')
            var_usr_name.set('')
        elif usr_pwd != pswd:
            messagebox.showwarning('警告！' ,'密码名错！')
            var_usr_pwd.set('')
        else:
            w1.destroy()
            stu.student_select_course(usr_name)

#登录/退出按钮
btn_login = tk.Button(w1, text='登录', font=('黑体', 14), command=usr_login, width=7)
btn_login.place(x=100, y=200)
btn_sign_up = tk.Button(w1, text='退出', font=('黑体', 14) ,width=7)
btn_sign_up.place(x=200, y=200)

w1.mainloop()
