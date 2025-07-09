# Electricity Cost Prediction

This repository contains a machine learning project focused on predicting electricity costs based on various infrastructure and environmental features. The dataset originates from a Kaggle dataset and includes real-world attributes such as water consumption, recycling rate, air quality index, and more. The main goal is to build a regression model that accurately estimates electricity cost per building.

---

## 📌 Problem Statement

With the rising demand for energy efficiency in urban environments, predicting electricity consumption is critical for better resource management. This project aims to:

- Develop a regression model to predict `Electricity_cost`.
- Understand the impact of environmental and structural features on electricity cost.
- Evaluate and compare model performance using RMSE and R-Square.

---

## 🧠 Features

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
| `Electricity_cost`            | Target variable: electricity cost in currency   | Numerical    |

---

## 🧪 Project Structure

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
│   └── predictions.ipynb       # EDA, visualization, training, and testing model
├── models/
│   └── final_model.pkl      # Saved trained model
├── submission/
│   └── submission.csv       # Output file to be uploaded to Kaggle
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

---

## 📂 Dataset & Credits

The dataset used in this project was sourced from a Kaggle dataset. You can access the original dataset and challenge description via the following link:

🔗 [The Electricity Cost Prediction Challenge](https://www.kaggle.com/datasets/gauravduttakiit/the-electricity-cost-prediction-challenge)

We would like to extend our appreciation to the organizers and dataset contributors for making this resource available for public use.
