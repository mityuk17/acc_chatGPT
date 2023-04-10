import asyncio

import telethon
import chat_GPT
import logging
logging.basicConfig(level=logging.INFO)


api_id = 9411854
api_hash = '499c76606cefdeadd4b1ece84a5a9932'
client = telethon.TelegramClient('main_acc', api_id=api_id, api_hash=api_hash)
client.start()