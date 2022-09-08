from flask import render_template, redirect
from flask.views import View
from db import db
from models.todo import Todo


class DeleteView(View):
    methods = ["GET"]

    def dispatch_request(self, id):
        task_to_delete = Todo.query.get_or_404(id)
        try: 
            db.session.delete(task_to_delete)
            db.session.commit()
            return redirect('/')
        except Exception as ex:
            return ex
