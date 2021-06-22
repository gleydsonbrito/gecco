import numpy as np
import array
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from tensorflow.keras.layers.experimental import preprocessing
import tensorflow as tf


from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.callbacks import EarlyStopping

from storage import get_csv

X = []
Y = []

data = get_csv()

for i in data:
    X.append(i[0])
    Y.append(i[1])

X = np.array(X).reshape(-1, 1)
Y = np.array(Y).reshape(-1, 29)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)


def build_model():
    model = Sequential([
        Dense(64, activation='relu', input_shape=[len(X_train), 1]),
        Dense(64, activation='relu'),
        Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(
        loss='mse',
        optimizer=optimizer,
        metrics=['mae', 'mse']
    )

    return model


model = build_model()

earl_stop = EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(
    X_train,
    Y_train,
    epochs=200,
    validation_data=(X_test, Y_test),
    callbacks=earl_stop
)

loss, mae, mse = model.evaluate(X_test, Y_test, verbose=2)

print("Testing set Mean Abs Error: {:5.2f} MPG".format(mae))


def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch

    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [MPG]')
    plt.plot(hist['epoch'], hist['mae'],
             label='Train Error')
    plt.plot(hist['epoch'], hist['val_mae'],
             label='Val Error')
    plt.ylim([0, 5])
    plt.legend()

    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$MPG^2$]')
    plt.plot(hist['epoch'], hist['mse'],
             label='Train Error')
    plt.plot(hist['epoch'], hist['val_mse'],
             label='Val Error')
    plt.ylim([0, 20])
    plt.legend()
    plt.show()


plot_history(history)
