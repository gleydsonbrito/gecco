import numpy as np
import array
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from tensorflow.keras.layers.experimental import preprocessing


from keras.models import Sequential
from keras.layers import Dense, Flatten

from storage import get_csv

X = []
Y = []

data = get_csv()

for i in data:
    X.append(i[0])
    Y.append(i[1])

X = np.array(X).reshape(-1, 1)
Y = np.array(Y).reshape(-1, 29)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10)

# normalize = preprocessing.Normalization()
# normalize.adapt(X_train)

model = Sequential([
    # normalize,
    Dense(1, activation='sigmoid'),
    Dense(16, activation='relu'),
    Dense(32, activation='relu'),
    Dense(64, activation='sigmoid'),
    Dense(128, activation='relu'),
    Dense(29, activation='relu')
])

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(X_train, Y_train,
                    validation_data=(X_test, Y_test),
                    epochs=200)

_, accuracy = model.evaluate(X_test, Y_test, verbose=1)
print('Accuracy: %2f', (accuracy))

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Acurácia')
plt.ylabel('Acurácia')
plt.xlabel('Épocas')
plt.legend(['Treinamento', 'Teste'], loc='lower right')
print(history.history.keys())
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Erro')
plt.ylabel('Loss')
plt.xlabel('Épocas')
plt.legend(['Treinamento', 'Teste'], loc='upper right')
plt.show()
