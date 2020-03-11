#成绩分布
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import sqlite3
import random
import numpy as np

class FForm:
    def __init__(self):
        self.root = tk.Tk()  # 创建主窗体
        self.root.geometry('1200x600')
        self.canvas = tk.Canvas()  # 创建一块显示图形的画布
        self.figure = self.ddraw()  # 返回matplotlib所画图形的figure对象
        self.create_form(self.figure)  # 将figure显示在tkinter窗体上面
        self.root.mainloop()

    def ddraw(self):
        conn = sqlite3.connect('student2.db')  # 若文件不存在，会自动在当前目录创建
        cursor = conn.cursor()  # 创建一个cursor
        # 计算课程及其平均分
        cursor.execute('select cname,avg(grade) from sc,c where c.cno=sc.cno group by sc.cno')
        result = cursor.fetchall()
        print(result)
        avg_grade_list = [x[1] for x in result]
        cname_list = [x[0] for x in result]

        print(avg_grade_list)
        print(cname_list)

        # 中文乱码和坐标轴负号处理。
        plt.rc('font', family='SimHei', weight='bold')
        plt.rcParams['axes.unicode_minus'] = False
        # 数组反转
        #cname_list.reverse()

        '''#随机生成颜色
        def randomcolor():
            colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            color = ""
            for i in range(6):
                color += colorArr[random.randint(0,14)]
            return "#"+color

        colors=[]
        for i in range(len(cname_list)):
            colors += ''.join(randomcolor())'''

        # 绘图
        fig, ax = plt.subplots()
        b = ax.barh(range(len(cname_list)), avg_grade_list, height=0.3, color='#6699CC')

        # 为横向水平的柱图右侧添加数据标签
        for x in b:
            w = x.get_width()
            ax.text(w, x.get_y() + x.get_height() / 2, '%.1f' % float(w), ha='left', va='center')

        # 设置Y轴纵坐标上的刻度线标签
        ax.set_yticks(range(len(cname_list)))
        ax.set_yticklabels(cname_list, fontsize='10', fontweight='bold')

        # 不要x横坐标上的label标签
        # plt.xticks(())
        plt.xlabel(u"平均成绩", fontsize='12', fontweight='bold')
        plt.ylabel(u"课程名称", fontsize='12', fontweight='bold')
        plt.title('成绩分布', loc='center', fontsize='20', fontweight='bold', color='black')

        #plt.show()
        return fig

    def create_form(self, figure):
        # 把绘制的图形显示到tkinter窗口上
        self.canvas = FigureCanvasTkAgg(figure, self.root)
        self.canvas.draw()  # 以前的版本使用show()方法，matplotlib 2.2之后不再推荐show（）用draw代替，但是用show不会报错，会显示警告
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        # 把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        #toolbar = NavigationToolbar2Tk(self.canvas,self.root)  # matplotlib 2.2版本之后推荐使用NavigationToolbar2Tk，若使用NavigationToolbar2TkAgg会警告
        #toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    form = FForm()

#待改进：
# 1.条形图的颜色要不同
# 2.把图片变小

















