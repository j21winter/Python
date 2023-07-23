from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html', row_num = 8, column_num = 8, color_1='black', color_2 = 'red')

@app.route('/<string:color_1>/<string:color_2>')
def colors(color_1,color_2):
    return render_template('index.html', row_num = 8 , column_num = 8, color_1 =color_1, color_2 = color_2)

@app.route('/<int:x>')
def size_y(x):
    return render_template('index.html', row_num = 8 , column_num = x, color_1 ='black', color_2 = 'red')

@app.route('/<int:x>/<int:y>')
def size_x_y(x,y):
    return render_template('index.html', row_num = y , column_num = x, color_1 ='black', color_2 = 'red')

@app.route('/<int:x>/<int:y>/<string:color_1>/<string:color_2>')
def color_and_size(x,y,color_1, color_2):
    return render_template('index.html', row_num = y , column_num = x, color_1 = color_1, color_2 = color_2)


if __name__=="__main__":
    app.run(debug=True) 