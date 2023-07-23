from flask import Flask, render_template, redirect, session, request
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'Secret'

position = 0

def generate_randint():
    random_num = random.randint(0,100)
    print(random_num)
    return random_num

@app.route('/')
def home():
    if 'random_num' and 'guess' and 'count' and 'leaderboard' not in session:
        session['random_num'] = generate_randint()
        session['guess'] = 0
        session['count'] = 0
        session['leaderboard'] = []
    print(session)
    return render_template('index.html', random_num = session['random_num'], guess=session['guess'], count = session['count'])

@app.route('/restart')
def restart():
    session.clear()
    return redirect ('/')

@app.route('/guess', methods=['POST'])
def my_guess():
    session['guess'] = int(request.form['guess'])
    session['count'] += 1
    return redirect('/')

@app.route('/high_score', methods=['POST'])
def leaderboard():
    name = request.form['name']
    count = session['count']
    random_num = session['random_num']
    date = datetime.now()
    date = date.strftime('%d/%m/%Y')
    session['leaderboard'].append({name,count,random_num, date})
    print(session)
    return render_template('leaderboard.html', name=name, count=count, random_num = random_num, date=date, position=position)

# Leaderboard could have a class for each row of the leaderboard. I could iterate the class and potentially add it to the session so that the leaderboard is more permanent?? I would image that connecting that leaderboard to a database would be the most effective way to make that happen and to order the leaderboard with new additions to the leaderboard.


if __name__ == '__main__':
    app.run(debug=True)