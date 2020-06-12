#创建数据库
import sqlite3

conn = sqlite3.connect('management.db')#若文件不存在，会自动在当前目录创建
cursor = conn.cursor()#创建一个cursor


# 执行一条SQL语句，创建学生表s表:
cursor.execute('create table s (xh char(4) primary key, xm char(8),'
               'xb char(2), csrq date, jg char(10), sjhm char(20), yxh char(10))')
#插入数据
cursor.execute('INSERT INTO S VALUES (\'1101\', \'李明\', \'男\', \'1993-03-06\', \'上海\', \'13613005486\', \'02\')')
cursor.execute('INSERT INTO s VALUES (\'1102\', \'刘晓明\', \'男\', \'1992-12-08\', \'安徽\', \'18913457890\', \'01\')')
cursor.execute('INSERT INTO s VALUES (\'1103\', \'张颖\', \'女\', \'1993-01-05\', \'江苏\', \'18826490423\', \'01\')')
cursor.execute('INSERT INTO s VALUES (\'1104\', \'刘晶晶\', \'女\', \'1994-11-06\', \'上海\', \'13331934111\', \'01\')')
cursor.execute('INSERT INTO s VALUES (\'1105\', \'刘成刚\', \'男\', \'1991-06-07\', \'上海\', \'18015872567\', \'01\')')
cursor.execute('INSERT INTO s VALUES (\'1106\', \'李二丽\', \'女\', \'1993-05-04\', \'江苏\', \'18107620945\', \'01\')')
cursor.execute('INSERT INTO s VALUES (\'1107\', \'张晓峰\', \'男\', \'1992-08-16\', \'浙江\', \'13912341078\', \'01\')')


#创建课程表c表
cursor.execute('create table c (kh char(4) primary key, km char(20),'
                'xf integer,xs integer, yxh char(10))')
#插入数据
cursor.execute('insert into c values (\'08301001\', \'分子物理学\', \'4\', \'40\', \'03\')')
cursor.execute('insert into c values (\'08302001\', \'通信学\',  \'3\', \'30\', \'02\')')
cursor.execute('insert into c values (\'08305001\', \'离散数学\',  \'4\', \'40\', \'01\')')
cursor.execute('insert into c values (\'08305002\', \'数据库原理\',  \'4\', \'50\', \'01\')')
cursor.execute('insert into c values (\'08305003\', \'数据结构\', \'4\', \'50\', \'01\')')
cursor.execute('insert into c values (\'08305004\', \'系统结构\', \'6\', \'60\', \'01\')')



cursor.execute('create table d (yxh char(10) primary key, mc char(20),'
                'dz char(20),lxdh char(8))')
cursor.execute('insert into d values (\'01\', \'计算机学院\', \'上大东校区三号楼\', \'65347567\')')
cursor.execute('insert into d values (\'02\', \'通讯学院\', \'上大东校区二号楼\', \'65341234\')')



cursor.execute('create table e (xh int(4) not null, xq char(20),'
                'kh char(10),gh char(8),pscj int(11),kscj int(11),zpcj int(11))')

cursor.execute('insert into e values (\'1101\', \'2012-2013秋季\', \'08305001\', \'0103\', \'63\', \'60\', \'60\')')
cursor.execute('insert into e values (\'1102\', \'2012-2013秋季\', \'08305001\', \'0103\', \'90\', \'87\', \'87\')')
cursor.execute('insert into e values (\'1102\', \'2012-2013冬季\',\'08305002\', \'0101\', \'85\', \'82\', \'82\')')
cursor.execute('insert into e values (\'1102\', \'2013-2014秋季\', \'08305004\', \'0101\', null, null, null)')
cursor.execute('INSERT INTO e VALUES (\'1103\', \'2012-2013秋季\', \'08305001\', \'0103\', \'59\', \'56\', \'56\')')
cursor.execute('INSERT INTO e VALUES (\'1103\', \'2012-2013冬季\', \'08305002\', \'0102\', \'79\', \'75\', \'75\')')
cursor.execute('INSERT INTO e VALUES (\'1103\', \'2012-2013冬季\', \'08305003\', \'0102\', \'87\', \'84\', \'84\')')
cursor.execute('INSERT INTO e VALUES (\'1103\', \'2013-2014秋季\', \'08305001\', \'0102\', null, null, null)')
cursor.execute('INSERT INTO e VALUES (\'1103\', \'2013-2014秋季\', \'08305004\', \'0101\', null, null, null)')
cursor.execute('INSERT INTO e VALUES (\'1104\', \'2012-2013秋季\', \'08305001\', \'0103\', \'78\', \'74\', \'74\')')
cursor.execute('INSERT INTO e VALUES (\'1104\', \'2013-2014冬季\', \'08302001\', \'0201\', null, null, null)')
cursor.execute('INSERT INTO e VALUES (\'1106\', \'2012-2013秋季\', \'08305001\', \'0103\', \'88\', \'85\', \'85\')')
cursor.execute('INSERT INTO e VALUES (\'1106\', \'2012-2013冬季\', \'08305002\', \'0103\', \'69\', \'66\', \'66\')')
cursor.execute('INSERT INTO e VALUES (\'1107\', \'2012-2013秋季\', \'08305001\', \'0103\', \'94\', \'90\', \'90\')')
cursor.execute('INSERT INTO e VALUES (\'1107\', \'2012-2013冬季\', \'08305003\', \'0102\', \'82\', \'79\', \'79\')')
cursor.execute('INSERT INTO e VALUES (\'1107\', \'2013-2014秋季\', \'08305004\', \'0101\', null, null, null)')
cursor.execute('INSERT INTO e VALUES (\'1107\', \'2013-2014秋季\', \'08305004\', \'0101\', null, null, null)')
cursor.execute('INSERT INTO e VALUES (\'1107\', \'2012-2013冬季\', \'08305002\', \'0102\', null, null, null)')
cursor.execute('INSERT INTO e VALUES (\'1107\', \'2013-2014秋季\', \'08305004\', \'0101\', null, null, null)')
cursor.execute('INSERT INTO e VALUES (\'1107\', \'2012-2013冬季\', \'08305002\', \'0102\', null, null, null)')
cursor.execute('INSERT INTO e VALUES (\'1107\', \'2013-2014秋季\', \'08305004\', \'0101\', null, null, null)')


cursor.execute('create table o (xq char(20) , kh char(10),'
                'gh char(8),skcj char(10))')

cursor.execute('INSERT INTO o VALUES (\'2012-2013秋季\', \'08305001\', \'0103\', \'星期三5-8\')')
cursor.execute('INSERT INTO o VALUES (\'2012-2013冬季\', \'08305002\', \'0101\', \'星期三1-4\')')
cursor.execute('INSERT INTO o VALUES (\'2012-2013冬季\', \'08305002\', \'0102\', \'星期三1-4\')')
cursor.execute('INSERT INTO o VALUES (\'2012-2013冬季\', \'08305002\', \'0103\', \'星期三1-4\')')
cursor.execute('INSERT INTO o VALUES (\'2012-2013冬季\', \'08305003\', \'0102\', \'星期五5-8\')')
cursor.execute('INSERT INTO o VALUES (\'2013-2014秋季\', \'08305004\', \'0101\', \'星期二1-4\')')
cursor.execute('INSERT INTO o VALUES (\'2013-2014秋季\', \'08305001\', \'0102\', \'星期一5-8\')')
cursor.execute('INSERT INTO o VALUES (\'2013-2014冬季\', \'08302001\', \'0201\', \'星期一5-8\')')

# 创建教师表t表:
cursor.execute('create table t (gh char(8) primary key, xm char(8),'
               'xb char(2), csrq date, xl char(10), jbgz decimal(8,2), yxh char(10))')
#插入数据
cursor.execute('INSERT INTO t VALUES (\'0101\', \'陈迪茂\', \'男\', \'1973-03-06\', \'副教授\', \'3567.00\', \'01\')')
cursor.execute('INSERT INTO t VALUES (\'0102\', \'马小红\', \'女\', \'1972-12-08\', \'讲师\', \'2845.00\', \'01\')')
cursor.execute('INSERT INTO t VALUES (\'0103\', \'吴宝钢\', \'男\', \'1980-11-06\', \'讲师\', \'2554.00\', \'01\')')
cursor.execute('INSERT INTO t VALUES (\'0201\', \'张心颖\', \'女\', \'1960-01-05\', \'教授\', \'4200.00\', \'02\')')






'''
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

'''

cursor.close()
conn.commit()
conn.close()
