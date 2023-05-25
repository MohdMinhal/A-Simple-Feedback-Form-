from flask import Flask, render_template, request, url_for
import sqlite3

#flask configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

#Home page for the WebApp
@app.route('/')
def index():
    return render_template('home.html')

#page which takes the new visitor details and process it into database
@app.route("/submit",methods=['POST'])
def submit():
    if request.method == "POST":

        name = request.form['visitor_name']
        phone = request.form['visitor_phone']
        email = request.form['visitor_email']
        course = request.form['visitor_course']
        feedback = request.form['visitor_feedback']

        con = sqlite3.connect("info.db")
        cur = con.cursor()
        cur.execute("INSERT INTO visitor (Name, Phone, Email, Course, Feedback) VALUES (?,?,?,?,?)", (name,phone,email,course,feedback))
        con.commit()
        con.close()
        return render_template("success.html")
    else:
        return "<h1> Lol ... GET Method not allowed</h1>"


#run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
