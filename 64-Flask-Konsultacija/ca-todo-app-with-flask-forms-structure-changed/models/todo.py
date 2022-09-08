from db import db

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(200))
    date_created = db.Column(db.DateTime)

    def __init__(self, content, date_created):
        self.content = content
        self.date_created = date_created

    def __repr__(self):
        return f'{self.name} - {self.email}'

