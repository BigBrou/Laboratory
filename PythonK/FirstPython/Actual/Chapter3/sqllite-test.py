import sqlite3

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
cur.executescript("""
    DROP TABLE IF EXISTS ITEMS;

    CREATE TABLE ITEMS(
        ITEM_ID INTEGER PRIMARY KEY,
        NAME    VARCHAR(100) UNIQUE,
        PRICE   INTEGER
    );

    INSERT INTO ITEMS
        (NAME, PRICE)
    VALUES
        ('Apple', 800),
        ('Banana', 1000),
        ('Oranger', 5000);
""")

conn.commit()

cur = conn.cursor()
cur.execute("SELECT ITEM_ID, NAME, PRICE FROM ITEMS")

item_list = cur.fetchall()
for it in item_list:
    print(it)
