from flask import request

from Resources.GeneralResource import GeneralResource
from Services.SessionSharingResource import SessionSharingResource
from Services.QueryFraudDetectorService import QueryFraudDetectorService
from Services.TrainModelService import TrainModelService


class TrainModelResource(GeneralResource):
    """Describe what this endpoint does."""
    def __init__(self) -> None:
        super().__init__()

        # Inject all dependencies for resource in constructor
        self.calc = TrainModelService()


    def post(self):
        """Process post request."""
        return self.returnResult(self.calc.handle_service, request.json)