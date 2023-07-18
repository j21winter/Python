from flask import Flask
app = Flask(__name__)
route_list  = ['/','/dojo','/say/<string:name>', '/repeat/<int:num>/<string:word>']

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def print_dojo():
    return 'DOJO!'

@app.route('/say/<string:name>')
def say(name):
    return (f'Hi {name.capitalize()}')

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    return (f'\n{word}') * num

@app.route('/<input>/')
def check_URL(input):
    for route in route_list:
        if input not in route_list:
            return 'Sorry! No response. Try again'
    else:
        return input

if __name__ == "__main__":
    app.run(debug=True)