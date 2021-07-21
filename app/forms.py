from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ConfigForm(FlaskForm):
    own_letterset = StringField('Letters:', validators=[DataRequired()])
    submit = SubmitField('Send')
