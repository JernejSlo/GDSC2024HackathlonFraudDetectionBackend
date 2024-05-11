from flask_restful import Resource

from Extra.HandleReturn import HandleReturn


class SessionSharingResource(Resource):

    def __init__(self,session_manager):
        self.session_manager = session_manager

    def assign_session(self, user_session_id):
        return self.session_manager.assign_session(user_session_id)

    def un_assign_session(self, user_session_id):
        return self.session_manager.un_assign_session(user_session_id)

    def check_session_status(self, user_session_id):
        return self.session_manager.check_session_present(user_session_id)

    def set_session_active(self, user_session_id):
        self.session_manager.set_shared_session_status(user_session_id, True)

    def set_session_inactive(self, user_session_id):
        self.session_manager.set_shared_session_status(user_session_id, False)

    def returnResult(self, func, data_):
        try:
            user_session_id = data_['user_session_id']
            session, self.session_id = self.check_session_status(user_session_id)
            if session is None:
                self.session, self.session_id = self.assign_session(user_session_id)
                data, session_data = func(data_, data=self.session["data"])
                print("This session was assigned", self.session)
            else:
                self.set_session_active(self.session_id)
                data, session_data = func(data_, data=session["data"])
            self.un_assign_session(self.session_id)
            return HandleReturn().toJson(data)
        except Exception as e:
            return HandleReturn().handleError(str(e))