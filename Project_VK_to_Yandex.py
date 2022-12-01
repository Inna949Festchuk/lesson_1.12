with open('token.txt', 'r') as file_object:
    token_vk = file_object.read().strip()
    
import time
import requests
from pprint import pprint

class VkFoto:
    url = 'https://api.vk.com/method/photos.get'
    def __init__(self, token_vk, version='5.131'):
        self.params = {
            'access_token': token_vk,
            'v': version    
        }
    def profile_fotos(self, owner_id=457689717):
        '''
        owner_id — идентификационный номер владельца аккаунта ВКонтакте
        amount_foto  - количество выгружаемых фото максимального размера
        '''
        profile_fotos_params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': True,
            'photo_sizes': True,
            'count': 1000
        }
        response = requests.get(self.url, params={**self.params, **profile_fotos_params}).json()
        return response

vk_foto_1 = VkFoto(token_vk, '5.131')
count_z = vk_foto_1.profile_fotos()['response']['count']

for i in range(int(count_z)):
    print(f'Число фотографийв профиле: {count_z}, это {i + 1} фотография.')
    # Получаем контент с сылкой на фото
    dicts_foto_1 = vk_foto_1.profile_fotos()['response']['items'][i]['sizes']
    # pprint (dicts_foto_1)
    # # Получаем дату добавления фото в профиль
    # date_foto_1 = vk_foto_1.profile_fotos()['response']['items'][i]['date']
    # pprint(date_foto_1)
    # Получаем количество лайкосов фотки профиля
    # likes_foto_1 = vk_foto_1.profile_fotos()['response']['items'][i]['likes']['count']
    # pprint(likes_foto_1)

    # Dictionary Comprehension (словарное включение)
    ''' Делаем новый словарь с ключом - размер фото 
        Делаем из нового словаря список и ...
        сортируем этот список по размеру фото и по убыванию
        Выбираем три ссылки на фото для сохранения на яндекс '''
    dct = {v['height'] * v['width']:v['url'] for v in dicts_foto_1}
    sort_dct = dict(sorted(dct.items(), reverse=True)[0:2])
    pprint (sort_dct)

import json
with open ('metadates.json', 'w') as outfile:
    js = [{ "file_name": "34.jpg", "size": "z"}]
    json.dump(js, outfile, indent=2)
