import pandas as pd
import pickle
import os

PREPROCESSOR_PATH = os.path.join(os.path.dirname(__file__), '../artifacts/preprocessor.pkl')

def add_features(df):
    df["Water_Per_Resident"] = df["Water_Consumption_Per_Building"] / df["Resident_Count"]
    high_residents = df["Resident_Count"] > df["Resident_Count"].quantile(0.75)
    water_above_mean = df["Water_Consumption_Per_Building"] > df["Water_Consumption_Per_Building"].mean()
    df["high_water_residents"] = (high_residents & water_above_mean).astype(int)
    low_air_quality = df["Air_Quality_Index"] < df["Air_Quality_Index"].quantile(0.25)
    issue_resolution_mean = df["Issue_Resolution_Time"].mean()
    df['low_air_high_issue'] = ((low_air_quality & (df["Issue_Resolution_Time"] > issue_resolution_mean)).astype(int))
    df['low_air_high_residents'] = ((low_air_quality & high_residents).astype(int))
    df['high_issue_residents'] = ((df["Issue_Resolution_Time"] > issue_resolution_mean) & high_residents).astype(int)
    high_recycling = df["Recycling_Rate"] > df["Recycling_Rate"].quantile(0.75)
    high_utilization = df["Utilization_Rate"] > df["Utilization_Rate"].quantile(0.75)
    df['high_recycling_utilization'] = ((high_recycling & high_utilization).astype(int))

    return df

def preprocess_data(df):
    df = add_features(df)

    categoric = df.select_dtypes(include=['object']).columns.tolist()

    with open(PREPROCESSOR_PATH, 'rb') as f:
        preprocessor = pickle.load(f)

    df_processed = preprocessor.transform(df)
    
    numeric = df.select_dtypes(include=['number']).columns.tolist()

    df_processed = pd.DataFrame(df_processed, columns = numeric + list(preprocessor.transformers_[1][1].get_feature_names_out(categoric)))
    return df_processed

