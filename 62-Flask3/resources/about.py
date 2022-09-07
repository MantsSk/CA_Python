from flask import render_template
from flask.views import View

from db import db
from models.Message import Message


class AboutView(View):
    methods = ["GET"]

    def dispatch_request(self):
        new_msg = Message("vakaris", "email@mail", "vienas", "8666666")
        db.session.add(new_msg)
        db.session.commit()
        return render_template('about.html')
