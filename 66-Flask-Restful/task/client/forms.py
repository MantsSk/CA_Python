from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FloatField, IntegerField
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    title = StringField('Title', [DataRequired()])
    price = FloatField('Price', [DataRequired()])
    quantity = IntegerField('Quantity', [DataRequired()])
    submit = SubmitField('Submit')
