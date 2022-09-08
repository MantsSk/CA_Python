from flask import render_template, redirect
from flask.views import View
from form import UpdateForm
from db import db
from datetime import datetime
from models.todo import Todo


class UpdateView(View):
    methods = ["GET", "POST"]

    def dispatch_request(self, id):
        update_form = UpdateForm()
        task = Todo.query.get_or_404(id)
        if update_form.validate_on_submit():
            task.content = update_form.name.data
            task.date_created = datetime.now().replace(microsecond=0)
            try: 
                db.session.commit()
                return redirect('/')
            except Exception as ex:
                return ex
        else: 
            return render_template('update.html', task=task, form=update_form)