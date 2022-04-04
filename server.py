from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key="force is with you"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/the_form', methods=['POST'])
def the_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')


@app.route('/results')
def results():
    return render_template("results.html")

if __name__=="__main__":
    app.run(debug=True)