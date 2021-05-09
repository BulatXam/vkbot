from models import Member
from models import Conversation

from vk_keyboard import Vk_Keyboard

import requests

class Bot:
    '''Работа с ботом.

    Тут собраны все команды бота.'''
    def __init__(self, token, group_id=None):
        self.__token = token
        if group_id == None:
            self.group_id = self.__token.groups.getById()['id']
        else:
            self.group_id = group_id

        self.commands = {
            # lvl-0
            # 'Бот скажи мем':(self.meme, 0)
            #lvl-1

            #lvl-2

            #lvl-3

            #lvl-4
 
            #lvl-5

            #lvl-6

            #lvl-7

            #lvl-8

            #lvl-9

            #lvl-10
        }

    def in_commands(self, message, command_text=None, level=0):
        if command_text:
            command = command_text.capitalize()
        else:
            command = message.text.capitalize()

        commands_list = [*self.commands]
        if command in commands_list:
            if int(level) >= self.commands[command][1]:
                # Если подходит по уровню, то вызывается команда и
                # отправляется сообщение с текстом, что вернула функция.
                self.__token.messages.send(
                    peer_id=event.peer_id,
                    message=self.commands[command][0](message),
                )
            else:
                self.__token.messages.send(
                    peer_id=message.peer_id,
                    message='Маловат еще для такого',
                    random_id=0,
                )