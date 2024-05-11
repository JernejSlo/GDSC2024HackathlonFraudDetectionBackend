import string
import random
import threading
from datetime import datetime

from ML.FraudDetectionModel import FraudDetectionModel


class SessionManager(object):

    def __init__(self, model_path):
        self.sessions = {}
        self.model_path = model_path
        self.lock = threading.Lock()

    def get_random_string(self,length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def get_session(self,session_id):
        with self.lock:
            return self.sessions.get(session_id)

    def initialize_fraud_detection_services(self,n, input_shape, num_classes):
        for i in range(n):
            session_id = self.get_random_string(5)
            data = {"model": FraudDetectionModel(self.model_path,input_shape,num_classes)}
            session = {"owner": "", "data": data,"running": False,"disabled": False}
            print(session)
            self.sessions[session_id] = session

    def assign_session(self, user_session_id):
        for key in self.sessions:
            with self.lock:
                session = self.sessions[key]
                if not session["running"] and not session["disabled"]:
                    self.sessions[key]["owner"] = user_session_id
                    self.sessions[key]["running"] = True
                    self.sessions[key]["data"]["context_loaded"] = True
                    return session, key
        raise ValueError("All sessions are currently busy, please try again later.")

    def un_assign_session(self,user_session_id):
        for key in self.sessions:
            with self.lock:
                session = self.sessions[key]
                owner = session["owner"]
                if owner == user_session_id:
                    self.sessions[key]["owner"] = ""
                    self.sessions[key]["running"] = False
                    self.sessions[key]["data"]["context_loaded"] = False
                    print("Session was successfully freed up.")
                    break

    def check_session_present(self, user_session_id):
        for key in self.sessions:
            with self.lock:
                session = self.sessions[key]
                owner = session["owner"]
                if owner == user_session_id:
                   return session,key
        return None,None

    def set_shared_session_status(self,session_id, running):
        with self.lock:
            self.sessions[session_id]["running"] = running