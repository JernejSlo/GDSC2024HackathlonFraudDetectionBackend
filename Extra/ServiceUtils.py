class ServiceUtils():

    def set_necessary_data(self,arr,input_data):
        for value in arr:
            if value not in input_data:
                raise Exception(f"{value} missing from request")
            else:
                setattr(self, value, input_data[value])