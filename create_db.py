import sqlite3
import tkinter as tk

conn = sqlite3.connect('student2.db')#若文件不存在，会自动在当前目录创建
cursor = conn.cursor()#创建一个cursor
'''
# 执行一条SQL语句，创建s表:
cursor.execute('create table s (sno char(4) primary key, sname char(8),'
               'sex char(2), age char(2), sdept char(10), logn char(20), pswd char(20))')
cursor.execute('insert into s values (\'1001\', \'张三\', \'男\', \'19\', \'计算机\', \'s1\', \'s1\')')
cursor.execute('insert into s values (\'1002\', \'李四\', \'男\', \'21\', \'通信\', \'s2\', \'s2\')')
cursor.execute('insert into s values (\'1003\', \'王五\', \'女\', \'18\', \'新闻\', \'s3\', \'s3\')')
cursor.execute('insert into s values (\'1004\', \'赵六\', \'男\', \'22\', \'计算机\', \'s4\', \'s4\')')

#创建c表
cursor.execute('create table c (cno char(4) primary key, cname char(20),'
               'credit integer, cdept char(10), tname char(8))')

cursor.execute('insert into c values (\'0830\', \'高级语言程序设计\', 4, \'计算机\', \'李青\')')
cursor.execute('insert into c values (\'0831\', \'数字逻辑\', 3, \'计算机\', \'彭俊杰\')')
cursor.execute('insert into c values (\'0832\', \'数据结构\', 4, \'计算机\', \'曹旻\')')
cursor.execute('insert into c values (\'0833\', \'计算机网络\', 6, \'计算机\', \'张云华\')')

#创建sc表
cursor.execute('create table sc(sno char(4) references s(sno),'
               'cno char(4) references c(cno), grade integer, primary key(sno,cno))')
cursor.execute('insert into sc values (\'1001\', \'0830\', 88)')
cursor.execute('insert into sc values (\'1001\', \'0831\', 88)')
cursor.execute('insert into sc values (\'1001\', \'0832\', 91)')
cursor.execute('insert into sc values (\'1001\', \'0833\', 88)')
cursor.execute('insert into sc values (\'1003\', \'0832\', 76)')
cursor.execute('insert into sc values (\'1003\', \'0833\', 65)')
cursor.execute('insert into sc (sno, cno, grade) values (\'1004\', \'0831\', 97)')

cursor.close()
conn.commit()
conn.close()
'''
#学生选课窗口
def w_select_course():
    w2=tk.Tk()
    w2.title('学生选课')
    w2.geometry('600x600')
    tk.Label(w2, text='学生详细信息:', font=('黑体', 14)).place(x=10, y=20)

    w2.mainloop()

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
entry_usr_name.place(x=120,y=100)
# 口令输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(w1, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120,y=140)

#用户登录
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    cursor.execute('select pswd from s where logn=?', (usr_name,))
    values = cursor.fetchall()#该值类型为元组列表
    if usr_pwd in values[0]:
        w_select_course()

#登录/退出按钮
btn_login = tk.Button(w1, text='登录', command=usr_login)
btn_login.place(x=120, y=240)
btn_sign_up = tk.Button(w1, text='退出')
btn_sign_up.place(x=200, y=240)

w1.mainloop()