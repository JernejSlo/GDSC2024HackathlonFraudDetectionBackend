import json


class HandleReturn():

    def toJson(self,data):
        return json.loads(json.dumps(data))

    def handleError(self,error):
        return self.toJson({"status": "failure", "error": str(error)})