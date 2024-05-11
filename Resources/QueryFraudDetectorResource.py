from flask import request

from Services.SessionSharingResource import SessionSharingResource
from Services.QueryFraudDetectorService import QueryFraudDetectorService


class QueryFraudDetectorResource(SessionSharingResource):
    """Describe what this endpoint does."""
    def __init__(self,session_manager) -> None:
        super().__init__(session_manager)

        # Inject all dependencies for resource in constructor
        self.calc = QueryFraudDetectorService()


    def post(self):
        """Process post request."""
        return self.returnResult(self.calc.handle_service, request.json)