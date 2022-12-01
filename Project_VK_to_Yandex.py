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

    def profile_fotos(self, owner_id=764412154):
        '''
        owner_id — идентификационный номер владельца аккаунта ВКонтакте
        amount_foto  - количество выгружаемых фото максимального размера
        '''
        profile_fotos_params = {
            'album_id': 'profile',
            'rev': '0',
            'extended': '1',
            'photo_sizes': '1'
        }
        req = requests.get(self.url, params={**self.params, **profile_fotos_params}).json()
        return req['response']['items'][0]['sizes']
        
vk_foto_1 = VkFoto(token_vk, '5.131')
dicts_foto = vk_foto_1.profile_fotos()
# pprint(dicts_foto)

# i = 0
# for dict_foto in dicts_foto:
#     size_foto = dict_foto['height'] * dict_foto['width']
# #     size_dict = {size_foto:dicts_foto[i]} # Делаем новый словарь с ключом - размер фото 
# #     # lst.append(list(size_dict.items())) # Делаем из нового словаря список и ...
# #     sorted_size_list = dict(sorted((size_dict.items()), reverse=True)) # ... сортируем этот список по размеру фото и по убывагнию
    
# #     i += 1
# # pprint(size_dict)
# # pprint(sorted_size_list[0:4]) #Выбираем с последние четыре фото для сохранения на яндекс диске

# lst = [sorted({dict_foto['height'] * dict_foto['width']:dict_foto}.items()) for dict_foto in dicts_foto]

# pprint (sorted(lst))

dct = {v['height'] * v['width']:v for v in dicts_foto}
sort_dct = dict(sorted(dct.items(), reverse=True)[0:4])

pprint (sort_dct)

# lst = []
# for dict_foto in dicts_foto:
#     size_foto = dict_foto['height'] * dict_foto['width']
#     size_dict = {size_foto:list(dict_foto.items())} # Делаем новый словарь с ключом - размер фото 
#     lst.append(list(size_dict.items())) # Делаем из нового словаря список и ...
#     sorted_size_list = sorted(lst, reverse=True) # ... сортируем этот список по размеру фото и по убывагнию
# pprint(sorted_size_list[0:4]) #Выбираем с последние четыре фото для сохранения на яндекс диске



# # Получаем ссылку на фото профиля
# pprint(vk_foto_1.profile_fotos()[0]['sizes'][0]['url'])
# # Получаем размер фото
# height = vk_foto_1.profile_fotos()[0]['sizes'][0]['height']
# width = vk_foto_1.profile_fotos()[0]['sizes'][0]['width']
# pprint(f'{height}x{width} px')

# # Получаем дату добавления фото в профиль
# pprint(vk_foto_1.profile_fotos()[0]['date'])
# # Получаем количество лайкосов фотки профиля
# pprint(vk_foto_1.profile_fotos()[0]['likes']['count'])
