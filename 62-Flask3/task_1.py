from flask import Flask
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

# Helper functions for CRUD operations

def add_student(name, age, grade):
    student = Student(name=name, age=age, grade=grade)
    db.session.add(student)
    db.session.commit()
    return student

def get_student_by_id(id):
    return db.session.get(Student, id)

def get_all_students():
    return Student.query.all()

def update_student(id, name, age, grade):
    student = db.session.get(Student, id)
    student.name = name
    student.age = age
    student.grade = grade
    db.session.commit()
    return student

def delete_student(id):
    student = db.session.get(Student, id)
    db.session.delete(student)
    db.session.commit()

if __name__ == '__main__':
    # Sample usage of the functions:
    with app.app_context():
        # Add students
        student1 = add_student('John Doe', 22, 'A')
        student2 = add_student('Jane Smith', 20, 'B')

        # Get students by ID
        print(get_student_by_id(student1.id))
        print(get_student_by_id(student2.id))

        # Get all students
        all_students = get_all_students()
        for student in all_students:
            print(student)

        # Update student
        update_student(student1.id, 'John Doe Jr.', 23, 'A+')
        updated_student = get_student_by_id(student1.id)
        print(updated_student)

        # Delete student
        delete_student(student2.id)
