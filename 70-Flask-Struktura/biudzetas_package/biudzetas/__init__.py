import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '4654f5dfadsrfasdr54e6rae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'biudzetas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from biudzetas.models import Vartotojas, Irasas

db.create_all()
bcrypt = Bcrypt(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'prisijungti'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(vartotojo_id):
    return Vartotojas.query.get(int(vartotojo_id))


class ManoModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.el_pastas == "donoras@gmail.com"

from biudzetas import routes
admin = Admin(app)
admin.add_view(ManoModelView(Vartotojas, db.session))
admin.add_view(ManoModelView(Irasas, db.session))

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# app.config['MAIL_USERNAME'] = MAIL_USERNAME
# app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
