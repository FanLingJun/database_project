'''学生成绩单'''
import tkinter as tk
from tkinter import scrolledtext
from tkinter import Spinbox

w3=tk.Tk()
w3.title('学生成绩单')
w3.geometry('800x400')


for r in range(3):
    for c in range(3):
        t1=tk.Text(w3,width=10,height=2)
        t1.grid(row=r,column=c)

w3.mainloop()



