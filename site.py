from flask import Flask, render_template, request, redirect, url_for, make_response
import sqlite3

app = Flask(__name__)
DATABASE = 'BAZA_ZOV.db'

def init_db():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute(
''' CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT
    )
  ''')
  conn.commit()
  conn.close()

init_db()

@app.route('/')

def home():
  return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])

def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
  
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
  
    if user:
      resp = make_response(redirect(url_for('welcome')))
      resp.set_cookie('username', username)
      return resp
    return "Wrong creds!"

@app.route('/welcome')

def welcome():
  username = request.cookies.get('username')
  if not username:
    return redirect(url_for('login'))
  return f"<h1> HELLO BRATANCHIK {username}!</h1>"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
