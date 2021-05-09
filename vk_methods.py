class Wall:
    def __init__(self, token):
        self.__token = token

    def post(self, owner_id, message, from_group=0, guid=0):
        return self.__token.api_method(
            method='wall.post',
            owner_id=owner_id,
            message=message,
            guid=guid,
            from_group=from_group,
        )

    def get(self, owner_id=None, domain=None, offset=None, 
        count=10, filter=None, extended=None, fields=None):
        return self.__token.api_method(
            method='wall.get',
            owner_id=owner_id,
            count=count,
        )

class Photos:
    def __init__(self, token):
        self.__token = token

    def getUploadServer(self, album_id, group_id=None):
        return self.__token.api_method(
            method='photos.getUploadServer',
            album_id=album_id,
            group_id=group_id
        )

    def getMessagesUploadServer(self, peer_id):
        return self.__token.api_method(
            method='photos.getMessagesUploadServer',
            peer_id=peer_id
        )

    def saveMessagesPhoto(self, photo, server, hash):
        return self.__token.api_method(
            method='photos.saveMessagesPhoto',
            photo=photo,
            server=server,
            hash=hash,
        )

    def getChatUploadServer(self, chat_id, crop_x, crop_y, crop_width):
        return self.__token.api_method(
            method='photo.getChatUploadServer',
            chat_id=chat_id,
            crop_x=crop_x,
            crop_y=crop_y,
            crop_width=crop_width,
        )

    def save(self, album_id, server, photos_list, hash, caption=None, 
        latitude=None, longitude=None, group_id=None):
        return self.__token.api_method(
            method='photos.save',
            album_id=album_idm,
            server=server,
            photos_list=photos_list,
            caption=caption,
            hash=hash,
            latitude=latitude,
            longitude=longitude,
            group_id=group_id,
        )

class Accounts:
    '''Работа с аккаунтом.'''

    def __init__(self, token):
        self.__token = token

    def getInfo(self):
        return self.__token.api_method(method='account.getInfo')

    def getProfileInfo(self):
        return self.__token.api_method(method='account.getProfileInfo')


class Groups:
    '''Для работы с сообществами.'''
    def __init__(self, token, group_id=None):
        self.__token = token

    def getById(self, group_id=None):

        return self.__token.api_method(method='groups.getById')

    def getLongPollServer(self, group_id=None):
        if group_id is None:
            group_id = self.__token.api_method(method='groups.getById')['id']

        longpoll = self.__token.api_method(
            'groups.getLongPollServer', group_id=group_id)
        return longpoll['response']

    def getLongPollSettings(self, group_id=None):
        if group_id is None:
            group_id = self.__token.api_method(method='groups.getById')['id']

        longpoll = self.__token.api_method(
            method='groups.getLongPollSettings', group_id=group_id)
        return longpoll['response']

    def addCallbackServer(self, url, title, secret_key, group_id=None):
        return self.__token.api_method(
            method="groups.addCallbackServer", 
            url=url, 
            title=title, 
            secret_key=secret_key, 
            group_id=group_id
        )

    def deleteCallbackServer(self, server_id, group_id=None):
        return self.__token.api_method(
            method="groups.deleteCallbackServer", 
            server_id=server_id, 
            group_id=group_id
        )

    def editCallbackServer(self, server_id, url, title, 
        secret_key, group_id=None):
        return self.__token.api_method(
            method="groups.editCallbackServer", 
            server_id=server_id, 
            url=url, 
            title=title, 
            secret_key=secret_key, 
            group_id=group_id
        )

    def getCallbackConfirmationCode(self, group_id=None):
        return self.__token.api_method(
            method="groups.getCallbackConfirmationCode", 
            group_id=group_id
        )

    def getCallbackServers(self, server_ids, group_id=None):
        return self.__token.api_method(
            method="groups.getCallbackServer", 
            server_ids=server_ids, 
            group_id=group_id
        )

    def getCallbackSettings(self, server_id, group_id=None):
        return self.__token.api_method(
            method="groups.getCallbackServerSettings", 
            server_id=server_id, 
            group_id=group_id
        )

    def setCallbackSettings(self, server_id, api_version, message_new=0):
        return self.__token.api_method(
            method="groups.getCallbackServerSettings", 
            server_id=server_id, 
            api_version=api_version, 
            message_new=message_new
        )


class Messages:
    '''Работа с сообщениями.'''
    def __init__(self, token):
        self.__token = token

    def send(self, message, reply_to=None, attachment=None,
            user_id=None, forward_messages=None, forward=None,
            peer_id=None, sticker_id=None, content_source=None,
            random_id=0, keyboard=None):
        return self.__token.api_method(
            method='messages.send', 
            user_id=user_id, 
            peer_id=peer_id, 
            random_id=random_id, 
            message=message,
            attachment=attachment,
            reply_to=reply_to,
            forward=forward,
            forward_messages=forward_messages,
            sticker_id=sticker_id,
            content_source=content_source,
            keyboard=keyboard,
        )

    def sendMessageEventAnswer(self, event_id, user_id, peer_id, event_data):
        return self.__token.api_method(
            method='messages.sendMessageEventAnswer',
            event_id=event_id,
            user_id=user_id,
            peer_id=peer_id,
            event_data=event_data,
        )

    def delete(self, message_ids, group_id=None, spam=0, delete_for_all=1):
        return self.__token.api_method(
            method='messages.delete',
            message_ids=message_ids,
            group_id=group_id,
            spam=spam,
            delete_for_all=delete_for_all # 1-удалить для всех, 0-для себя.
        )

    def restore(self, message_id, group_id=None):
        return self.__token.api_method(
            method='messages.restore',
            message_id=message_id,
            group_id=group_id
        )

    def getLongPollServer(self, need_pts=0, group_id=None, ip_v=3):
        response = self.__token.api_method(
            method='messages.getLongPollServer',
            need_pts=need_pts,
            group_id=group_id,
            ip_v=ip_v
        )
        return response['response']


    def pin(self, peer_id, message_id, conversation_message_id):
        return self.__token.api_method(
            method='messages.pin',
            peer_id=peer_id,
            message_id=message_id,
            conversation_message_id=conversation_message_id,
        )

    def unpin(self, peer_id, group_id=None):
        return self.__token.api_method(
            method='messages.pin',
            peer_id=peer_id,
            group_id=group_id
        )

    def addChatUser(self, chat_id, user_id, visible_messages_count=0):
        '''Добавление юзера в чат.'''
        return self.__token.api_method(
            method='messages.addChatUser', 
            chat_id=chat_id, 
            user_id=user_id, 
            visible_messages_count=visible_messages_count
        )


    def deleteChatPhoto(self, chat_id, group_id=None):
        return self.__token.api_method(
            method='messages.deleteChatPhoto',
            chat_id=chat_id,
            group_id=group_id,
        )

    def editChat(self, chat_id, title):
        return self.__token.api_method(
            method='messages.editChat',
            chat_id=chat_id,
            title=title,
        )

    def getByConversationMessageId(self, peer_id, conversation_message_ids,
        fields=None, extended=0, group_id=None):
        return self.__token.api_method(
            method='messages.ConversationMessageId',
            peer_id=peer_id,
            conversation_message_ids=conversation_message_ids,
            fields=fields,
            extended=extended,
            group_id=group_id,
        )

    def getChat(self, chat_id, chat_ids=None, fields=None, name_case=None):
        return self.__token.api_method(
            method='messages.getChat',
            chat_id=chat_id,
            chat_ids=chat_ids,       # список идентификаторов бесед.
            fields=fields,           # список дополнительных полей профилей.
            name_case=name_case,     # падеж для склонения имени и фамилии.
        )


    def getChatPreview(self, peer_id, link, fields):
        return self.__token.api_method(
            method='messages.getChatPreview',
            peer_id=peer_id,               
            link=link,
            fields=fields,
        )


    def getConversationMembers(self, peer_id, offset=0, count=20, 
        extended=0, fields=None, group_id=None):
        return self.__token.api_method(
            method='messages.getConversationMembers',
            peer_id=peer_id,
            offset=offset,
            count=count,             # макс. кол-во результатов.
            extended=extended,       # возвращать ли дополнительные поля.
            fields=fields,           # доп. поля профилей.
            group_id=group_id,
        )

    def getConversation(self, start_message_id, offset=0, count=20, 
        filter='all', extended=0, fields=None, group_id=None):
        return self.__token.api_method(
            method='messages.getConversation',
            start_message_id=start_message_id,
            offset=offset,
            count=count,
            filter=filter,
            extended=extended,
            fields=fields,
            group_id=group_id,
        )

    def getConversationsById(self, peer_ids, extended=None, 
        fields=None, group_id=None):
        return self.__token.api_method(
            method='messages.getConversationsById',
            peer_ids=peer_ids,
            extended=extended,
            fields=fields,
            group_id=group_id,
        )

    def getHistoryMessage(self, user_id, peer_id, rev=1, extended=0, fields=None, 
        group_id=None, offset=-1, count=10, start_message_id=-1):
        return self.__token.api_method(
            method='message.getHistory', 
            offset=offset, count=count, 
            user_id=user_id, 
            start_message_id=start_message_id
        )

    def getHistoryAttachments(self, peer_id, start_from, count, 
        media_type=None, photo_sizes=None, fields=None, group_id=None, 
        preserve_order=None, max_forwards_level=None):
        return self.__token.api_method(
            method='message.getHistoryAttachments',
            peer_id=peer_id,
            start_from=start_from,
            count=count,
            media_type=media_type,
            photo_sizes=photo_sizes,
            fields=fields,
            group_id=group_id,
            preserve_order=preserve_order,
            max_forwards_level=max_forwards_level
        )

    def getInviteLink(self, peer_id, reset=0, group_id=None):
        return self.__token.api_method(
            method='messages.getInviteLink',
            peer_id=peer_id,
            reset=reset,
            group_id=group_id,
        )

    def removeChatUser(self, chat_id, user_id, member_id):
        '''Выкинуть юзера из диалога.

        member_id брать из пересленных сообщений.'''
        return self.__token.api_method(
            method='messages.removeChatUser',
            chat_id=chat_id,
            user_id=user_id,
            member_id=member_id,
        )

    def setChatPhoto(self, file):
        return self.__token.api_method(
            method='messages.setChatPhoto',
            file=file,
        )


class Users:
    def __init__(self, token):
        self.__token = token

    def get(self, user_ids, fields, name_case=None):
        return self.__token.api_method(
            method='users.get',
            user_ids=user_ids,
            fields=fields,
            name_case=name_case,
        )