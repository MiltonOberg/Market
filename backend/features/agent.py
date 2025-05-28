import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam


class Agent:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.input_shape = self.X.shape[1:]
        self.learning_rate = 0.001
        self.model = self._create_model()
        self.train_data = None
        self.test_data = None

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
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )
        X_train_scaled = self.standard_scaler.fit_transform(X_train)
        X_test_scaled = self.standard_scaler.transform(X_test)
        self.train_data = (X_train_scaled, y_train)
        self.test_data = (X_test_scaled, y_test)

    def train(self, X, y):
        self.scaler(X, y)
        self.model.fit(
            self.train_data[0], self.train_data[1], epochs=100, batch_size=32, verbose=1
        )

    def predict(
        self,
    ):
        return self.model.predict(self.test_data, verbose=0)

    def predict_feature(self, days=7):
        latest_day = self.X.iloc[-1].values.reshape(1, -1)

        latest_scaled = self.standard_scaler.transform(latest_day)

        new_predictions = []

        for i in range(days):
            price = self.model.predict(latest_scaled)
            new_predictions.append(price)

            new_input = latest_day.copy()
            new_input[0][0] = price

            latest_scaled = self.standard_scaler.transform(new_input)
            latest_day = new_input

        return np.array(new_predictions).flatten()
