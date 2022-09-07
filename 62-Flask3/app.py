import os

from flask import Flask
from flask_migrate import Migrate  # importuojame migracijas

from db import db

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
db.init_app(app)

from resources.about import AboutView
from resources.index import IndexView
app.add_url_rule('/', view_func=IndexView.as_view('index-view'))
app.add_url_rule('/about', view_func=AboutView.as_view('about-view'))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Migrate(app, db)  # Susiejame app ir db.

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
