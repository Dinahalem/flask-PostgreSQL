import psycopg2
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv()
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')


def db_conn():
    conn = psycopg2.connect(database="flask_db", host=POSTGRES_HOST, user=POSTGRES_USER, password=POSTGRES_PASSWORD,
                            port=5432)
    return conn


@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM courses ORDER BY id''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=data)


@app.route('/create', methods=['POST'])
def create():
    conn = db_conn()
    cur = conn.cursor()
    name = request.form['name']
    fees = request.form['fees']
    duration = request.form['duration']
    cur.execute('''INSERT INTO courses (name,fees,duration) VALUES(%s,%s,%s)''', (name, fees, duration))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/update', methods=['POST'])
def update():
    conn = db_conn()
    cur = conn.cursor()

    name = request.form['name']
    fees = request.form['fees']
    duration = request.form['duration']
    id = request.form['id']

    cur.execute('''UPDATE courses SET name=%s,fees=%s, duration=%s WHERE id=%s''', (name, fees, duration, id))
    conn.commit()

    return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete():
    conn = db_conn()
    cur = conn.cursor()

    id = request.form['id']

    cur.execute('''DELETE FROM courses WHERE id=%s''', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
