import sqlite3
import tkinter as tk
from tkinter import messagebox
import w_select_course as stu

#！！！整体需改成函数，在主函数中调用！！！

conn = sqlite3.connect('student2.db')#若文件不存在，会自动在当前目录创建
cursor = conn.cursor()#创建一个cursor

#系统登录
w1=tk.Tk()
w1.title('系统登录')
w1.geometry('400x300')

'''
#系统登录界面带图片
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='pic.gif')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='Wellcome', font=('Arial', 16)).pack()
'''

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
        stu.student_select_course()  #！！！要改成转到成绩管理窗口！！！
    else:
        cursor.execute('select logn from s')
        logns=cursor.fetchall()  # 该值类型为元组列表
        logn_list=[x[0] for x in logns]  #取列表中各元组的第一个元素组成新的列表
        cursor.execute('select pswd from s where logn=?', (usr_name,))
        pswd = cursor.fetchall()
        print(logn_list)
        print(pswd)
        if usr_name not in logn_list:
            messagebox.showwarning('警告！' ,'用户名错！')
            var_usr_pwd.set('')
            var_usr_name.set('')
        elif usr_pwd not in pswd[0]:
            messagebox.showwarning('警告！' ,'密码名错！')
            var_usr_pwd.set('')
        else:
            cursor.execute('select count from s where logn=?', (usr_name,))
            temp = cursor.fetchall()
            temp=temp[0]
            temp=temp[0]
            cursor.execute('update s set count=? where logn=?', (temp+1, usr_name,))
            conn.commit()
            stu.student_select_course(usr_name)
            #！！！系统界面消失！！！

#登录/退出按钮
btn_login = tk.Button(w1, text='登录', font=('黑体', 14), command=usr_login, width=7)
btn_login.place(x=100, y=200)
btn_sign_up = tk.Button(w1, text='退出', font=('黑体', 14) ,width=7)
btn_sign_up.place(x=200, y=200)

w1.mainloop()

###待美化界面