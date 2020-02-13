import sqlite3

def connect():
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    cur_obj.close()
    conn.commit()
    conn.close()

def insert(table_name, insert_arr):
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    if table_name == 's':
        # (sno, sname, sex, age, sdept, logn, pswd)
        cur_obj.execute("INSERT INTO s "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, 0)", (insert_arr[0], insert_arr[1], insert_arr[2], insert_arr[3], insert_arr[4], insert_arr[5], insert_arr[6]))
    elif table_name == 'c':
        # (cno, cname, credit, cdept,tname)
        cur_obj.execute("INSERT INTO c "
                        "VALUES (?, ?, ?, ?, ?)", (insert_arr[0], insert_arr[1], insert_arr[2], insert_arr[3],insert_arr[4]))
    elif table_name == 'sc':
        # (sno, cno, grade)
        cur_obj.execute("INSERT INTO sc "
                        "VALUES (?, ?, ?)", (insert_arr[0], insert_arr[1], insert_arr[2]))
    elif table_name == 'nsc':
        # (sno, cno, tag)
        cur_obj.execute("INSERT INTO nsc "
                        "VALUES (?, ?, ?)", (insert_arr[0], insert_arr[1], insert_arr[2]))
    cur_obj.close()
    conn.commit()
    conn.close()

def get_all(table_name):
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    # 缺省查询报错，只能枚举
    if table_name == 's':
        cur_obj.execute("SELECT * FROM s")
    elif table_name == 'c':
        cur_obj.execute("SELECT * FROM c")
    elif table_name == 'sc':
        cur_obj.execute("SELECT * FROM sc")
    elif table_name == 'nsc':
        cur_obj.execute("SELECT * FROM nsc")
    table = cur_obj.fetchall()
    cur_obj.close()
    conn.close()
    return table

def update(table_name,update_arr):
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    if table_name == 's':
        # (sno, sname, sex, age, sdept, logn, pswd)
        cur_obj.execute("UPDATE s "
                        "SET sno = ?, "
                        "sname = ?, "
                        "sex = ?, "
                        "age = ?, "
                        "sdept = ?, "
                        "logn = ?, "
                        "pswd = ?,"
                        "count = ?"
                        "WHERE sno = ?",
                        (update_arr[0], update_arr[1], update_arr[2], update_arr[3], update_arr[4], update_arr[5], update_arr[6],update_arr[7],update_arr[0]))
    elif table_name == 'c':
        # (cno, cname, credit, cdept,tname)
        cur_obj.execute("UPDATE c "
                        "SET cno = ?, "
                        "cname = ?, "
                        "credit = ?, "
                        "cdept = ?, "
                        "tname = ? "
                        "WHERE cno = ?",
                        (update_arr[0], update_arr[1], update_arr[2], update_arr[3], update_arr[4],update_arr[0]))
    elif table_name == 'sc':
        # (sno, cno, grade)
        cur_obj.execute("UPDATE sc "
                        "SET sno = ?, "
                        "cno = ?, "
                        "grade = ? "
                        "WHERE sno = ?AND cno = ?",
                        (update_arr[0], update_arr[1], update_arr[2],update_arr[0],update_arr[1]))
    elif table_name == 'nsc':
        # (sno, cno, tag)
        cur_obj.execute("UPDATE nsc "
                        "SET sno = ?, "
                        "cno = ?, "
                        "tag = ? "
                        "WHERE sno =? AND cno = ?",
                        (update_arr[0], update_arr[1], update_arr[2], update_arr[0], update_arr[1]))
    cur_obj.close()
    conn.commit()
    conn.close()

def delete(table_name,num):
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    if table_name == 's':
        cur_obj.execute("DELETE FROM s "
                        "WHERE sno = ?", (num,))
    elif table_name == 'c':
        cur_obj.execute("DELETE FROM c "
                        "WHERE cno = ?", (num,))
    elif table_name == 'sc':
        cur_obj.execute("DELETE FROM sc "
                        "WHERE sno = ?", (num,))
    elif table_name == 'nsc':
        cur_obj.execute("DELETE FROM nsc "
                        "WHERE sno = ?", (num,))
    cur_obj.close()
    conn.commit()
    conn.close()

def search(table_name,arr1="",arr2="",arr3="",arr4="",arr5="",arr6=""):
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    if table_name == 's':
        # (sno, sname, sex, age, sdept, logn, pswd)
        cur_obj.execute("SELECT * "
                        "FROM s "
                        "WHERE sno = ? OR sname = ? OR sex = ? OR age = ? OR sdept = ? OR logn =?",
                        (arr1, arr2, arr3, arr4, arr5,arr6))
    elif table_name == 'c':
        # (cno, cname, credit, cdept,tname)
        cur_obj.execute("SELECT * "
                        "FROM c "
                        "WHERE cno = ? OR cname = ? OR credit = ? OR cdept = ? or tname = ?",
                        (arr1, arr2, arr3, arr4, arr5))
    elif table_name == 'sc':
        # (sno, cno, grade)
        cur_obj.execute("SELECT * "
                        "FROM sc "
                        "WHERE sno = ? OR cno = ? OR grade = ?",
                        (arr1, arr2, arr3))
    elif table_name == 'nsc':
        # (sno, cno, tag)
        cur_obj.execute("SELECT * "
                        "FROM nsc "
                        "WHERE sno = ? OR cno = ? OR tag = ?",
                        (arr1, arr2, arr3))
    search_info = cur_obj.fetchall()
    cur_obj.close()
    conn.close()
    return search_info

def nsc_search(arr1,arr2):
    conn = sqlite3.connect("student2.db")
    cur_obj = conn.cursor()
    cur_obj.execute("SELECT * "
                    "FROM nsc "
                    "WHERE sno = ? AND tag = ?",
                    (arr1, arr2))
    search_info = cur_obj.fetchall()
    cur_obj.close()
    conn.close()
    return search_info

