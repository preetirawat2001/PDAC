from sklearn.ensemble import RandomForestRegressor, StackingRegressor
from sklearn.linear_model import ElasticNet
from xgboost import XGBRegressor
import torch
import torch.nn as nn
import torch.nn.functional as F

def get_stacked_ensemble_model():
    base_models = [
        ('elastic', ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42)),
        ('rf', RandomForestRegressor(n_estimators=100, random_state=42)),
        ('xgb', XGBRegressor(n_estimators=100, learning_rate=0.05, random_state=42))
    ]
    meta_model = RandomForestRegressor(n_estimators=50, random_state=42)
    return StackingRegressor(estimators=base_models, final_estimator=meta_model)