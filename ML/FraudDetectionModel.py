import os

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, Input
class FraudDetectionModel():
    """
        Parent class of the fraud detection model. Contains functions for fraud detection and model training.
    """
    def __init__(self, weights_path, input_shape,user_model_input_shape, num_classes=2):
        self.input_shape = input_shape
        self.user_model_input_shape = user_model_input_shape
        self.num_classes = num_classes
        if os.path.exists(weights_path):
            print("Loading model from saved weights.")
            self.model = self.load_model(weights_path)
        else:
            print("No weights found. Creating a new model.")
            self.model = self.build_lstm_model()

    def build_lstm_model(self):

        # Define the input for the time series data
        time_series_input = Input(shape=self.input_shape, name='time_series_input')

        # Define the input for the user model data
        # Assume user_model_input_shape is defined based on your user model data
        user_model_input = Input(shape=self.user_model_input_shape, name='user_model_input')

        # Processing time series data through LSTM layers
        x = layers.LSTM(128, return_sequences=True)(time_series_input)
        x = layers.Dropout(0.3)(x)
        x = layers.LSTM(64, return_sequences=False)(x)
        x = layers.Dropout(0.3)(x)

        # Combine the output of LSTM with the user model input
        # Use layers.concatenate to merge the outputs along the last dimension
        combined = layers.concatenate([x, user_model_input])

        # Fully connected layers
        x = layers.Dense(32, activation='relu')(combined)
        x = layers.Dropout(0.2)(x)
        output = layers.Dense(self.num_classes, activation='sigmoid')(x)

        # Create the model by specifying the inputs and outputs
        model = models.Model(inputs=[time_series_input, user_model_input], outputs=output)
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        return model

    def load_model(self, weights_path):
        model = self.build_lstm_model()  # Build the model structure
        model.load_weights(weights_path)  # Load the saved weights
        return model

    def save_model(self, model_weights):
        # Save the entire model to a file
        model_w = model_weights
        if model_w.split(".")[-1] != "keras":
            model_w += ".keras"
        self.model.save(model_w)
        print("Model saved to", model_w)
    def train(self, X_train, X_val, y_train, y_val, user_model_train,user_model_val, epochs=10, batch_size=32, validation_data=None):
        """
            This function handles training the model using NumPy arrays and also saves the model weights.

            :param train_data: Training data as a tuple (inputs, targets) where both are NumPy arrays.
            :param epochs: Number of epochs to train for.
            :param batch_size: Size of batches to use during training.
            :param validation_data: Validation data as a tuple (inputs, targets) where both are NumPy arrays.
            :return: Training history, containing details like loss and accuracy per epoch.
        """
        try:
            self.model.summary()
            history = self.model.fit(
                x=[X_train, np.asarray(user_model_train)],  # Input features reshaped for LSTM
                y=y_train,  # Corresponding targets
                epochs=10,
                batch_size=32,
                validation_data=([X_val, user_model_val], y_val)
            )
            return history
        except Exception as e:
            print("Model failed during training.")
            raise e






    def predict(self,data):
        """
            This function is used for predicting whether a transaction is fraudulent by using a ml model.

            :param data: user data and transaction history used for predicting a transaction being fraudulent.
            :return:
        """
        # handle prediction here
        predictions = self.model.predict(data)

        return predictions