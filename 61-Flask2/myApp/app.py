import os

from flask import Flask, render_template, request

from scr.articles import articles
from scr.forms.article_form import ArticleForm

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        autorius = request.form['autorius']
        tekstas = request.form['tekstas']
        pavadinimas = request.form['pavadinimas']
        articles.append({
            'data': date,
            'autorius': autorius,
            'pavadinimas': pavadinimas,
            'tekstas': tekstas,
            'status': 'published'
        })
    return render_template('index.html', data=articles)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<string:title>')  # parametruose nurodomas kintamasis (title) ir jo tipas (string)
def article(title):  # kintam1jį būtinai nurodykite ir funkcijos parametruose
    return render_template('article.html', title=title,
                           data=articles)  # taip pat ir čia reikia jį perduoti


@app.route('/add-article')
def add_article():
    return render_template('add_article.html')


@app.route('/add-article/wtf', methods=['GET', 'POST'])
def add_article_wtf():
    form = ArticleForm()
    if form.validate_on_submit():
        return render_template('add_success.html', form=form)
    return render_template('add_article_wtf.html', form=form)

@app.route(
        '/animal/<string:myanimal>/<int:legs>')  # parametruose nurodomas kintamasis (title) ir
# jo tipas (string)
def animal(myanimal, legs):  # kintam1jį būtinai nurodykite ir funkcijos parametruose
    return render_template('index.html', data=articles)  # taip pat ir čia reikia jį perduoti


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
