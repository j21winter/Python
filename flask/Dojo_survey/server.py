from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/result')
def results():
    return render_template('result.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['courses'] = request.form.getlist('courses')
    session['comments'] = request.form['comments']
    print(session)
    return redirect('/result')

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)