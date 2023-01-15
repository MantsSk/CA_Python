import os

import requests
from flask import Flask, render_template, request, flash, url_for
from flask_login import LoginManager, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from db import db
from models.User import User
from scr.articles import articles
from scr.forms.article_form import ArticleForm
from scr.forms.login_form import LoginForm
from scr.forms.registration_form import RegistrationForm

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'register'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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


@app.route('/flash')  # parametruose nurodomas kintamasis (title) ir
def flash_messages():  # kintam1jį būtinai nurodykite ir funkcijos parametruose
    flash('Sėkmingai prisiregistravote! Galite prisijungti', 'danger')
    return render_template('info.html')  # taip pat ir čia reikia jį perduoti


@app.route('/register', methods=['GET', 'POST'])
def register():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data,
                    password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('Sėkmingai prisiregistravote! Galite prisijungti', 'success')
        return redirect(url_for('index'))
    return render_template('registration.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Prisijungti nepavyko. Patikrinkite el. paštą ir slaptažodį', 'danger')
    return render_template('login.html', title='Prisijungti', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
