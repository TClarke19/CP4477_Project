from flask import Flask, request, render_template
from wtforms import SubmitField, FloatField, Form
from wtforms.validators import DataRequired
from joblib import load
import numpy as np
import os
from socket import gethostname

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
app = Flask(__name__, template_folder=template_dir)

mpg_model = load('mpg_model.joblib')
diabetes_model = load('diabetes_model.joblib')

class MpgForm(Form):
    cylinders = FloatField('cylinders', validators=[DataRequired()])
    displacement = FloatField('displacement', validators=[DataRequired()])
    horsepower = FloatField('horsepower', validators=[DataRequired()])
    weight = FloatField('weight', validators=[DataRequired()])
    age = FloatField('age', validators=[DataRequired()])
    origin_japan = FloatField('origin_japan', validators=[DataRequired()])
    origin_usa = FloatField('origin_usa', validators=[DataRequired()])
    submit = SubmitField('Predict MPG')

class DiabetesForm(Form):
    pregnancies = FloatField('pregnancies', validators=[DataRequired()])
    BloodPressure = FloatField('BloodPressure', validators=[DataRequired()])
    Insulin = FloatField('Insulin', validators=[DataRequired()])
    Outcome = FloatField('Outcome', validators=[DataRequired()])
    BMI_Age = FloatField('BMI_Age', validators=[DataRequired()])
    DPF_Age = FloatField('dpf-age', validators=[DataRequired()])
    submit = SubmitField('Predict Diabetes')

@app.route('/', methods=['GET', 'POST'])
def index():
    mpg_form = MpgForm()
    diabetes_form = DiabetesForm()

    if 'mpg_submit' in request.form and mpg_form.validate():
        dataMPG = [mpg_form.cylinders.data, 
                   mpg_form.displacement.data, 
                   mpg_form.horsepower.data, 
                   mpg_form.weight.data, 
                   mpg_form.age.data, 
                   mpg_form.origin_japan.data, 
                   mpg_form.origin_usa.data]
        prediction = mpg_model.predict(np.array(dataMPG).reshape(1, -1))
        return f'The predicted MPG is {prediction[0]}'

    elif 'diabetes_submit' in request.form and diabetes_form.validate():
        dataDiabetes = [diabetes_form.pregnancies.data, 
                        diabetes_form.BloodPressure.data, 
                        diabetes_form.Insulin.data, 
                        diabetes_form.Outcome.data, 
                        diabetes_form.BMI_Age.data, 
                        diabetes_form.DPF_Age.data]
        prediction = diabetes_model.predict(np.array(dataDiabetes).reshape(1, -1))
        return f'The predicted Diabetes is {prediction[0]}'

    return render_template('index.html', mpg_form=mpg_form, diabetes_form=diabetes_form)

if __name__ == '__main__':
    app.run(debug=False)