import os

import tensorflow as tf
from tensorflow.keras import layers, models
class FraudDetectionModel():
    """
        Parent class of the fraud detection model. Contains functions for fraud detection and model training.
    """
    def __init__(self, weights_path, input_shape, num_classes=2):
        self.input_shape = input_shape
        self.num_classes = num_classes
        if os.path.exists(weights_path):
            print("Loading model from saved weights.")
            self.model = self.load_model(weights_path)
        else:
            print("No weights found. Creating a new model.")
            self.model = self.build_lstm_model()

    def build_lstm_model(self):
        model = models.Sequential([
            layers.LSTM(128, input_shape=self.input_shape, return_sequences=True),
            layers.Dropout(0.3),
            layers.LSTM(64, return_sequences=False),
            layers.Dropout(0.3),
            layers.Dense(32, activation='relu'),
            layers.Dropout(0.2),
            layers.Dense(self.num_classes, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def load_model(self, weights_path):
        model = self.build_lstm_model()  # Build the model structure
        model.load_weights(weights_path)  # Load the saved weights
        return model

    def save_model(self):
        # Save the entire model to a file
        self.model.save(self.weights_path)
        print("Model saved to", self.weights_path)
    def train(self, train_data, epochs=10, batch_size=32, validation_data=None):
        """
                    This funtion handles training the model as well as saving the model weights.

                    :param data: data to use to train the model.
                    :param kwargs: additional parameters for new training or training using old weights.
                    :return: status of the model training
                """
        # Assuming train_data is a TensorFlow dataset or a tuple (inputs, targets)
        try:
            self.model.fit(train_data, epochs=epochs, batch_size=batch_size, validation_data=validation_data)
        except Exception as e:
            raise e





    def predict(self,data):
        """
            This function is used for predicting whether a transaction is fraudulent by using a ml model.

            :param data: user data and transaction history used for predicting a transaction being fraudulent.
            :return:
        """
        # handle prediction here
        prediction = ""

        return prediction