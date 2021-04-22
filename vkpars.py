import requests
import json
from time import sleep



token = ''
version = 5.126
domain = 'rhymes'
offset = 0
all_posts = []
z = []
urlpat = 0
def check_requests(a):
    if a == 5:

        response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                "v": version,
                                'domain': domain,
                                'offset': offset
                            }
                            )

        data = response.json()['response']['items']

        data = data[1]

        img_url = data['attachments'][0]['photo']['sizes'][-1]['url']

        #print(data['text'], img_url)
        with open("data_file.json", "w", encoding='utf-8') as write_file:
            json.dump(data['text'], write_file)
        with open("data_url.json", "w", encoding='utf-8') as file:
            json.dump(data['attachments'][0]['photo']['sizes'][-1]['url'], file)
