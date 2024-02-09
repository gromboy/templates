from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('page.html', title='Домашняя страница',
                           username=user)


app.run(port=8080, host='127.0.0.1')
