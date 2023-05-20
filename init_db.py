import psycopg2

conn = psycopg2.connect(database="postgres", host="postgres-server", user="postgres", password="1234", port="5432")
cur = conn.cursor()

cur.execute("CREATE DATABASE flask_db")
cur.execute('''CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY, name varchar(100), fees integer, 
duration integer);''')
cur.execute('''INSERT INTO courses (name, fees,duration) VALUES ('python',6500,45),('Java', 7000,60),('Javascript',
6000,30);''')

conn.commit()
cur.close()
conn.close()
