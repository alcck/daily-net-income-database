import sqlite3


def connect():
    conn = sqlite3.connect('netincome.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS netincome (Id INTEGER PRIMARY KEY, date text, earnings integer, groceries "
        "integer, entertainment integer, clothes integer, books integer)")
    conn.commit()
    conn.close()


def insert(date, earnings, groceries, entertainment, clothes, books):
    conn = sqlite3.connect('netincome.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO netincome VALUES (NULL,?,?,?,?,?,?)",
                (date, earnings, groceries, entertainment, clothes, books))
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


def delete(idx):
    conn = sqlite3.connect('netincome.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM netincome WHERE id=?", (idx,))
    conn.commit()
    conn.close()


def search(date='', earnings='', groceries='', entertainment='', clothes='', books=''):
    conn = sqlite3.connect('netincome.db')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM netincome WHERE date=? OR earnings=? OR groceries=? OR entertainment=? OR clothes=? OR books=?",
        (date, earnings, groceries, entertainment, clothes, books))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# connect()
