import pandas as pd
import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../artifacts/model.pkl')

class CostPredictor:
    def __init__(self):
        with open(MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, X):
        predictions = self.model.predict(X)
        return predictions
    
predictor = CostPredictor()