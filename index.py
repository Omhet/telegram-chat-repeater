from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
from decouple import config

API_ID = config('API_ID')
API_HASH = config('API_HASH')
SESSION_STRING = config('SESSION_STRING')
CHAT_FROM = int(config('CHAT_FROM'))
CHAT_TO = int(config('CHAT_TO'))

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)
        # print(client.session.save())

# with client:
#     client.loop.run_until_complete(main())

@client.on(events.NewMessage(chats=CHAT_FROM))
async def my_event_handler(event):
    await client.send_message(CHAT_TO, event.raw_text)

client.start()
client.run_until_disconnected()
