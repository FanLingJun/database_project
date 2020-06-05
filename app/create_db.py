#创建数据库
import sqlite3

conn = sqlite3.connect('management.db')#若文件不存在，会自动在当前目录创建
cursor = conn.cursor()#创建一个cursor

# 执行一条SQL语句，创建学生表s表:
cursor.execute('create table s (sno char(4) primary key, sname char(8),'
               'sex char(2), age char(2), sdept char(10), logn char(20), pswd char(20))')
#插入数据
cursor.execute('insert into s values (\'1001\', \'张明\', \'男\', \'19\', \'计算机\', \'s1\', \'s1\')')
cursor.execute('insert into s  values (\'1002\', \'李明\', \'男\', \'21\', \'计算机\', \'s2\', \'s2\')')
cursor.execute('insert into s values (\'1003\', \'王铭\', \'女\', \'18\', \'计算机\', \'s3\', \'s3\')')
cursor.execute('insert into s values (\'1004\', \'赵明\', \'男\', \'22\', \'计算机\', \'s4\', \'s4\')')


#创建课程表c表
cursor.execute('create table c (cno char(4) primary key, cname char(20),'
                'credit integer, cdept char(10), tname char(8))')
#插入数据
cursor.execute('insert into c values (\'0830\', \'高级语言程序设计\', 4, \'计算机\', \'李青\')')
cursor.execute('insert into c values (\'0831\', \'数字逻辑\', 3, \'计算机\', \'彭俊杰\')')
cursor.execute('insert into c values (\'0832\', \'数据结构\', 4, \'计算机\', \'曹旻\')')
cursor.execute('insert into c values (\'0833\', \'计算机网络\', 6, \'计算机\', \'张云华\')')

#创建学习表sc表
cursor.execute('create table sc(sno char(4) references s(sno),'
               'cno char(4) references c(cno), grade integer, primary key(sno,cno))')
#插入数据
cursor.execute('insert into sc values (\'1001\', \'0830\', 88)')
cursor.execute('insert into sc values (\'1001\', \'0831\', 88)')
cursor.execute('insert into sc values (\'1001\', \'0832\', 91)')
cursor.execute('insert into sc values (\'1001\', \'0833\', 88)')
cursor.execute('insert into sc values (\'1003\', \'0832\', 76)')
cursor.execute('insert into sc values (\'1003\', \'0833\', 65)')
cursor.execute('insert into sc values (\'1004\', \'0831\', 97)')


#创建未学习表nsc表(记录每位同学未学习的课程，即全部课程除去已修课程)
cursor.execute('create table nsc(sno char(4) references s(sno),'
               'cno char(4) references c(cno), tag integer, primary key(sno,cno))')

# 创建教师表t表:
cursor.execute('create table t (tno char(4) primary key, tname char(8),'
               'sex char(2), age char(2), tdept char(10), logn char(20), pswd char(20))')
#插入数据
cursor.execute('insert into t values (\'3001\', \'张老师\', \'男\', \'39\', \'计算机\', \'t1\', \'password\')')
cursor.execute('insert into t  values (\'3002\', \'李老师\', \'男\', \'42\', \'计算机\', \'t2\', \'password\')')
cursor.execute('insert into t values (\'3003\', \'王老师\', \'女\', \'43\', \'数学\', \'t3\', \'password\')')
cursor.execute('insert into t values (\'3004\', \'赵老师\', \'男\', \'45\', \'计算机\', \'t4\', \'password\')')

cursor.close()
conn.commit()
conn.close()
