import sqlite3

def connect():
    conn = sqlite3.connect("management.db")
    cur_obj = conn.cursor()
    cur_obj.close()
    conn.commit()
    conn.close()

def insert(table_name, insert_arr):
    conn = sqlite3.connect("management.db")
    cur_obj = conn.cursor()
    if table_name == 's':
        # (xh, xm, xb, csrq, jg, sjhm, yxh)
        cur_obj.execute("INSERT INTO s "
                        "VALUES (?, ?, ?, ?, ?, ?, ?)", (insert_arr[0], insert_arr[1], insert_arr[2], insert_arr[3], insert_arr[4], insert_arr[5], insert_arr[6]))
    elif table_name == 'c':
        # (kh, km, xf, xs,yxh)
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
    elif table_name == 'd':
        # (yxh, mc, dz,lxdh)
        cur_obj.execute("INSERT INTO d "
                        "VALUES (?, ?, ?, ?)", (insert_arr[0], insert_arr[1], insert_arr[2], insert_arr[3]))

    elif table_name == 'e':
        # (xh, xq, kh, gh, pscj, kscj, zpcj)
        cur_obj.execute("INSERT INTO e "
                        "VALUES (?, ?, ?, ?, ?, ?, ?)", (insert_arr[0], insert_arr[1], insert_arr[2], insert_arr[3], insert_arr[4], insert_arr[5],insert_arr[6]))
    elif table_name == 'o':
        # (xq, kh, gh, sksj)
        cur_obj.execute("INSERT INTO o "
                        "VALUES (?, ?, ?, ?)", (insert_arr[0], insert_arr[1], insert_arr[2], insert_arr[3]))
    elif table_name == 't':
        # gh,xm,xb,csrq,xl,jbgz,yxh
        cur_obj.execute("INSERT INTO t "
                        "VALUES (?, ?, ?, ?, ?, ?, ?)", (
                        insert_arr[0], insert_arr[1], insert_arr[2], insert_arr[3], insert_arr[4], insert_arr[5],
                        insert_arr[6]))
    cur_obj.close()
    conn.commit()
    conn.close()

def get_all(table_name):
    conn = sqlite3.connect("management.db")
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
    elif table_name == 'o':
        cur_obj.execute("SELECT * FROM o")
    elif table_name == 't':
        cur_obj.execute("SELECT * FROM t")
    elif table_name == 'e':
        cur_obj.execute("SELECT * FROM e")
    elif table_name == 'd':
        cur_obj.execute("SELECT * FROM d")
    table = cur_obj.fetchall()
    cur_obj.close()
    conn.close()
    return table

def update(table_name,update_arr):
    conn = sqlite3.connect("management.db")
    cur_obj = conn.cursor()
    if table_name == 's':
        # (xh, xm, xb, csrq, jg, sjhm, yxh)
        cur_obj.execute("UPDATE s "
                        "SET xh = ?, "
                        "xm = ?, "
                        "xb = ?, "
                        "csrq = ?, "
                        "jg = ?, "
                        "sjhm = ?, "
                        "yxh = ?"
                        "WHERE xh = ?",
                        (update_arr[0], update_arr[1], update_arr[2], update_arr[3], update_arr[4], update_arr[5], update_arr[6],update_arr[0]))
    elif table_name == 'c':
        # (kh, km, xf, xs,yxh)
        cur_obj.execute("UPDATE c "
                        "SET kh = ?, "
                        "km = ?, "
                        "xf = ?, "
                        "xs = ?, "
                        "yxh = ? "
                        "WHERE kh = ?",
                        (update_arr[0], update_arr[1], update_arr[2], update_arr[3], update_arr[4],update_arr[0]))
    elif table_name == 'd':
        # (yxh, mc, dz,lxdh)
        cur_obj.execute("UPDATE d "
                        "SET yxh = ?, "
                        "mc = ?, "
                        "dz = ?, "
                        "lxdh = ?"
                        "WHERE yxh = ?",
                        (update_arr[0], update_arr[1], update_arr[2], update_arr[3], update_arr[0]))
    elif table_name == 'e':
        # (xh, xq, kh, gh, pscj, kscj, zpcj)
        cur_obj.execute("UPDATE e "
                        "SET xh = ?, "
                        "xq = ?, "
                        "kh = ?, "
                        "gh = ?, "
                        "pscj = ?, "
                        "kscj = ?, "
                        "zpcj = ?"
                        "WHERE xh = ? and kh = ?",
                        (update_arr[0], update_arr[1], update_arr[2], update_arr[3], update_arr[4], update_arr[5],
                         update_arr[6], update_arr[0], update_arr[2]))
    elif table_name == 'o':
        # (xq, kh, gh, sksj)
        cur_obj.execute("UPDATE o "
                        "SET xq = ?, "
                        "kh = ?, "
                        "gh = ?, "
                        "sksj = ? "
                        "WHERE kh = ? and kh = ? and gh = ?",
                        (update_arr[0], update_arr[1], update_arr[2], update_arr[3], update_arr[0], update_arr[1], update_arr[2]))
    elif table_name == 't':
        # gh,xm,xb,csrq,xl,jbgz,yxh
        cur_obj.execute("UPDATE t "
                        "SET gh = ?, "
                        "xm = ?, "
                        "xb = ?, "
                        "csrq = ?, "
                        "xl = ?, "
                        "jbgz = ?, "
                        "yxh = ?"
                        "WHERE gh = ?",
                        (update_arr[0], update_arr[1], update_arr[2], update_arr[3], update_arr[4], update_arr[5],
                         update_arr[6], update_arr[0]))
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
    conn = sqlite3.connect("management.db")
    cur_obj = conn.cursor()
    if table_name == 's':
        cur_obj.execute("DELETE FROM s "
                        "WHERE xh = ?", (num,))
    elif table_name == 'c':
        '''
        cur_obj.execute("DELETE FROM c "
                        "WHERE cno = ?", (num,))
        '''
    elif table_name == 'o':
        '''
        cur_obj.execute("DELETE FROM o "
                        "WHERE kh = ? and gh = ?", (num,))
        '''
    elif table_name == 't':
        cur_obj.execute("DELETE FROM t "
                        "WHERE gh = ?", (num,))
    elif table_name == 'e':
        '''
        cur_obj.execute("DELETE FROM o "
                        "WHERE kh = ? and gh = ?", (num,))
        '''
    elif table_name == 'd':
        cur_obj.execute("DELETE FROM d "
                        "WHERE yxh = ?", (num,))

    elif table_name == 'sc':
        cur_obj.execute("DELETE FROM sc "
                        "WHERE sno = ?", (num,))
    elif table_name == 'nsc':
        cur_obj.execute("DELETE FROM nsc "
                        "WHERE sno = ?", (num,))
    cur_obj.close()
    conn.commit()
    conn.close()

def search(table_name,arr1="",arr2="",arr3="",arr4="",arr5="",arr6="",arr7=""):
    conn = sqlite3.connect("management.db")
    cur_obj = conn.cursor()
    if table_name == 's':
        # (xh, xm, xb, csrq, jg, sjhm, yxh)
        cur_obj.execute("SELECT * "
                        "FROM s "
                        "WHERE xh = ? OR xm = ? OR xb = ? OR csrq = ? OR jg = ? OR sjhm =? or yxh = ?",
                        (arr1, arr2, arr3, arr4, arr5,arr6,arr7))
    elif table_name == 'c':
        # (kh, km, xf, xs,yxh)
        cur_obj.execute("SELECT * "
                        "FROM c "
                        "WHERE kh = ? OR km = ? OR xf = ? OR xs = ? or yxh = ?",
                        (arr1, arr2, arr3, arr4, arr5))
    elif table_name == 'd':
        # (yxh, mc, dz,lxdh)
        cur_obj.execute("SELECT * "
                    "FROM d "
                    "WHERE yxh = ? OR mc = ? OR dz = ? OR lxdh = ?",
                    (arr1, arr2, arr3, arr4))
    elif table_name == 'o':
        # (xq, kh, gh, sksj)
        cur_obj.execute("SELECT * "
                    "FROM o "
                    "WHERE xq = ? OR kh = ? OR gh = ? OR sksj = ?",
                    (arr1, arr2, arr3, arr4))
    elif table_name == 'e':
        # (xh, xq, kh, gh, pscj, kscj, zpcj)
        cur_obj.execute("SELECT * "
                        "FROM e "
                        "WHERE xh = ? OR xq = ? OR kh = ? OR gh = ? OR pscj = ? OR kscj =? or zpcj = ?",
                        (arr1, arr2, arr3, arr4, arr5,arr6,arr7))
    elif table_name == 't':
        # gh,xm,xb,csrq,xl,jbgz,yxh
        cur_obj.execute("SELECT * "
                        "FROM t "
                        "WHERE gh = ? OR xm = ? OR xb = ? OR csrq = ? OR xl = ? OR jbgz =? or yxh = ?",
                        (arr1, arr2, arr3, arr4, arr5, arr6, arr7))
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
    conn = sqlite3.connect("management.db")
    cur_obj = conn.cursor()
    cur_obj.execute("SELECT * "
                    "FROM nsc "
                    "WHERE sno = ? AND tag = ?",
                    (arr1, arr2))
    search_info = cur_obj.fetchall()
    cur_obj.close()
    conn.close()
    return search_info
