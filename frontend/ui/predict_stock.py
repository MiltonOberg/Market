from backend.components.stock import Stock
from backend.features.agent import Agent


class PredictStock:
    def __init__(self, choice: str = None, stock: Stock = None):
        self.stock = Stock(choice) if choice else stock
        self.agent = Agent
