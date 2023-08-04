import os
from datetime import datetime
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from form import MessageForm


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bet kokia simbolių eilutė'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80))
    comment = db.Column(db.Text, nullable=False)

    def __init__(self, first_name, last_name, comment, date):
        self.first_name = first_name
        self.last_name = last_name
        self.comment = comment
        self.date = date

    def __repr__(self):
        return f'{self.first_name} - {self.last_name}'


@app.route('/', methods=['GET', 'POST'])
def index():
    data = Message.query.all()
    form = MessageForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        comment = form.comment.data
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        entry = Message(first_name=first_name,
                        last_name=last_name, comment=comment, date=date)
        db.session.add(entry)
        db.session.commit()
        data = Message.query.all()
        stats = 10000 - len(data)
        return render_template('index.html', form=False, data=data, stats=stats)
    return render_template('index.html', form=form, data=data)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
