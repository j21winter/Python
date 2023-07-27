from flask import Flask, render_template, session, redirect, request

from user import User

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/read(all)')
def read_all():
    users = User.get_all()
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
    user_id = User.save(data)
    return redirect(f'/show/{user_id}')

@app.route('/show/<user_id>')
def show(user_id):
    user = User.get_one_by_id(user_id)
    return render_template('user_profile.html', user = user)

@app.route('/edit/<user_id>')
def edit_form(user_id):
    user = User.get_one_by_id(user_id)
    return render_template('edit_profile.html', user = user)

@app.route('/make_edits/<user_id>', methods={'POST'})
def make_edits(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    updated_user = User.update_user(data)
    return redirect(f'/show/{user_id}')

@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    User.delete_user(user_id)
    return redirect('/read(all)')

if __name__ == '__main__':
    app.run(debug=True)