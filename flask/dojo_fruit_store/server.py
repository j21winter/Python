from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    today = datetime.now()
    date_time = today.strftime("%d/%m/%Y %H:%M:%S")
    order_total = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    
    print(f'\nCharging {request.form["first_name"]} for {order_total} fruits\n')
    return render_template("checkout.html", order_total = order_total, today=date_time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
