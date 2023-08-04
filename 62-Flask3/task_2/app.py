from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<Student {self.name}>"

# Create the database and tables
with app.app_context():
    db.create_all()

# Routes for CRUD operations

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        grade = request.form['grade']
        student = Student(name=name, age=age, grade=grade)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.age = int(request.form['age'])
        student.grade = request.form['grade']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
