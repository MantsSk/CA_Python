from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from biudzetas.config import Config
from flask_admin import Admin

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.prisijungti'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    admin = Admin(app)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # admin.init_app(app)

    from biudzetas.users.routes import users
    from biudzetas.expenses.routes import expenses
    from biudzetas.main.routes import main
    from biudzetas.errors.routes import errors
    # from biudzetas.administrator.routes import administrator
    app.register_blueprint(users)
    app.register_blueprint(expenses)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    # app.register_blueprint(administrator)

    return app