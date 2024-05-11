import numpy as np

from Extra.HandleReturn import HandleReturn
from Extra.ServiceUtils import ServiceUtils
from Services.GeneralCalculationService import GeneralCalculationService


class QueryFraudDetectorService(GeneralCalculationService):
    """Description of the class"""


    def set_data(self, input_data,session):
        try:
            # all values that are strictly necessary, and the endpoint will not work without them
            print("input_data", input_data, session)
            all_values = ["user_model", "transaction_history"]
            ServiceUtils.set_necessary_data(self, all_values, input_data)

            if "class_names" in input_data: self.classes = input_data["class_names"]
            else: self.classes = None

            # loading data from session or if there is no session
            if session is None:
                print("session is empty")
                raise Exception("Session wasn't assigned.")
            else:
                self.model = session["model"]
        except Exception as e:
            raise Exception(f"Error happened when loading in the data. {e}")
        return self

    def predictFraud(self):
        classes = self.classes
        data = np.asarray(self.transaction_history)
        predictions = self.model.predict(data)
        labels = []
        for prediction in predictions:
            pred = np.argmax(prediction)
            if (classes is not None and len(classes) >= pred):
                pred = classes[pred]
            labels.append(pred)

        return {"Prediction": labels}

    def calculate(self, *args, **kwargs):
        try:
            result = self.predictFraud(*args, **kwargs)
        except Exception as e:
            raise Exception(str(e))
        return result

    def handle_service(self, dict, **kwargs):
        # session data
        data = kwargs.get("data",None)

        return self.set_data(dict,data).calculate(), {"Dictionary": "That holds the values that will be stored in the session data"}

