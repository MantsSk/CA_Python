
from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.errorhandler(404)
def klaida_404(klaida):
    return render_template("404.html"), 404


@errors.errorhandler(403)
def klaida_403(klaida):
    return render_template("403.html"), 403


@errors.errorhandler(500)
def klaida_500(klaida):
    return render_template("500.html"), 500