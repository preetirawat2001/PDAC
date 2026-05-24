import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess_discovery_data(file_path="/content/pan_data.csv"):
    df = pd.read_csv(file_path)
    le = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = le.fit_transform(df[col].astype(str))
    feature_cols = [col for col in df.columns if col != 'ic50_effect_size']
    X = df[feature_cols]
    y = df['ic50_effect_size'] if 'ic50_effect_size' in df.columns else df.iloc[:, -1]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, feature_cols, scaler