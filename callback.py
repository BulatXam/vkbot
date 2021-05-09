import json
from event import convert_event

class GroupCallback:
    def __init__(self, token, url, title):
        self.__token = token
        self.group_id = self.__token.groups.getById()['id']
        
        self.url = url
        self.title = title
        self.confirmation_code = self.__token.groups.getCallbackConfirmationCode(
            group_id = self.group_id
        )
        self.server_id = self.__addServer()


    def listenServer(self, raw, HttpResponse):
        if raw['type'] == 'confirm':
            return HttpResponse(self.confirmation_code, 200)
        else:
            return convert_event(raw)

    def __addServer(self):
        return self.__token.groups.addCallbackServer(
            group_id = self.group_id,
            url = self.url,
            title = self.title,
            secret_key = self.confirmation_code,
        )

    def getSettings(self):
        return self.__token.groups.getCallbackSettings(
            group_id = self.group_id,
            server_id = self.server_id,
        )

    def setSettings(**kwargs):
        return self.__token.groups.setSettings(**kwargs)