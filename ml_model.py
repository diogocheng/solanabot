import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

class MLModel:
    def __init__(self):
        try:
            self.model = joblib.load('trading_model.pkl')
        except:
            self.model = GradientBoostingClassifier(n_estimators=100)

    def train(self, data_path='historical_data.csv'):
        df = pd.read_csv(data_path)
        # Ensure your CSV has columns: liquidity, volume_24h, price_change_24h, buy_sell_ratio, success_label
        X = df[['liquidity', 'volume_24h', 'price_change_24h', 'buy_sell_ratio']]
        y = df['success_label']
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        self.model.fit(X_train, y_train)
        joblib.dump(self.model, 'trading_model.pkl')

    def predict(self, features):
        return self.model.predict_proba([features])[0][1]
