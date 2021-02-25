from telethon import TelegramClient, events, sync
from decouple import config

API_ID = config('API_ID')
API_HASH = config('API_HASH')
SESSION_NAME = config('SESSION_NAME')
CHAT_FROM = config('CHAT_FROM')
CHAT_TO = config('CHAT_TO')

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # await client.send_message(CHAT_TO, 'Hello, from my python code!')


@client.on(events.NewMessage(chats=CHAT_FROM))
async def my_event_handler(event):
    print(event.raw_text)
    await client.send_message(CHAT_TO, event.raw_text)

client.start()
client.run_until_disconnected()

# with client:
#     client.loop.run_until_complete(main())