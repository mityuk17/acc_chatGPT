import asyncio

import telethon
import chat_GPT
import logging
logging.basicConfig(level=logging.INFO)


api_id = 0
api_hash = ''
client = telethon.TelegramClient('main_acc', api_id=api_id, api_hash=api_hash)
client.start()
