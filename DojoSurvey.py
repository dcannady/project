from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    info = {"name": request.form['name'],
    "location": request.form['location'],
    "lang": request.form['lang'],
    "comment": request.form['comment']}
    len(info["name"])
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect ('/')
    return render_template('results.html', info = info)
app.run(debug = True)
