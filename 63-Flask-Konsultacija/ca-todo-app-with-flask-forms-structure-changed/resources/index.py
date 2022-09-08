from flask import render_template, redirect, url_for
from flask.views import View
from form import TaskForm
from db import db
from datetime import datetime
from models.todo import Todo


class IndexView(View):
    methods = ["GET", "POST"]

    def dispatch_request(self):
        form = TaskForm()
        if form.validate_on_submit():
            task_content = form.name.data
            new_task = Todo(content=task_content, date_created=datetime.now().replace(microsecond=0))
            try: 
                db.session.add(new_task)
                db.session.commit()
                return redirect(url_for('index-view'))
            except Exception as ex:
                return ex
        else:  
            tasks = Todo.query.order_by(Todo.date_created).all()
            return render_template('index.html', tasks = tasks, form=form)