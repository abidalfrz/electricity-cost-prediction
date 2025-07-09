# Electricity Cost Prediction

This repository contains a complete pipeline for a machine learning project aimed at predicting **electricity cost** using structured features such as building usage, population, environmental and utility metrics. The dataset comes from a Kaggle competition.

---

## 📌 Overview

This project tackles a regression problem, where the objective is to predict the **Electricity Cost** . The dataset includes multiple categorical and numerical attributes that reflect building structure, air quality, water usage, and more.

The data was sourced from a Kaggle dataset and includes `train.csv`, `test.csv`, and a `sample_submission.csv` file.

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
