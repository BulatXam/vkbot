# Для загрузки медиа в вк.
import requests

class Vk_Upload:
    def __init__(self, token):
        self.__token = token

    def photo_messages(self, photo, peer_id):
        upload_server = self.__token.photos.getMessagesUploadServer(
            peer_id=peer_id
        )['response']

        data = {'photo':('photo.jpg', photo, 'image/jpg')}
        response_photo = requests.post(
            url=upload_server['upload_url'], 
            files=data,
        ).json()

        save_photo = self.__token.photos.saveMessagesPhoto(
            server = response_photo['server'],
            photo = response_photo['photo'],
            hash = response_photo['hash'],
        )

        try:
            photo_result = f"photo{save_photo['owner_id']}_{save_photo['id']}"
            return photo_result
        except KeyError:
            return ValueError('Неправильное значение photo')

        return save_photo