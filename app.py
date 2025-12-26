import pandas as pd
from flask import Flask, request, url_for, render_template, redirect, flash
from services.preprocessing import preprocess_data
from services.predictor import predictor
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            data = {
                'Site_Area': str(request.form['Site_Area']),
                'Structure_Type': str(request.form['Structure_Type']),
                'Water_Consumption_Per_Building': float(request.form['Water_Consumption_Per_Building']),
                'Recycling_Rate': float(request.form['Recycling_Rate']),
                'Utilization_Rate': float(request.form['Utilization_Rate']),
                'Air_Quality_Index': float(request.form['Air_Quality_Index']),
                'Issue_Resolution_Time': float(request.form['Issue_Resolution_Time']),
                'Resident_Count': int(request.form['Resident_Count'])
            }

            X = pd.DataFrame([data])
            X_processed = preprocess_data(X)
            prediction = predictor.predict(X_processed)[0]
            flash('Prediction successful!', 'success')
            return redirect(url_for('result', cost=prediction))
        except Exception as e:
            flash(f'Error occurred: {str(e)}', 'error')
            return redirect(url_for('home'))
        
    return render_template('predict.html')

@app.route('/result')
def result():
    cost = request.args.get('cost', default=0, type=float)

    return render_template('result.html', cost=cost)

if __name__ == '__main__':
    app.run(debug=True)
