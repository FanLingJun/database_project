#成绩管理主窗口
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import sqlite3
from tkinter import END   #用来清空内容
import database_crud
import w_stuinfo_maintain as m1
import w_courinfo_maintain as m2
import w_course_score_dis as s1

#成绩管理主界面
def teacher_manage():
 w4 = tk.Tk()
 w4.title('成绩管理')
 w4.geometry('800x400')
 # 维护的下拉框
 def goto_w_create_stu():  # 跳转至学生表
  w4.destroy()
  m1.student_info_maintain()
 def goto_w_create_cou():  # 跳转至课程表
  w4.destroy()
  m2.course_info_maintain()
 # Menu 的给定参数是所创建菜单的父窗口控件。菜单控件 menubar 将是 w4 框架的顶层。
 menubar = tk.Menu(w4)

 # maintainmenu 是 menubar 控件的菜单，或 w4的子菜单
 maintainmenu = tk.Menu(menubar, tearoff=0)

 # add_command 将命令添加到菜单 filemenu。label 是子菜单中显示的文本。
 maintainmenu.add_command(label="学生表",command=goto_w_create_stu)
 maintainmenu.add_command(label="课程表",command=goto_w_create_cou)

 # 使用命令 add_cascade 将 filemenu 添加到 menubar。维护 是显示在 app 框架顶部的菜单标签
 menubar.add_cascade(label='维护', menu=maintainmenu)

 runmenu = tk.Menu(menubar, tearoff=0)
 menubar.add_cascade(label='运行', menu=runmenu)

 menubar.add_radiobutton(label='关闭', command=w4.quit)

 w4.config(menu=menubar)  # 配置menubar成为 w4 的 menu。否则，GUI 中不会显示任何菜单栏

 #下拉框选择课程
 comvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
 comboxlist = ttk.Combobox(w4, textvariable=comvalue)  # 初始化
 conn = sqlite3.connect('student2.db')  # 若文件不存在，会自动在当前目录创建
 cursor = conn.cursor()  # 创建一个cursor
 cursor.execute('select cname from c')
 cname = cursor.fetchall()
 #枚举所有课程
 ccname_list=[]
 for i in range(len(cname)):
  cursor.execute('select cname from c')
  ccname = cursor.fetchall()
  temp = ccname[i]  # 数据类型转换到str
  ccname_list += [temp[0]]

 comboxlist["values"] = (ccname_list)
 comboxlist.pack()
 comboxlist.grid(padx=20, pady=80)

 tk.Label(w4, text='课程:', font=('黑体', 14)).place(x=20, y=15)
 tk.Label(w4, text='任课教师:', font=('黑体', 14)).place(x=400, y=15)
 tk.Label(w4, text='请选择课程名:', font=('黑体', 13)).place(x=20, y=50)
 tk.Label(w4, text='已选修此课程的学生:', font=('黑体', 13)).place(x=300, y=50)

 t4 = scrolledtext.ScrolledText(w4, width=45, height=20)
 t4.grid(column=0, row=0, columnspan=3)
 t4.place(x=300, y=80)

 #返回已选修某课程的学生的学号、成绩
 def selected_course(coursename):
  #根据课程名称找到课号
  cursor.execute('select cno from c where cname=?',(coursename,))
  cno = cursor.fetchall()
  temp = cno[0]  # 转换数据类型作用，数据类型已转换为元组
  cno = temp[0]  # 数据类型转换为str

  cursor.execute('select sno,grade from sc where cno=?',(cno,))
  values = cursor.fetchall()
  sno_list = [x[0] for x in values]  # 已修课程的学号列表
  grade_list = [x[1] for x in values]  # 已修课程的成绩列表
  print(sno_list,grade_list)
  return sno_list,grade_list,

 # 选择好课程后 点击 查询 则调用下列函数
 def query():
  tk.Label(w4, text='                ', font=('黑体', 14)).place(x=100, y=15)
  tk.Label(w4, text='                ', font=('黑体', 14)).place(x=550, y=15)
  temp = comboxlist.get()
  cursor.execute('select tname from c where cname=?', (temp,))
  tname = cursor.fetchall()
  t = tname[0]  # 数据类型转换到str
  tname= t[0]  # 已修课程的教师
  tk.Label(w4, text=temp, font=('黑体', 14)).place(x=100, y=15)
  tk.Label(w4, text=tname, font=('黑体', 14)).place(x=550, y=15)

  t4.delete(1.0,END)  #清空原先内容
  t4.insert('end', ' 学号          成绩\n')
  values=selected_course(temp) #selected_course()函数返回已选修该课程的学生学号，成绩
  sno_list = values[0]
  grade_list = values[1]
  for i in range(len(sno_list)):
   t4.insert('end', sno_list[i] + '            ' + str(grade_list[i])+'\n')

 #输入成绩
 def in_put():
  #使查询 成绩分布 退出 按钮无效
  if btn_query['state'] == 'normal':
   btn_query['state'] = 'disabled'
  if btn_grade_distribution['state'] == 'normal':
   btn_grade_distribution['state'] = 'disabled'
  if btn_quit['state'] == 'normal':
   btn_quit['state'] = 'disabled'

  root = tk.Tk()
  root.title("输入成绩")
  root.geometry('300x100')

  tk.Label(root, text="学号：").grid(row=0, column=0)
  tk.Label(root, text="成绩：").grid(row=1, column=0)

  e1 = tk.Entry(root)
  e2 = tk.Entry(root)

  # 设置输入框的位置
  e1.grid(row=0, column=1)
  e2.grid(row=1, column=1)

 #若关闭窗口 其他按钮可使用
  def on_closing():
   if btn_query['state'] == 'disabled':
    btn_query['state'] = 'normal'
   if btn_grade_distribution['state'] == 'disabled':
    btn_grade_distribution['state'] = 'normal'
   if btn_quit['state'] == 'disabled':
    btn_quit['state'] = 'normal'
   root.destroy()

  root.protocol("WM_DELETE_WINDOW", on_closing)

  def save():
   coursename = comboxlist.get()
   # 根据课程名称找到课号
   cursor.execute('select cno from c where cname=?', (coursename,))
   cno = cursor.fetchall()
   temp = cno[0]  # 转换数据类型作用，数据类型已转换为元组
   cno = temp[0]  # 数据类型转换为str
   cursor.execute('update sc set sno=?, cno=?, grade=? where sno=? and cno=?', (e1.get(),cno, e2.get(),e1.get(),cno))
   conn.commit()

   #修改消息框中成绩
   t4.delete(1.0, END)  # 清空原先内容
   t4.insert('end', ' 学号          成绩\n')
   values = selected_course(coursename)
   sno_list = values[0]
   grade_list = values[1]
   for i in range(len(sno_list)):
    t4.insert('end', sno_list[i] + '            ' + str(grade_list[i]) + '\n')

  def dele():
   e1.delete(0, tk.END)
   e2.delete(0, tk.END)

  # 设置按钮，点击按钮执行命令 command= 命令函数
  theButton1 = tk.Button(root, text="确定", width=10, command=save)
  theButton2 = tk.Button(root, text="清除", width=10, command=dele)

  # 设置按钮的位置行列及大小
  theButton1.grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
  theButton2.grid(row=6, column=1, sticky=tk.E, padx=10, pady=5)

 def goto_w_dis():
  s1.FForm()
 btn_query = tk.Button(w4, text='查询', width=7,command=query)
 btn_query.place(x=700, y=80)
 btn_input = tk.Button(w4, text='输入成绩', width=7,command=in_put)
 btn_input.place(x=700, y=160)
 btn_grade_distribution = tk.Button(w4, text='成绩分布', width=7,command=goto_w_dis)
 btn_grade_distribution.place(x=700, y=240)
 btn_quit = tk.Button(w4, text='退出', width=7,command=w4.quit)
 btn_quit.place(x=700, y=320)

 w4.mainloop()  # 进入消息循环

if __name__ == '__main__':
 teacher_manage()
