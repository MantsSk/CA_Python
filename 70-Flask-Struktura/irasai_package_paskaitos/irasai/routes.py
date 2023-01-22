@ app.route("/")
def index():
    return render_template("index.html")


@app.route("/naujas_irasas", methods=['GET', 'POST'])
@login_required
def new_record():
    form = forms.IrasasForm()
    if form.validate_on_submit():
        naujas_irasas = Irasas(
            irasas=form.irasas.data, vartotojas_id=current_user.id, data=datetime.datetime.now())
        db.session.add(naujas_irasas)
        db.session.commit()
        flash(f"Irasas sukurtas", "success")
        return redirect(url_for('index'))
    return render_template("prideti_irasa.html", form=form)


@app.route("/mano_irasai")
@login_required
def my_records():
    page = request.args.get('page', 1, type=int)
    visi_irasai = Irasas.query.filter_by(
        vartotojas_id=current_user.id).paginate(page=page, per_page=1)
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
        slaptazodis = bcrypt.generate_password_hash(
            form.slaptazodis.data).decode('utf-8')
        vartotojas = Vartotojas(
            vardas=vardas, el_pastas=el_pastas, slaptazodis=slaptazodis)
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
        user = Vartotojas.query.filter_by(
            el_pastas=form.el_pastas.data).first()
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
    nuotrauka = url_for(
        'static', filename='profilio_nuotraukos/' + current_user.nuotrauka)
    return render_template('paskyra.html', form=form, nuotrauka=nuotrauka)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = forms.UzklausosAtnaujinimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(
            el_pastas=form.el_pastas.data).first()
        send_reset_email(user)
        flash(
            'Jums išsiųstas el. laiškas su slaptažodžio atnaujinimo instrukcijomis.', 'info')
        return redirect(url_for('prisijungti'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = Vartotojas.verify_reset_token(token)
    if user is None:
        flash('Užklausa netinkama arba pasibaigusio galiojimo', 'warning')
        return redirect(url_for('reset_request'))
    form = forms.SlaptazodzioAtnaujinimoForma()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.slaptazodis.data).decode('utf-8')
        user.slaptazodis = hashed_password
        db.session.commit()
        flash('Tavo slaptažodis buvo atnaujintas! Gali prisijungti', 'success')
        return redirect(url_for('prisijungti'))
    return render_template('reset_token.html', title='Reset Password', form=form)
