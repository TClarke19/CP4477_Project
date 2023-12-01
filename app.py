from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField
from wtforms.validators import DataRequired
import numpy as np

class MpgForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    submit = SubmitField('Predict MPG')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key' #TODO: replace with secret key

@app.route('/')
def home():
    return "Testing"

if __name__ == "__main__":
    app.run(debug=True)