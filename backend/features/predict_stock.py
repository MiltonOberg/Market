from backend.components.stock import Stock
from backend.features.agent import Agent


class PredictStock:
    def __init__(self, choice: str = None, stock: Stock = None):
        self.stock = Stock(choice) if choice else stock
        self.agent = Agent(self.stock)
        self.agent.train()

    def predict_days(self, period=7):
        feature_preds = self.agent.predict_future(self.stock, days=period)
        return feature_preds
