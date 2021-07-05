import numpy as np
import tensorflow as tf
import pandas as pd

model = tf.keras.Sequential([
  tf.keras.layers.Dense(1, input_shape=(4,), activation='sigmoid')
])
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['binary_accuracy'])

model.save("creditDataModel")