from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'sqlite.db')

db = SQLAlchemy(app)
ma = Marshmallow(app)
Migrate(app, db)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    done = db.Column('done', db.Boolean)


# Užduoties schema
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'done')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


# Crud
@app.route('/tasks/new', methods=['POST'])
def add_task():
    title = request.json['title']
    done = request.json['done']
    new_task = Task(title=title, done=done)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)


# cRud
@app.route('/tasks', methods=['GET'])
def all_tasks():
    all_tasks = Task.query.all()
    return tasks_schema.jsonify(all_tasks)


# cRud
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)


# crUd
@app.route('/tasks/<id>', methods=['PUT'])
def edit_task(id):
    task = Task.query.get(id)
    task.title = request.json['title']
    task.done = request.json['done']
    db.session.commit()
    return task_schema.jsonify(task)


# cruD
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
