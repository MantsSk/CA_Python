from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from models import User


class ProfileForm(FlaskForm):
    name = StringField('Vardas', [DataRequired()])
    email = StringField('El. paštas', [DataRequired()])
    avatar = FileField('Atnaujinti profilio nuotrauką', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Atnaujinti')

    def validate_name(self, name):
        if name.data != current_user.name:
            user = User.query.filter_by(name=name.data).first()
            if user:
                raise ValidationError('Šis name panaudotas. Pasirinkite kitą.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Šis el. pašto adresas panaudotas. Pasirinkite kitą.')
