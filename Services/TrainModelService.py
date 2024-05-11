from Extra.ServiceUtils import ServiceUtils
from Services.GeneralCalculationService import GeneralCalculationService


class TrainModelService(GeneralCalculationService):
    """Description of the class"""


    def set_data(self, input_data,session):
        try:
            # all values that are strictly necessary, and the endpoint will not work without them
            all_values = ["model_path", "data_path", "model_weights"]
            ServiceUtils.set_necessary_data(self, all_values, input_data)
        except Exception as e:
            raise Exception(f"Error happened when loading in the data. {e}")
        return self

    def trainModel(self):


        return {"Dictionary": " is the result"}

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

