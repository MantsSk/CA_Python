from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from biudzetas import db
from biudzetas.models import Irasas
from biudzetas.expenses.forms import IrasasForm
from datetime import datetime

expenses = Blueprint('expenses', __name__)

@expenses.route("/irasai")
@login_required
def records():
    db.create_all()
    page = request.args.get('page', 1, type=int)
    visi_irasai = Irasas.query.filter_by(vartotojas_id=current_user.id).order_by(Irasas.data.asc()).paginate(page=page,
                                                                                                             per_page=5)
    return render_template("irasai.html", visi_irasai=visi_irasai, datetime=datetime)


@expenses.route("/naujas_irasas", methods=["GET", "POST"])
def new_record():
    db.create_all()
    forma = IrasasForm()
    if forma.validate_on_submit():
        naujas_irasas = Irasas(pajamos=forma.pajamos.data, suma=forma.suma.data, vartotojas_id=current_user.id)
        db.session.add(naujas_irasas)
        db.session.commit()
        flash(f"Įrašas sukurtas", 'success')
        return redirect(url_for('expenses.records'))
    return render_template("prideti_irasa.html", form=forma)


@expenses.route("/delete/<int:id>")
def delete(id):
    irasas = Irasas.query.get(id)
    db.session.delete(irasas)
    db.session.commit()
    return redirect(url_for('expenses.records'))


@expenses.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    forma = IrasasForm()
    irasas = Irasas.query.get(id)
    if forma.validate_on_submit():
        irasas.pajamos = forma.pajamos.data
        irasas.suma = forma.suma.data
        db.session.commit()
        return redirect(url_for('expenses.records'))
    return render_template("update.html", form=forma, irasas=irasas)


@expenses.route("/balansas")
def balance():
    try:
        visi_irasai = Irasas.query.filter_by(vartotojas_id=current_user.id)
    except:
        visi_irasai = []
    balansas = 0
    for irasas in visi_irasai:
        if irasas.pajamos:
            balansas += irasas.suma
        else:
            balansas -= irasas.suma
    return render_template("balansas.html", balansas=balansas)