# coding=utf-8
# 导入Flask库
from flask import Flask
from flask import request
from flask import render_template
import sqlite3

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
    if request.form['username'] == 'student' and request.form['password'] == 'password':
        return render_template('student_index.html')
    return render_template('teacher_index.html')

# 显示学生首页的函数，可以显示首页里的信息
@app.route('/student_index', methods=['GET'])
def student_index():
    return render_template('student_index.html')

# 显示教师首页的函数，可以显示首页里的信息
@app.route('/teacher_index', methods=['GET'])
def teacher_index():
    return render_template('teacher_index.html')









# 主函数
if __name__ == '__main__':
    app.debug = True
    app.run()
