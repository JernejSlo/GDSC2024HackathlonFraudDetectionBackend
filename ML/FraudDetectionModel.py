class FraudDetectionModel():
    """
        Parent class of the fraud detection model. Contains functions for fraud detection and model training.
    """
    def __init__(self, model_file):
        self.model = "load model here"

    def train(self,data, model_path, **kwargs):
        """
            This funtion handles training the model as well as saving the model weights.

            :param data: data to use to train the model.
            :param kwargs: additional parameters for new training or training using old weights.
            :return: status of the model training
        """
        # train model here

        return

    def predict(self,data):
        """
            This function is used for predicting whether a transaction is fraudulent by using a ml model.

            :param data: user data and transaction history used for predicting a transaction being fraudulent.
            :return:
        """
        # handle prediction here
        prediction = ""

        return prediction