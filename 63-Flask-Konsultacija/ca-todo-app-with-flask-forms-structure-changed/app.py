from flask import Flask
from flask_migrate import Migrate

from db import db


app = Flask(__name__)

app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)

db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'bet kokia simbolių eilutė'


migrate = Migrate(app, db)


from resources.index import IndexView
from resources.delete import DeleteView
from resources.update import UpdateView
app.add_url_rule('/', view_func=IndexView.as_view('index-view'))
app.add_url_rule('/delete/<int:id>', view_func=DeleteView.as_view('delete-view'))
app.add_url_rule('/update/<int:id>', view_func=UpdateView.as_view('update-view'))


if __name__ == "__main__":
    app.run(debug=True)