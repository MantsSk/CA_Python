import os
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, logout_user, login_user, UserMixin, login_required
import forms
from flask_bcrypt import Bcrypt
import datetime
from PIL import Image
import secrets
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '4654f5dfadsrfasdr54e6rae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'blogas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "prisijungti"

class Irasas(db.Model):
    __tablename__ = "irasas"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column("Data", db.DateTime)
    irasas = db.Column("irasas", db.String(20))
    vartotojas_id = db.Column(db.Integer, db.ForeignKey("vartotojas.id"))
    vartotojas = db.relationship("Vartotojas", backref="irasai")

class Vartotojas(db.Model, UserMixin):
    __tablename__ = "vartotojas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String(20), unique=True, nullable=False)
    el_pastas = db.Column("El.Pastas", db.String(120), unique=True, nullable=False)
    nuotrauka = db.Column("Nuotrauka", db.String(20), nullable=False, default="default.jpg")
    slaptazodis = db.Column("Slaptazodis", db.String(60), unique=True, nullable=False)

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

class ManoModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.el_pastas == "mantas.skara@gmail.com"

admin = Admin(app)
admin.add_view(ModelView(Irasas, db.session))
admin.add_view(ManoModelView(Vartotojas, db.session))

with app.app_context():
    db.create_all()

def save_picture(picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static', 'profilio_nuotraukos', picture_fn)

    output_size = (125, 125)
    i = Image.open(picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@login_manager.user_loader
def load_user(vartotojo_id):
    return Vartotojas.query.get(int(vartotojo_id))

@ app.route("/")
def index():
    return render_template("index.html")

@app.route("/naujas_irasas", methods=['GET', 'POST'])
@login_required
def new_record():
    form = forms.IrasasForm()
    if form.validate_on_submit():
        naujas_irasas = Irasas(irasas=form.irasas.data, vartotojas_id=current_user.id, data=datetime.datetime.now())
        db.session.add(naujas_irasas)
        db.session.commit()
        flash(f"Irasas sukurtas", "success")
        return redirect(url_for('index'))
    return render_template("prideti_irasa.html", form=form)

@app.route("/mano_irasai")
@login_required
def my_records():
    page = request.args.get('page', 1, type=int)
    visi_irasai = Irasas.query.filter_by(vartotojas_id=current_user.id).paginate(page=page, per_page=1)
    return render_template("mano_irasai.html", visi_irasai=visi_irasai, datetime=datetime.datetime)

@app.route("/visi_irasai")
@login_required
def all_records():
    page = request.args.get('page', 1, type=int)
    visi_irasai = Irasas.query.paginate(page=page, per_page=3)
    return render_template("visi_irasai.html", visi_irasai=visi_irasai, datetime=datetime.datetime)

@app.route("/registruotis", methods=['GET', 'POST'])
def registruotis():
    form = forms.RegistracijosForma()
    if form.validate_on_submit():
        vardas = form.vardas.data
        el_pastas = form.el_pastas.data
        slaptazodis = bcrypt.generate_password_hash(form.slaptazodis.data).decode('utf-8')
        vartotojas = Vartotojas(vardas=vardas, el_pastas=el_pastas, slaptazodis=slaptazodis)
        db.session.add(vartotojas)
        db.session.commit()
        flash("Sekmingai prisiregistravote! Galite prisijungti", 'success')
        return redirect(url_for('index'))
    return render_template("registruotis.html", form=form)

@app.route("/prisijungti", methods=['GET', 'POST'])
def prisijungti():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.PrisijungimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(el_pastas=form.el_pastas.data).first()
        if user and bcrypt.check_password_hash(user.slaptazodis, form.slaptazodis.data):
            login_user(user, remember=form.prisiminti.data)
            next_page = request.args.get('next')
            flash(f"Sveiki prisijunge {current_user.vardas}", 'success')
            return redirect(next_page) if next_page else redirect(url_for("index"))
        else:
            flash("Prisijungti nepavyko. Patikrinkite el.pasta arba slaptazodi", 'danger')
    return render_template('prisijungti.html', form=form)

@app.route("/atsijungti")
def atsijungti():
    logout_user()
    return redirect(url_for('index'))

@app.route("/paskyra", methods=['GET', 'POST'])
@login_required
def account(): 
    form = forms.PaskyrosAtnaujinimoForma()
    if form.validate_on_submit():
        if form.nuotrauka.data:
            # print(form.nuotrauka.data.filename)
            nuotrauka = save_picture(form.nuotrauka.data)
            current_user.nuotrauka = nuotrauka
        current_user.vardas = form.vardas.data
        current_user.el_pastas = form.el_pastas.data
        db.session.commit()
        flash("Tavo paskyra atnaujinta", 'success')
        return redirect(url_for('account'))
    form.vardas.data = current_user.vardas
    form.el_pastas.data = current_user.el_pastas
    nuotrauka = url_for('static', filename='profilio_nuotraukos/' + current_user.nuotrauka)
    return render_template('paskyra.html', form=form, nuotrauka=nuotrauka)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
