from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, URL
from app.models import Data

class UrlShortenerForm(FlaskForm):
    url = StringField('Url to Shorter', validators=[DataRequired(), URL()])
    submit = SubmitField('Short')