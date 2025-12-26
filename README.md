# Electricity Cost Prediction

This repository contains a machine learning project focused on predicting electricity costs based on various infrastructure and environmental features. The dataset originates from a Kaggle dataset and includes real-world attributes such as water consumption, recycling rate, air quality index, and more. The main goal is to build a regression model that accurately estimates electricity cost per building.

---

## 📌 Problem Statement

With the rising demand for energy efficiency in urban environments, predicting electricity consumption is critical for better resource management. This project aims to:

- Develop a regression model to predict `Electricity_cost`.
- Understand the impact of environmental and structural features on electricity cost.
- Evaluate and compare model performance using RMSE and R-squared.

---

## 🧠 Features (Webapp)

- Electricity Cost Prediction: Utilizes a Gradient Boosting regression model to predict electricity costs based on user-input features.
- Easy-to-use Interface: A web application built with Flask that allows users to input relevant features and receive instant predictions.
- Responsive Design: Built with Bootstrap for a clean and user-friendly experience.

---

## 📊 Features (Dataset)

The dataset contains the following features:

| Feature Name                   | Description                                         | Type         |
|-------------------------------|-----------------------------------------------------|--------------|
| `Site_Area`                   | Name of the district/zone                          | Categorical  |
| `Structure_Type`              | Type of building (Residential, Industrial, etc.)   | Categorical  |
| `Water_Consumption_Per_Building` | Monthly water usage per building                | Numerical    |
| `Recycling_Rate`              | Waste recycling rate                          | Numerical    |
| `Utilization_Rate`            | Resource utilization efficiency                 | Numerical    |
| `Air_Quality_Index`           | Pollution index in the area                        | Numerical    |
| `Issue_Resolution_Time`       | Avg. time to resolve infrastructure issues   | Numerical    |
| `Resident_Count`              | Number of residents per structure                  | Numerical    |
| `Electricity_cost`            | Target variable: electricity cost    | Numerical    |

---

## 📁 Project Structure

```bash
electricity-cost-prediction/
├── data/
│   ├── raw/                 # Original Kaggle datasets
│   │   ├── train.csv
│   │   ├── test.csv
│   │   └── sample_submission.csv
│   └── processed/           # Cleaned, encoded, and feature-engineered datasets
│       ├── train_processed.csv
│       └── test_processed.csv
├── notebooks/
│   └── main.ipynb       # EDA, visualization, training, and testing model
├── artifacts/
│       ├── model.pkl              # Trained model file
│       └── preprocessor.pkl       # Preprocessing pipeline file
├── submission/
│   └── submission_final.csv       # Output file 
├── services/
│   ├── preprocessing.py     # Data preprocessing functions
│   └── predictor.py        # Model prediction functions
├── static/                   # Static files for the web app
│   ├── css/
│   └── js/
├── templates/                # HTML templates for the web app
│   ├── base.html
│   ├── index.html
│   ├── predict.html
│   └── result.html
├── app.py                    # Main application entry point
├── requirements.txt         # Python dependencies list
├── .gitignore
├── README.md                
```

---

## 🔁 Workflow

This project follows a typical machine learning workflow:

1. Data Collection and Preparation
   - Downloaded from Kaggle (see [Dataset & Credits](#-dataset--credits) section).
   - Contains training, test, and submission datasets.
   - Create train and validation set from splitting train.csv.

2. Data Preprocessing
   - Handled missing values and duplicates.
   - Performed feature engineering, label encoding for categorical features, and scaling for numerical features.

3. Exploratory Data Analysis (EDA)
   - Analyzed feature distributions, relationships, and outliers.
   - Visualized correlations between features and the target.

4. Model Training
   - Tried multiple regression models: Random Forest, Gradient Boosting, LightGBM, CatBoost, and XGBoost.
   - Hyperparameter tuning was performed where applicable using optuna.

5. Model Evaluation
   - Models were evaluated using RMSE and R² metrics on the validation set.
   - Visualized feature importance using SHAP values.
   - Best-performing model: **Gradient Boosting (GB)**.

6. Prediction & Submission
   - The final model is built using `sklearn.pipeline.Pipeline`, which encapsulates both the preprocessing steps (via `ColumnTransformer`) and the best model. This approach ensures that all data transformations are applied consistently during both training and prediction.
   - Submission file prepared in the required Kaggle format.

---

## 📈 Model Performance

Several regression models were evaluated to predict electricity cost. The performance was measured using **Root Mean Squared Error (RMSE)** and **R-squared (R²)** metrics. The results are summarized below:

| Model                 | RMSE        | R²       |
|----------------------|-------------|----------|
| Gradient Boosting (gb) | **3845.02**   | **0.2518** |
| LightGBM (lgbm)        | 3905.12   | 0.2268 |
| CatBoost               | 3921.79   | 0.2241 |
| Random Forest (rf)     | 3935.05   | 0.2099 |
| XGBoost (xgb)          | 4135.62   | 0.1498 |

The **Gradient Boosting model** outperformed the others with the **lowest RMSE (3845.02)** and the **highest R² score (0.2518)**, and was selected as the final model for inference.

---

## 📂 Dataset & Credits

The dataset used in this project was sourced from a Kaggle dataset. You can access the original dataset and challenge description via the following link:

🔗 [The Electricity Cost Prediction Challenge](https://www.kaggle.com/datasets/gauravduttakiit/the-electricity-cost-prediction-challenge)

We would like to extend our appreciation to the organizers and dataset contributors for making this resource available for public use.

---

## 🚀 How to Run

To run this project on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/abidalfrz/electricity-cost-prediction.git
cd electricity-cost-prediction
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate.bat     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
# Run the flask application
python app.py

# The Webapp will be accessible at http://localhost:5000
```

### 5. 5. Access the Application

Open your web browser and navigate to `http://localhost:5000` to access the house price prediction web app.

1. Click on "Start Prediction".
2. Fill in the required features in the form.
3. Cliclk "CALCULATE COST" to get the predicted electricity cost.

---

