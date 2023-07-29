from flask import Flask, render_template, session, redirect, request

from user import Users

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/read(all)')
def read_all():
    users = Users.get_all()
    return render_template('read(all).html', users = users)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'], 
        'email': request.form['email']
    }
    Users.save(data)
    return redirect('/read(all)')

if __name__ == '__main__':
    app.run(debug=True)