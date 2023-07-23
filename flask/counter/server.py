from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route ('/')
def home_page():
    if 'counter' and 'counter_2' not in session:
        session['counter'] = 0
        session['counter_2'] = 0
    else:
        session['counter'] += 1
        session['counter_2'] += 1
    return render_template('index.html')


@app.route('/add')
def add():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/form', methods=['POST'])
def add_form():
    session['counter'] += (int(request.form['input']) - 1)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)