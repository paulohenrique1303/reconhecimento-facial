import tensorflow as tf
import keras

model = keras.models.Sequential([
    keras.layers.Conv2D(32, (3,3), activation= 'relu'),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Conv2D(64, (3,3), activation= 'relu'),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation= 'relu'),
    keras.layers.Dense(60, activation= "softmax")
])


model.compile(
    optimizer= 'adam',
    loss = 'categorical_crossentropy',
    metrics= ['accuracy']
)

model.fit
