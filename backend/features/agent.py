import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

from backend.components.stock import Stock


class Agent:
    def __init__(self, stock: Stock):
        self.X, self.y = stock.df.drop(columns=["Close"]), stock.df["Close"]
        self.input_shape = self.X.shape[1:]
        self.learning_rate = 0.001
        self.model = self._create_model()
        self.train_data = None
        self.test_data = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

        self.standard_scaler = StandardScaler()

    def _create_model(self):
        model = Sequential()
        model.add(Flatten(input_shape=self.input_shape))
        model.add(Dense(64, activation="relu"))
        model.add(Dense(64, activation="relu"))
        model.add(Dense(1, activation="linear"))

        model.compile(loss="mse", optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def scaler(self, X, y):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )
        X_train_scaled = self.standard_scaler.fit_transform(self.X_train)
        X_test_scaled = self.standard_scaler.transform(self.X_test)
        self.train_data = (X_train_scaled, self.y_train)
        self.test_data = (X_test_scaled, self.y_test)

    def train(self):
        self.scaler(self.X, self.y)
        self.model.fit(
            self.train_data[0], self.train_data[1], epochs=100, batch_size=32, verbose=0
        )

    def predict(
        self,
    ):
        return self.model.predict(self.test_data, verbose=0)

    def predict_future(self, market, days=7):
        difs = [high - low for high, low in zip(market.df["High"], market.df["Low"])]
        volumes = [
            np.random.randint(market.df["Volume"].min(), market.df["Volume"].max())
            for i in range(days)
        ]

        latest_day = self.X.iloc[-1].values.reshape(1, -1)

        latest_scaled = self.standard_scaler.transform(latest_day)

        new_predictions = []

        for i in range(days):
            price = self.model.predict(latest_scaled)
            new_predictions.append(price)

            high = np.random.uniform(latest_day[0][1], latest_day[0][1] + difs[i])
            low = np.random.uniform(latest_day[0][2], latest_day[0][2] - difs[i])
            latest_day = np.array([[price[0][0], high, low, volumes[i]]])

            latest_scaled = self.standard_scaler.transform(latest_day)

        return np.array(new_predictions).flatten()
