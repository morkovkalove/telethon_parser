from telethon.sync import TelegramClient 
from telethon.tl.functions.messages import GetHistoryRequest 

api_id = 12345  #your api id
api_hash = 'asdfghjkl123' #your api hash 
name = 'parsing_session' #any name
chat = 'chanell_name'  # Канал откуда парсить



client = TelegramClient(name, api_id, api_hash)
# updates = client(ImportChatInviteRequest('https://t.me/+OflQ5VeKI_ljNzNi'))
# chat = client.get_entity('1667947415')


@client.on(events.NewMessage(chats=chat))
async def startingMessages(event):
    #Выводим по 1 сообщению в консоль в режиме реального времени
    async for event.message in client.iter_messages(chat, limit=1):
        user = await client.get_entity(event.message.sender_id)
        message_dt = datetime.datetime.now()
        print(f'Когда: {message_dt:%d.%m.%Y %H:%M}  Имя отправителя : {user.username}, Id отправителя {event.message.sender_id}, Сообщение : {event.message.text}')
      

client.start()
client.run_until_disconnected()
