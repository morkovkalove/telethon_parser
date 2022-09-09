from telethon.sync import TelegramClient 
from telethon.tl.functions.messages import GetHistoryRequest 

api_id = 12345  #your api id
api_hash = 'asdfghjkl123' #your api hash 
name = 'parsing_session' #any name
chat = 'https://t.me/...'  # Канал откуда парсить


with TelegramClient(name, api_id, api_hash) as client: 

    for message in client.iter_messages(chat): 
        user = client.get_entity(message.sender_id) 
        
        print(f'Имя отправителя : {user.username}, Id отправителя {message.sender_id}, Сообщение : {message.text}')
