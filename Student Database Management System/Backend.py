import sqlite3

def stdData():
    con = sqlite3.connect("database.db")
    con.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text, DateOfBirth text, \
                Age text, Gender text, Address text, Mobile_no text)")
    con.commit()
    con.close()

stdData()

def addstdRec(StdID , Firstname , Surname , DateOfBirth , Age , Gender , Address , Mobile_no):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?)",(StdID , Firstname , Surname , DateOfBirth , Age , Gender , Address , Mobile_no))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def delRec(id):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(StdID = "", Firstname = "", Surname = "", DateOfBirth ="", Age ="", Gender ="", Address ="", Mobile_no=""):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID = ? OR Firstname = ? OR Surname = ? OR DateOfBirth =? OR Age =? OR Gender =? OR \
                Address =? OR Mobile_no=?", (StdID , Firstname , Surname , DateOfBirth , Age , Gender , Address , Mobile_no))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows