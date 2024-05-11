"""Code for the flask app."""
import threading

from flask import Flask
from flask_restful import Api#, Resource, reqparse

import logging

from Extra.SessionManager import SessionManager
from Resources.QueryFraudDetectorResource import QueryFraudDetectorResource


def create_app(session_manager):
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(QueryFraudDetectorResource, '/detect_fraud',resource_class_args=[session_manager])
    #api.add_resource(TrainModelResource, '/train_model')

    return app

# sessions logic
model_path = ""
session_manager = SessionManager(model_path)

session_manager.initialize_fraud_detection_services(10)


logging.basicConfig(filename='record.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = create_app(session_manager)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)
    cleanup_thread = threading.Thread(target=session_manager.clear_sessions(), daemon=True)
    cleanup_thread.start()