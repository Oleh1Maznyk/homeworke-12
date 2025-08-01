from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/countries')
def countries():
    places = [
        "Париж, Франція",
        "Кіото, Японія",
        "Мачу-Пікчу, Перу",
        "Кейптаун, ПАР",
        "Сідней, Австралія"
    ]
    return render_template('countries.html', places=places)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return redirect(url_for('index'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
