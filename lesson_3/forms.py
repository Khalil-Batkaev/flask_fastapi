from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, DateField
from wtforms.validators import DataRequired, EqualTo, Email


class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    conf_password = PasswordField('conf_password', validators=[DataRequired(), EqualTo('password')])
    birth_date = DateField('birth_date')
    confirm = BooleanField('Согласие на обработку данных', validators=[DataRequired()])
