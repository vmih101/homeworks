import requests
 
TOKEN = '6061331387:AAESIULRh-Xvzt7Lq4ybo33lFumpSK2bvW8'
 
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'
 
# все обновления
def updates():
    current_updates_link = BASE_URL + 'getupdates'
    request = requests.get(current_updates_link)
    return request.json()
 
# из обновлений берем сообщение и айди чата
def message():
    data = updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    last_message = data['result'][-1]['message']['text']
    user_name = data['result'][-1]['message']['from']['username']
    message_list = {'chat_id': chat_id, 'text': last_message, 'user_name': user_name}
    return message_list
 
# отправляем сообщения
def send_message(chat_id, text='...'):
    url =  BASE_URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)
 
# обработка команд
def bot_answer():
    answer = message()
    text = answer['text']
    id = answer['chat_id']
    user_name = answer['user_name']
    
    if text == '/привет':
        send_message(id, f'Привет {user_name}')
 
bot_answer()
    

