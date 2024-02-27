from flask import Flask, request, redirect
import psycopg2
import os

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = psycopg2.connect(
        dbname=os.environ['POSTGRES_DB'],
	user=os.environ['POSTGRES_USER'],
	password=os.environ['POSTGRES_PASSWORD'],
        host='db'
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    account = cur.fetchone()
    cur.close()
    conn.close()
    if account:
        return redirect('/welcome.html', code=302)
    else:
        return 'Login failed', 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
