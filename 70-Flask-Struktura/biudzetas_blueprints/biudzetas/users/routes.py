from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from biudzetas.users.forms import (RegistracijosForma, PrisijungimoForma, 
SlaptazodzioAtnaujinimoForma, PaskyrosAtnaujinimoForma, UzklausosAtnaujinimoForma)
from biudzetas.models import Vartotojas
from biudzetas import db
from werkzeug.security import generate_password_hash, check_password_hash
from biudzetas.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

@users.route("/registruotis", methods=['GET', 'POST'])
def registruotis():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistracijosForma()
    if form.validate_on_submit():
        koduotas_slaptazodis = generate_password_hash(form.slaptazodis.data)
        vartotojas = Vartotojas(vardas=form.vardas.data, el_pastas=form.el_pastas.data,
                                slaptazodis=koduotas_slaptazodis)
        db.session.add(vartotojas)
        db.session.commit()
        flash('Sėkmingai prisiregistravote! Galite prisijungti', 'success')
        return redirect(url_for('main.index'))
    return render_template('registruotis.html', title='Register', form=form)


@users.route("/prisijungti", methods=['GET', 'POST'])
def prisijungti():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = PrisijungimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(el_pastas=form.el_pastas.data).first()
        if user and check_password_hash(user.slaptazodis, form.slaptazodis.data):
            login_user(user, remember=form.prisiminti.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Prisijungti nepavyko. Patikrinkite el. paštą ir slaptažodį', 'danger')
    return render_template('prisijungti.html', title='Prisijungti', form=form)


@users.route("/atsijungti")
def atsijungti():
    logout_user()
    return redirect(url_for('main.index'))

@users.route("/paskyra", methods=['GET', 'POST'])
@login_required
def paskyra():
    form = PaskyrosAtnaujinimoForma()
    if form.validate_on_submit():
        if form.nuotrauka.data:
            nuotrauka = save_picture(form.nuotrauka.data)
            current_user.nuotrauka = nuotrauka
        current_user.vardas = form.vardas.data
        current_user.el_pastas = form.el_pastas.data
        db.session.commit()
        flash('Tavo paskyra atnaujinta!', 'success')
        return redirect(url_for('paskyra'))
    elif request.method == 'GET':
        form.vardas.data = current_user.vardas
        form.el_pastas.data = current_user.el_pastas
    nuotrauka = url_for('static', filename='profilio_nuotraukos/' + current_user.nuotrauka)
    return render_template('paskyra.html', title='Account', form=form, nuotrauka=nuotrauka)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UzklausosAtnaujinimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(el_pastas=form.el_pastas.data).first()
        send_reset_email(user)
        flash('Jums išsiųstas el. laiškas su slaptažodžio atnaujinimo instrukcijomis.', 'info')
        return redirect(url_for('prisijungti'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = Vartotojas.verify_reset_token(token)
    if user is None:
        flash('Užklausa netinkama arba pasibaigusio galiojimo', 'warning')
        return redirect(url_for('reset_request'))
    form = SlaptazodzioAtnaujinimoForma()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.slaptazodis.data)
        user.slaptazodis = hashed_password
        db.session.commit()
        flash('Tavo slaptažodis buvo atnaujintas! Gali prisijungti', 'success')
        return redirect(url_for('prisijungti'))
    return render_template('reset_token.html', title='Reset Password', form=form)