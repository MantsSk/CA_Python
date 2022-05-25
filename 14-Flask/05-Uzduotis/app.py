from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime)

db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        if request.form['content'] != "":
            task_content = request.form['content']
            new_task = Todo(content=task_content, date_created=datetime.now().replace(microsecond=0))
            try: 
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except Exception as ex:
                return ex
        else: 
            return redirect('/')
    else:  
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)

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
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        if request.form['content'] != "":
            task.content = request.form['content']
            task.date_created = datetime.now().replace(microsecond=0)
            try: 
                db.session.commit()
                return redirect('/')
            except Exception as ex:
                return ex
        else:
            return "Updating value to nothing, not allowed"
    else: 
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)