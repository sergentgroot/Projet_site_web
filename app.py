from flask import Flask, render_template
app = Flask(__name__)

from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/menu_page.html', methods=['GET', 'POST'])
def menu():
    return render_template('menu_page.html')

@app.route('/menu_page.html', methods=['GET', 'POST'])
def indexinmenu():
    return render_template('index.html')

@app.route('/dessert_page.html')
def dessert():
    return render_template('dessert_page.html')

@app.route('/burger_page.html')
def burger():
    return render_template('burger_page.html')

@app.route('/boisson_page.html')
def boisson():
    return render_template('boisson_page.html')




if __name__ == '__main__':
    app.run(debug=True)