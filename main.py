from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/training/<prof>')
def index(prof):
    return render_template('page.html', title='Домашняя страница',
                           prof=prof)


app.run(port=8080, host='127.0.0.1')
