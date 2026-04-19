import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import LSTM, Dense  # type: ignore
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore

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

        self.LOOKBACK = 60

    def _create_sequense(self):
        X_seq, y_seq = [], []
        for i in range(self.LOOKBACK, len(self.X)):
            X_seq.append(self.X.iloc[i - self.LOOKBACK : i].values)
            y_seq.append(self.y.iloc[i])
        return np.array(X_seq), np.array(y_seq)

    def _create_model(self):
        model = Sequential()
        model.add(
            LSTM(
                128, input_shape=(self.LOOKBACK, self.X.shape(1)), return_sequences=True
            )
        )
        model.add(LSTM(64))
        model.add(Dense(1, activation="linear"))

        model.compile(loss="mse", optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def predict_future(
        self,
    ):
        latest_day = self.X.iloc[-1].values.reshape(1, -1)
        return latest_day


if __name__ == "__main__":
    stock = Stock("saab")
    agent = MultiAgent(stock)
    agent.train()
