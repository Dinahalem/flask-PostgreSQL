import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')

conn = psycopg2.connect(database="flask_db", host=POSTGRES_HOST, user=POSTGRES_USER, password=POSTGRES_PASSWORD,
                        port=5432)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY, name varchar(100), fees integer, 
duration integer);''')
cur.execute('''INSERT INTO courses (name, fees,duration) VALUES ('python',6500,45),('Java', 7000,60),('Javascript',
6000,30);''')

conn.commit()
cur.close()
conn.close()
