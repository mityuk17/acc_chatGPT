import asyncio

import telethon
import chat_GPT
import logging
logging.basicConfig(level=logging.INFO)

def get_channels():
    with open('channels.txt') as file:
        ids = file.readlines()
    for i in range(len(ids)):
        ids[i] = ids[i].strip()
    return ids


api_id = 0
api_hash = ''
client = telethon.TelegramClient('main_acc', api_id=api_id, api_hash=api_hash)
whitelist = get_channels()


@client.on(telethon.events.NewMessage())
async def comment(event: telethon.events.NewMessage):
    msg = event.message
    print(msg)
    if msg.is_private:
        await msg.reply("")
        return
    elif msg.post:
        prompt = msg.message
        response = (await chat_GPT.text(prompt)).strip('.').strip()
        print(f'Ответ: {response}')
        await client.send_message(entity=msg.peer_id, message=response, comment_to=msg)


client.start()
client.run_until_disconnected()
