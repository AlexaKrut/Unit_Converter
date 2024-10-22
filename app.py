from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/length')
def length():
    return render_template('length.html')

@app.route('/weight')
def weight():
    return render_template('weight.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')


if  __name__ == '__main__':
    app.run(port=5001, debug=True)
