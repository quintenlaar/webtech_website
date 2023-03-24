from flask import Flask, render_template, flash, url_for, session, request, redirect, g
import sqlite3


# connecting flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "qwertiorejpowiinfsdjbv"

def connect_db():
    return sqlite3.connect("eten.sqlite")

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exeception):
    if hasattr(g, 'db'):
        g.db.close()

# main page
@app.route('/')
def index():
    return render_template("index.html")

# login page
@app.route('/login')
def login():
    return render_template('inlog.html')

# Adding to the database
@app.route('/database', methods=['post'])
def database():

    cursor = g.db.cursor()

    # email en wachtwoord aanvragen
    email = request.form.get('E-mailaddress')
    wachtwoord = request.form.get('Password')

    cursor.execute("INSERT INTO login (mail, wachtwoord) values (?, ?)", (email, wachtwoord))
    g.db.commit()

    cursor.execute("SELECT * FROM login;")
    for row in cursor:
        print(row)

    cursor.execute("DELETE FROM login WHERE mail=?", (email,))
    g.db.commit()

    return redirect(url_for("gelukt"))

@app.route('/gelukt')
def gelukt():
    return render_template("gelukt.html")
    

if __name__ == "__main__":
    app.run(debug=True)

