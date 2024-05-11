import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from Extra.Loading.LoadCSV import LoadCSV
from Extra.Loading.LoadUtils import LoadUtils
from Extra.ServiceUtils import ServiceUtils
from ML.FraudDetectionModel import FraudDetectionModel
from Services.GeneralCalculationService import GeneralCalculationService


class TrainModelService(GeneralCalculationService):
    """Description of the class"""


    def set_data(self, input_data,session):
        try:
            # all values that are strictly necessary, and the endpoint will not work without them
            all_values = ["data_path", "model_weights", "num_classes", "input_shape", "target_column", "window_size", "group_by"]
            ServiceUtils.set_necessary_data(self, all_values, input_data)
        except Exception as e:
            raise Exception(f"Error happened when loading in the data. {e}")
        return self

    def trainModel(self):
        try:
            loader = LoadCSV()
            X, y = loader.parse_data_series_csv(self.data_path, self.group_by, self.window_size,self.target_column,self.num_classes)
            print(len(y),len(X))

            X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
            X_train, X_val, y_train, y_val = np.array(X_train),np.array(X_val),np.array(y_train),np.array(y_val),
            model = FraudDetectionModel(self.model_weights, self.input_shape, self.num_classes)
            model.train(X_train, X_val, y_train, y_val)
            model.save_model(self.model_weights)
        except Exception as e:
            print(e)
            raise e
        return {"Status": "Success", "Message": "Model trained successfully."}

    def calculate(self, *args, **kwargs):
        try:
            result = self.trainModel(*args, **kwargs)
        except Exception as e:
            raise Exception(str(e))
        return result

    def handle_service(self, dict, **kwargs):
        # session data
        data = kwargs.get("data",None)

        return self.set_data(dict,data).calculate(), {"Dictionary": "That holds the values that will be stored in the session data"}

