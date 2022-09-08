from flask import Flask, redirect, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from form import TaskForm, UpdateForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'bet kokia simbolių eilutė'

app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(200))
    date_created = db.Column(db.DateTime)

db.create_all()
migrate = Migrate(app, db)

@app.route('/', methods=['POST', 'GET'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        task_content = form.name.data
        new_task = Todo(content=task_content, date_created=datetime.now().replace(microsecond=0))
        try: 
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as ex:
            return ex
    else:  
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks, form=form)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try: 
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as ex:
        return ex

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
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

if __name__ == "__main__":
    app.run(debug=True)