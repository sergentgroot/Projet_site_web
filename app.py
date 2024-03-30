from flask import Flask, render_template
app = Flask(__name__)

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/dessert')
def dessert():
    return render_template('dessert.html')



if __name__ == '__main__':
    app.run(debug=True)