import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL: str = 'https://random.dog/woof.json'
API_FOXS_URL: str = 'https://randomfox.ca/floof/'
BOT_TOKEN: str = '6781906191:AAGLzRxio2Pqqp_7ieWDulEySrn5JiyHo00'
ERROR_TEXT: str = 'Здесь должна была быть картинка с грязным бесчувственным животным :('

offset: int = -2
counter: int = 0
response: requests.Response
link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            if counter%3==0:
                response = requests.get(API_DOGS_URL)
                link = response.json()['url']
            elif counter%2==0:
                response = requests.get(API_FOXS_URL)
                link = response.json()['image']
            else:
                response = requests.get(API_CATS_URL)
                link = response.json()[0]['url']
            if response.status_code == 200:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1


