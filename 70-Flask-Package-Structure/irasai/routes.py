
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, logout_user, login_user, login_required
import datetime
from PIL import Image
import secrets
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Message
from PIL import Image
from irasai import mail
import os
from irasai import app, db, login_manager, bcrypt
from .models import Irasas, Vartotojas
from .forms import RegistracijosForma, PaskyrosAtnaujinimoForma, SlaptazodzioAtnaujinimoForma, IrasasForm, PrisijungimoForma, UzklausosAtnaujinimoForma


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Slaptažodžio atnaujinimo užklausa',
                  sender='el@pastas.lt',
                  recipients=["codeacademytest80@gmail.com"])
    msg.body = f'''Norėdami atnaujinti slaptažodį, paspauskite nuorodą:
    {url_for('reset_password', token=token, _external=True)}
    Jei jūs nedarėte šios užklausos, nieko nedarykite ir slaptažodis nebus pakeistas.
    '''
    mail.send(msg)


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
    form = IrasasForm()
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
    # page = request.args.get('page', 1, type=int)
    visi_irasai = Irasas.query.all()
    return render_template("visi_irasai.html", visi_irasai=visi_irasai, datetime=datetime.datetime)

@app.route("/registruotis", methods=['GET', 'POST'])
def registruotis():
    form = RegistracijosForma()
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
    form = PrisijungimoForma()
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
    form = PaskyrosAtnaujinimoForma()
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

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("home")) # pakeisti i index
    form = UzklausosAtnaujinimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(el_pastas=form.el_pastas.data).first()
        send_reset_email(user)
        flash(f"Jums issiustas el.laiskas su slaptazodzio atnaujinimo instrukcijomis: {user.el_pastas}", 'info')
        return redirect(url_for('prisijungti'))
    return render_template('reset_request.html', form=form)

@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("home")) # #2 fix bug
    user = Vartotojas.verify_reset_token(token)
    if user is None:
        flash("Uzklausa netinka arba pasibaigusio galiojima", "warning")
        return redirect(url_for("reset_request"))
    form = SlaptazodzioAtnaujinimoForma()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.slaptazodis.data).decode('utf-8')
        user.slaptazodis = hashed_password
        db.session.commit()
        flash("Tavo slaptazodis sekmingai pakeistas. Gali prisijungti", 'success')
        return redirect(url_for('prisijungti'))
    return render_template("reset_password.html", form=form)

@app.errorhandler(404)
def page_error(error):
    # error galime perduoti i template
    return render_template('error.html', error=error)
