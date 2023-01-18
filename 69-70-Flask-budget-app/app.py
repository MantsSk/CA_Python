import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, current_user, logout_user, login_user, login_required
from sqlalchemy import DateTime
from datetime import datetime
import forms

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'sqlite.db')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = "Log in to see this page."


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String(20), unique=True, nullable=False)
    email = db.Column("email", db.String(
        120), unique=True, nullable=False)
    password = db.Column("password", db.String(60),
                         unique=True, nullable=False)


class Entry(db.Model):
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column("date", DateTime, default=datetime.now())
    income = db.Column("income", db.Boolean)
    sum = db.Column("name", db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", lazy=True)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(
            name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. You can log in now.', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login failed. Check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


@app.route("/entries")
@login_required
def entries():
    try:
        all_entries = Entry.query.filter_by(
            user_id=current_user.id).all()
    except:
        all_entries = []
    print(all_entries)
    return render_template("entries.html", all_entries=all_entries, datetime=datetime)


@app.route("/new_entry", methods=["GET", "POST"])
@login_required
def new_entry():
    form = forms.EntryForm()
    if form.validate_on_submit():
        new_entry = Entry(income=form.income.data,
                          sum=form.sum.data, user_id=current_user.id)
        db.session.add(new_entry)
        db.session.commit()
        flash('Entry created successfully', 'success')
        return redirect(url_for('entries'))
    return render_template("new_entry.html", form=form)


@app.route("/delete/<int:id>")
@login_required
def delete(id):
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('entries'))


@app.route("/update/<int:id>", methods=['GET', 'POST'])
@login_required
def update(id):
    form = forms.EntryForm()
    entry = Entry.query.get(id)
    if form.validate_on_submit():
        entry.income = form.income.data
        entry.sum = form.sum.data
        db.session.commit()
        return redirect(url_for('entries'))
    return render_template('update.html', form=form, entry=entry)


@app.route("/balance")
@login_required
def balance():
    try:
        all_entries = Entry.query.filter_by(user_id=current_user.id)
    except:
        all_entries = []
    balance = 0
    for entry in all_entries:
        if entry.income:
            balance += entry.sum
        else:
            balance -= entry.sum
    return render_template("balance.html", balance=balance)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
