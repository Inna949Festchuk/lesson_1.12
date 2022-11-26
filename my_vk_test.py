with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()
    
import time
import requests
from pprint import pprint

# URL = 'https://api.vk.com/method/users.get'
# params = {
#     'user_ids': '1,2',
#     'access_token': token,
#     'v':'5.131',
#     'fields': 'education,sex'
# }
# res = requests.get(URL, params)
# pprint(res.json())

# def search_groups(q, sorting=0):
#     '''
#     Параметры sort
#     0 — сортировать по умолчанию (аналогично результатам поиска в полной версии сайта);
#     6 — сортировать по количеству пользователей.
#     '''
#     params = {
#         'q': q,
#         'access_token': token,
#         'v':'5.131',
#         'sort': sorting,
#         'count': 300
#     }
#     req = requests.get('https://api.vk.com/method/groups.search', params).json()
# #     pprint(req)
#     req = req['response']['items']
#     return req

# target_groups = search_groups('python')

# target_group_ids = ','.join([str(group['id']) for group in target_groups])

# params = {
#     'access_token': token,
#     'v':'5.131',
#     'group_ids': target_group_ids,
#     'fields':  'members_count,activity,description'

# }
# req = requests.get('https://api.vk.com/method/groups.getById', params)

# pprint(req.json()['response'])


class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version    
        }

    def search_groups(self, q, sorting=0):
        '''
        Параметры sort
        0 — сортировать по умолчанию (аналогично результатам поиска в полной версии сайта);
        6 — сортировать по количеству пользователей.
        '''
        group_search_url = self.url + 'groups.search'
        group_search_params = {
            'q': q,
            'sort': sorting,
            'count': 300
        }
        req = requests.get(group_search_url, params={**self.params, **group_search_params}).json()
        # **self.params, **group_search_params - распаковка словарей и объединение их в один (функцияя кваркс)
        return req['response']['items']   
    
    def search_groups_ext(self, q, sorting=0):
        group_search_ext_url = self.url + 'groups.getById'
        target_groups = self.search_groups(q, sorting)
        target_group_ids = ','.join([str(group['id']) for group in target_groups])
        groups_info_params = {
            'group_ids': target_group_ids,
            'fields': 'members_count,activity,description'
        }
        req = requests.get(group_search_ext_url, params={**self.params, **groups_info_params}).json()
        return req['response']

vk_client = VkUser(token, '5.131')
# pprint(vk_client.search_groups('python'))
# pprint(vk_client.search_groups_ext('python'))
import pandas as pd
pd.DataFrame(vk_client.search_groups_ext('python'))