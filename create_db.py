import sqlite3
import tkinter as tk

<<<<<<< HEAD
conn = sqlite3.connect('student2.db')#若文件不存在，会自动在当前目录创建
cursor = conn.cursor()#创建一个cursor

# 执行一条SQL语句，创建s表:
cursor.execute('create table s (sno char(4) primary key, sname char(8),'
               'sex char(2), age char(2), sdept char(10), logn char(20), pswd char(20), count integer default 0)')
cursor.execute('insert into s (sno, sname, sex, age, sdept, logn, pswd) values (\'1001\', \'张三\', \'男\', \'19\', \'计算机\', \'s1\', \'s1\')')
cursor.execute('insert into s (sno, sname, sex, age, sdept, logn, pswd) values (\'1002\', \'李四\', \'男\', \'21\', \'通信\', \'s2\', \'s2\')')
cursor.execute('insert into s (sno, sname, sex, age, sdept, logn, pswd) values (\'1003\', \'王五\', \'女\', \'18\', \'新闻\', \'s3\', \'s3\')')
cursor.execute('insert into s (sno, sname, sex, age, sdept, logn, pswd)values (\'1004\', \'赵六\', \'男\', \'22\', \'计算机\', \'s4\', \'s4\')')

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


#创建nsc表(未选课表)
cursor.execute('create table nsc(sno char(4) references s(sno),'
               'cno char(4) references c(cno), tag integer, primary key(sno,cno))')

cursor.close()
conn.commit()
conn.close()
=======
>>>>>>> 0b76f54de0a3b230f60f8fdcc89db26e926c2f7f
