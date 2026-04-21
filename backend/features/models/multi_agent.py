import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import LSTM, Dense, Input  # type: ignore
from tensorflow.keras.models import Sequential, load_model  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore

from backend.components.stock import Stock
from backend.features.models.agent import Agent
from utils.constants import MULTI_WEIGHTS_DIR, WEIGHTS_DIR
from utils.stock_list import SWEDISH_STOCKS


class MultiAgent(Agent):
    def __init__(self, stock: Stock, lookback: int = 60):
        """Does not take Dividens and Stock Splits into account for now."""
        df_return = stock.get_return_data()
        self.X, self.y = (
            df_return.drop(columns=["Close", "Dividends", "Stock Splits", "Return"]),
            df_return["Return"],
        )
        self.input_shape = self.X.shape[1:]
        self.learning_rate = 0.00025
        self.LOOKBACK = lookback
        self.model = self._create_model()
        self.train_data = None
        self.test_data = None
        self.standard_scaler = StandardScaler()

    def _create_sequense(self, X: np.array, y: np.array):
        X_seq, y_seq = [], []
        for i in range(self.LOOKBACK, len(X)):
            X_seq.append(X[i - self.LOOKBACK : i])
            y_seq.append(y[i])
        return np.array(X_seq), np.array(y_seq)

    def _create_model(self):
        model = Sequential()
        model.add(Input(shape=(self.LOOKBACK, self.X.shape[1])))
        model.add(LSTM(128, return_sequences=True))
        model.add(LSTM(64))
        model.add(Dense(1, activation="linear"))

        model.compile(loss="mse", optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def train_on_multiple(self, stock_list: list, epochs: int = 10):
        all_X_seq = []
        all_y_seq = []

        for ticker in stock_list:
            try:
                stock = Stock(ticker)
                df_return = stock.get_return_data()
                X, y = (
                    df_return.drop(
                        columns=["Close", "Dividends", "Stock Splits", "Return"]
                    ),
                    df_return["Return"],
                )
                X_scaled = np.array(self.standard_scaler.fit_transform(X))
                y_array = np.array(y)
                X_seq, y_seq = self._create_sequense(X_scaled, y_array)

                all_X_seq.append(X_seq)
                all_y_seq.append(y_seq)
            except Exception as e:
                print(f"Skipping {ticker}, not found: {e}")

        X_total = np.concatenate(all_X_seq)
        y_total = np.concatenate(all_y_seq)

        X_train, X_test, y_train, y_test = train_test_split(
            X_total, y_total, test_size=0.2, shuffle=True
        )
        self.train_data = (X_train, y_train)
        self.test_data = (X_test, y_test)

        history = self.model.fit(
            X_train,
            y_train,
            validation_data=(X_test, y_test),
            epochs=epochs,
            batch_size=32,
        )
        return history

    def evaluate_direction(
        self,
    ):
        ypred = self.model.predict(self.test_data[0], verbose=0)

        correct = sum(
            1
            for pred, actual in zip(ypred, self.test_data[1])
            if (pred < 0 and actual < 0) or (pred > 0 and actual > 0)
        )
        accuracy = correct / len(self.test_data[1]) * 100
        return accuracy

    def predict_future(self, stock_list: list):
        predictions = []
        for ticker in stock_list:
            try:
                stock = Stock(ticker)
                df = stock.get_return_data()
                X = df.drop(columns=["Close", "Dividends", "Stock Splits", "Return"])

                last_60_days = X.iloc[-self.LOOKBACK :].values
                last_60_scaled = self.standard_scaler.transform(last_60_days)

                input_seq = last_60_scaled.reshape(1, self.LOOKBACK, -1)
                prediction = self.model.predict(input_seq, verbose=0)
                predictions.append({"ticker": ticker, "predicted_return": prediction})
            except Exception as e:
                print(f"Skipping {ticker}, not found: {e}")
        return predictions

    def save_weights(
        self,
    ):
        WEIGHTS_DIR.mkdir(parents=True, exist_ok=True)
        self.model.save(MULTI_WEIGHTS_DIR)
        print("Weights saved")

    def load_weights(
        self,
    ):
        self.model = load_model(MULTI_WEIGHTS_DIR)


if __name__ == "__main__":
    stock = Stock("saab")
    agent = MultiAgent(stock)

    history = agent.train_on_multiple(SWEDISH_STOCKS)
    predictions = agent.predict_future(SWEDISH_STOCKS)
