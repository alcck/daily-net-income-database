import sqlite3

def connect():
    conn = sqlite3.connect('netincome.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE netincome (Id INTEGER PRIMARY KEY, date text, earnings integer, groceries integer, entertainment integer, clothes integer, books integer)")
    conn.commit()
    conn.close()

connect()

def insert(date, earnings, groceries, entertainment, clothes, books):
    conn = sqlite3.connect('netincome.db')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO netincome VALUES (NULL,?,?,?,?,?)", (date, earnings, groceries, entertainment, clothes, books))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('netincome.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM netincome")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('netincome.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM netincome WHERE id=?",(id,))
    conn.commit()
    conn.close()

def search(date='', earnings='', groceries, entertainment, clothes, books):
    conn = sqlite3.connect('netincome.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM netincome")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


insert("1-2-2023,800,100,60,0,50")