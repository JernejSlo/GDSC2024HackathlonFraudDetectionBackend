import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from Extra.DataProcessingUtils import DataProcessingUtils
from Extra.Loading.LoadCSV import LoadCSV
from Extra.Loading.LoadUtils import LoadUtils
from Extra.ServiceUtils import ServiceUtils
from ML.FraudDetectionModel import FraudDetectionModel
from Services.GeneralCalculationService import GeneralCalculationService


class UpdateFlaggedListService(GeneralCalculationService):
    """Description of the class"""


    def set_data(self, input_data):
        try:
            # all values that are strictly necessary, and the endpoint will not work without them
            all_values = ["transactions"]
            print()
            ServiceUtils.set_necessary_data(self, all_values, input_data)
            print(self.transactions)
        except Exception as e:
            print(e)
            raise Exception(f"Error happened when loading in the data. {e}")
        return self

    def updateUserModel(self):
        try:
            DataProcessingUtils("./Tests/transactions.csv","UserId","./Tests/users.csv").saveAndTrainModel(self.transactions)
        except Exception as e:

            raise e
        return {"Status": "Success", "Message": "The list of flagged transactions has been updated."}

    def calculate(self, *args, **kwargs):
        try:
            result = self.updateUserModel(*args, **kwargs)
        except Exception as e:
            raise Exception(str(e))
        return result

    def handle_service(self, dict, **kwargs):

        return self.set_data(dict).calculate(), {"Dictionary": "That holds the values that will be stored in the session data"}

