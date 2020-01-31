# 主函数
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')

# 创建一个Cursor:
cursor = conn.cursor()


# 继续执行一条SQL语句，插入一条记录:

def create():
    cursor.execute('create table user_test (id varchar(20) primary key, name varchar(20))')


def insert():
    num = 22
    str = 'test'
    while num >= 12:
        '''
        sql = """
            INSERT INTO user_test(id,
             name)
             VALUES (?, ?),
             (num,str)
        """

        '''
        result = cursor.execute(
            ' INSERT INTO user_test(id,name) VALUES(?, ?)', (num, str)
        )
        num -= 1
        print("num = ", num, "result = ", result)


def select():
    table_name = 'user_test'
    num = '22'
    cursor.execute('select * from ? where id = ?', (table_name, num,))
    values = cursor.fetchall()
    print(values)


def show_info():
    # 通过rowcount获得插入的行数:
    print(cursor.rowcount)


if __name__ == '__main__':
    # create()
    insert()
    # select()

    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()