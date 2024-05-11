
from flask_restful import Resource

from Extra.HandleReturn import HandleReturn


class GeneralResource(Resource):

    def returnResult(self, func, data):
        try:
            result = func(data)
            return HandleReturn().toJson(result)
        except Exception as e:
            return HandleReturn().handleError(e)