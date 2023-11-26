# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Add your conversion logic here
    # Example: Retrieve units from the form and calculate the cost
    units = float(request.form['units'])
    cost = units * 0.12  # Replace with your own logic
    return render_template('result.html', units=units, cost=cost)

if __name__ == '__main__':
    app.run(debug=True)
