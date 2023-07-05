import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host='localhost',
    dbname='library',
    user='user1',
    password='1111',
)

cur = conn.cursor()

# 테이블 생성
# cur.execute('''
# CREATE TABLE test_table (
# id SERIAL PRIMARY KEY,
# name VARCHAR(50))
# ''')
# conn.commit()

cur.execute('SELECT * FROM test_table')
rows =cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
