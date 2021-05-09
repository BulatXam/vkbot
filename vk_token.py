import requests

from vk_methods import Groups
from vk_methods import Messages
from vk_methods import Users
from vk_methods import Wall
from vk_methods import Accounts
from vk_methods import Photos

class Vk_Token:
    '''Токен вк.

    Токен будет аргументом для классов, которые работают с api вк.

    В классе есть метод api_method, он составляет основной запрос к серверу ВК, 
    например чтобы написать сообщение, надо составить запрос вида:
    https://api.vk.com/method/messages.send?user_id={user_id}&message={message_text}&peer_id={peer_id}&random_id={random_id}&access_token={access_token}&v=5.52,

    messages.send-это метод api, то есть то, что надо сделать серверу ВК,

    user_id, message, peer_id, random_id-это аргументы, которые надо передать серверу в урле, 
    я реализовал это с помощью **kwargs, смотри описание метода api_method.

    access_token, v-это аргументы, которые по дефолту должны быть в каждом методе, где нужны права доступа, 
    можно увидеть что они не добавлену к списку arguments и не итерируются, а просто добавлены в строку.'''
    def __init__(self, access_token=None, v='5.130'):
        super(Vk_Token, self).__init__()
        self.__access_token = access_token   # токен вк, с правами доступа.
        self.__v = v                         # версия api.
        self.groups = Groups(self)
        self.messages = Messages(self)
        self.users = Users(self)
        self.wall = Wall(self)
        self.accounts = Accounts(self)
        self.photos = Photos(self)

    def api_method(self, method, type='GET', **kwargs):
        '''Метод токена, в котором составляется основной запрос.

        method-метод api
        **kwargs-аргументы к методу api
        type-тип запроса, (GET, POST, DELETE, PUT(ин) и т.д.)

        Все аргументы храняется в списке arguments, которая составляется путем итерации **kwargs,
        и так как kwargs-это словарь, то мы просто составляем список с объектами ['ключ аргумента=значение аргумента', '....']
        если же значение аргумента == None, то он просто не записывается в список.

        Дальше мы соединяем все эти объекты списка, а между объектами списка ставим знак &,
        сделал все с помощью метода join в питоне из коробки.'''
        arguments = [(f"{key}={value}") for key, value in kwargs.items() if value is not None]
        if type == 'GET':
            request = requests.get(f"https://api.vk.com/method/{method}?v={self.__v}&access_token={self.__access_token}&{'&'.join(arguments)}")
        else:
            request = requests.post(f"https://api.vk.com/method/{method}?v={self.__v}&access_token={self.__access_token}&{'&'.join(arguments)}")

        try:
            return request.json()['response'][0]
        except:
            return request.json()