from backend.components.stock import Stock


class PredictStock:
    def __init__(self, choice: str = None, stock: Stock = None):
        self.stock = Stock(choice) if choice else stock

    def test(
        self,
    ):
        return "test"
