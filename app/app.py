# coding=utf-8
# 导入Flask库
from flask import Flask
from flask import request
from flask import render_template
import sqlite3
import db_crub as dbs

app = Flask(__name__)

'''
@app.route('/')
def home():
    return render_template('home.html')
'''

@app.route('/',methods=['GET', 'POST'])
def home():
    # 默认的页面
    return render_template('login.html')

# 对登录的用户名和密码进行判断
@app.route('/login', methods=['POST'])
def login():
    # 需要从request对象读取表单内容：
    # 有三种不同的结果
    if request.form['username'] == 'student' and request.form['password'] == 'password':
        return render_template('student_index.html')
    elif request.form['username'] == 'admin' and request.form['password'] == 'password':
        return render_template('admin_index.html')
    return render_template('teacher_index.html')

# 显示学生首页的函数，可以显示首页里的信息
@app.route('/student_index', methods=['GET'])
def student_index():
    return render_template('student_index.html')

# 显示教师首页的函数，可以显示首页里的信息
@app.route('/teacher_index', methods=['GET'])
def teacher_index():
    return render_template('teacher_index.html')

# 显示教师首页的函数，可以显示首页里的信息
@app.route('/admin_index', methods=['GET'])
def teacher_index():
    return render_template('admin_index.html')

# 学生---通过这个页面学生可以看到所有课程
@app.route('/getcourse', methods=['GET'])
def get_course():
    # 调用显示一个table所有数据的函数
    data = dbs.get_all('c')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        posts.append(dict_data)
    # print posts
    return render_template('student.html', posts=posts)

@app.route('/selectcourse', methods=['GET','POST'])
def select_course():
    # 需要从request对象读取表单内容：
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    insert_array = [student_id,course_id,0]
    # 选课表，学生初试成绩为 0 之后老师可以修改
    dbs.insert('sc',insert_array)

    data = dbs.get_all('sc')
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        posts.append(dict_data)
    return render_template('student.html', posts=posts)

@app.route('/deletecourse', methods=['GET','POST'])
def delete_course():
    # 需要从request对象读取表单内容：
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    # 这里暂时这么写，因为我发现之前的语句设计有问题，这里不能通过学号唯一确定一个选课记录
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    cur_obj.execute("DELETE FROM sc WHERE sno = ?,cno = ?", (student_id,course_id))
    cur_obj.close()
    conn.commit()
    conn.close()
    # 数据库用完随手关上
    data = dbs.get_all('sc')
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        posts.append(dict_data)
    return render_template('student.html', posts=posts)

@app.route('/getmytable', methods=['GET','POST'])
def get_my_course_table():
    # 这里是看自己的课表，那么就要用两个表一个sc和一个c
    # 需要从request对象读取表单内容：
    student_id = request.form['student_id']
    # 这里暂时这么写，还没有写好封装
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    cur_obj.execute("SELECT * FROM c WHERE cno in (select cno from sc where sno = ?)", (student_id,))
    data = cur_obj.fetchall()
    cur_obj.close()
    conn.commit()
    conn.close()
    # 数据库用完随手关上
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        posts.append(dict_data)
    return render_template('student.html', posts=posts)

@app.route('/managestudent', methods=['POST'])
def manage_student():
    # 需要从request对象读取表单内容：
    # (sno, sname, sex, age, sdept, logn, pswd)
    student_id = request.form['sno']
    student_name = request.form['sname']
    sex = request.form['sex']
    age = request.form['age']
    department = request.form['sdept']
    insert_array = [student_id,student_name,sex,age,department,student_id,student_id]
    # 学生的账号和密码默认是学号
    dbs.insert('s',insert_array)




# 主函数
if __name__ == '__main__':
    app.debug = True
    app.run()
