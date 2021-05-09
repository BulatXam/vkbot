import json

def convert_event(event):
    event = Event(event)
    if event.event_type == 'message_new':
        return MessageNewEvent()
    elif event.event_type == 'message_event':
        return MessageEventEvent()
    else:
        raise ValueError('the event is missing')

class Event:
    '''Базовое событие longpoll`a.

    В нем собран сырой json, тип события и объект, который он несет.'''
    def __init__(self, raw):
        self.raw = raw

        try:
            self.event_type = self.raw['type']
            self.object = self.raw['object']
        except TypeError:
            self.event_type = None
            self.object = None


class MessageEventEvent(Event):
    '''Событие callback.'''
    def __init__(self):
        self.user_id = self.object['user_id']
        self.peer_id = self.object['peer_id']
        self.event_id = self.object['event_id']
        self.payload = self.object['payload']
        self.conversation_message_id = self.object['conversation_message_id']
        self.chat_id = self.peer_id - int(2E9)


class MessageNewEvent(Event):
    '''Событие нового сообщения.'''
    def __init__(self):
        self.from_user = False
        self.from_chat = False
        self.from_group = False
        self.chat_id = None

        self.message = self.object['message']

        self.user_id = self.message['from_id']
        self.peer_id = self.message['peer_id']
        self.text = self.message['text']
        self.id = self.message['id']
        self.attachments = self.message['attachments']       # Вложения (аудио, картинки, файл, документ и т.д)
        self.conversation_message_id = self.message['conversation_message_id']
        try:
            self.is_important = self.message['important']
            self.fwd_messages = self.message['fwd_messages'] # Пересленные сообщения(если существуют)
        except KeyError:
            self.is_important = None
            self.is_important = None

        try:
            self.reply_message = MessageNewEvent(message=self.message['reply_message'])   # ответное сообщение.
        except KeyError:
            self.reply_message = None

        try:
            self.action = self.message['action']
            self.action_type = self.action['type']
            self.member_id = self.action['member_id']
        except:
            self.action = None

        if self.peer_id < 0:
            self.from_group = True
        elif self.peer_id < int(2E9):                                          # с 2Е9(дифферинциально) начинается отсчет peer_id для групп. 
            self.from_user = True
        else:
            self.from_chat = True
            self.chat_id = self.peer_id - int(2E9)

    def is_new_user(self):
        if self.action:
            if self.action_type == 'chat_invite_user':
                return True

    def is_kick_user(self):
        if self.action:
            if self.action_type == 'chat_kick_user':
                return True

    def is_dont_pass_sencorship(self):
        pass