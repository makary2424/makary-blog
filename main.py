from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "sadfjkls jfkjaskl jf"

@app.route("/")
def index():
    print(session.get('user'))
    con = sqlite3.connect("data_base.db")
    con.row_factory = sqlite3.Row
    articles = con.execute("select id, title, text from articles").fetchall()
    return render_template("index.html", articles=articles)

@app.route("/create", methods=["Post", "Get"])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form["text"]
        if title and text:
            connect = sqlite3.connect("data_base.db")
            connect.execute("insert into articles (title, text) values (?, ?)", [title, text])
            connect.commit()
            return redirect("/")
    return render_template("create.html")
@app.errorhandler(404)
def not_found(e):
    return redirect('/')

@app.route("/create2", methods=["Get", "Post"])
def create2():
    if request.method == 'POST':
        title = request.form['title']
        print(title)
        text = request.form["text"]
        print(text)
        if title and text:
            connect2 = sqlite3.connect("data_base.db")
            connect2.execute("insert into articles (title, text) values (?, ?)", [title, text])
            connect2.commit()
    return render_template("create2.html")

@app.route('/delete/<int:id>')
def delete(id):
    connect = sqlite3.connect('data_base.db')
    connect.execute(f"delete from articles where id = {id}")
    connect.commit()
    return redirect("/")
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form['user_name']
        session['user'] = user_name
        return redirect("/")
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)


