from sklearn.preprocessing import StandardScaler

from backend.components.stock import Stock
from backend.features.models.agent import Agent


class MultiAgent(Agent):
    def __init__(self, stock: Stock):
        """Does not take Dividens and Stock Splits into account for now."""
        df_return = stock.get_return_data()
        self.X, self.y = (
            df_return.drop(columns=["Close", "Dividends", "Stock Splits", "Return"]),
            df_return["Return"],
        )
        self.input_shape = self.X.shape[1:]
        self.learning_rate = 0.00025
        self.model = self._create_model()
        self.train_data = None
        self.test_data = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

        self.standard_scaler = StandardScaler()


if __name__ == "__main__":
    stock = Stock("saab")
    agent = MultiAgent(stock)
    agent.train()
