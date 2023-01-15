from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError


def status_check(form, field):
    if field.data != 'published' and field.data != 'unpublished':
        raise ValidationError(f"Field must either published or unpublished")


class ArticleForm(FlaskForm):
    author = StringField('author', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    status = StringField('status', validators=[DataRequired(), status_check])
    text = StringField('text', validators=[DataRequired()])
    date = DateField('date', validators=[DataRequired()])
    submit = SubmitField('Submit')
