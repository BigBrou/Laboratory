import sqlite3

filepath = 'test2.sqlite'
conn = sqlite3.connect(filepath)

cur = conn.cursor()
cur.executescript("""
    DROP TABLE IF EXISTS ITEMS;

    CREATE TABLE ITEMS(
        ITEM_ID INTEGER PRIMARY KEY,
        NAME    VARCHAR(100) UNIQUE,
        PRICE   INTEGER
    );
""")
conn.commit()

cur = conn.cursor()
cur.execute("""
    INSERT INTO ITEMS
        (NAME, PRICE)
    VALUES
        (?,?)
""", ("FiveMoreHours", 5200))
conn.commit()
print("Commit Executed #1")

cur = conn.cursor()
data = [
    ("Mango"    , 7700),
    ("Kiwi"     , 500),
    ("Persimmon", 300),
    ("Bananaw"  , 400)
]
cur.executemany("INSERT INTO ITEMS (NAME, PRICE) VALUES (?,?)", (data))
conn.commit()
print("Commit Executed #2")

cur = conn.cursor()
price_range = (4000, 7000)
cur.execute(
    "SELECT * FROM ITEMS WHERE PRICE >= ? AND PRICE <= ?",
    price_range
)
print("Commit Executed #3")

fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)
