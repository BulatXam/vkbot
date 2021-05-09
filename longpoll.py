from event import convert_event

import requests

class GroupLongPoll:
    '''Longpoll работающий с помошью longpoll-сервера сообщества.'''
    def __init__(self, token):
        self.__token = token

        self.__connectLongPoll()   # Подключаем longpoll сразу с вызовом класса.

    def __connectLongPoll(self):
        '''Подключение longpoll.

        Вызывается метод groupsGetLongPollServer(),
        который выводит все данные о longpoll.'''
        longpoll = self.__token.groups.getLongPollServer() # вывод данных о настройке LongPoll.
        self.server = longpoll['server']                   # имя сервера на стороне ВК.
        self.key = longpoll['key']                         # ключ сервера.
        self.ts = longpoll['ts']                           # номер предыдущего запроса.
        self.wait = 25                                     # ожидание, сколько будет длиться длинный запрос.

        return longpoll

    def requestLongPoll(self, update_ts=True):
        '''Для работы с "длинными" запросами.

        Делаем запрос и если произошло событие, то сервер отправляет ответ, 
        а если ничего не произошло в течении указанного времени wait, то сервер отправляет "пустой" запрос.'''
        response = requests.get(f'{self.server}?act=a_check&key={self.key}&ts={self.ts}&wait={self.wait}').json()

        if update_ts:
            try:
                self.ts = response['ts']
            except KeyError:               # При большом количестве запросов, появляется ошибка "2" и идет перезапуск longpoll
                if response['failed'] == 2:
                    self.__connectLongPoll()
                    response = requests.get(f'{self.server}?act=a_check&key={self.key}&ts={self.ts}&wait={self.wait}').json()
        
        return [event for event in response['updates']]
            

    def listenEvents(self):
        '''Прослушивается сервер. 

        json превращается в объект класса события, которое произошло.'''
        while True:
            for event in self.requestLongPoll():
                yield convert_event(event)