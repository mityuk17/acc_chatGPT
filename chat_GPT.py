import asyncio

import openai


openai.api_key = "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"


async def text(text):
    prompt = text
    task = 'Я буду присылать тебе посты, а ты поставь себя в роль позитивного и иногда саркастичного маркетолога мужского пола, который читает мой блог и пишет короткие комментарии на мои посты. Выделяй главный JBTD в тексте автора поста, но не пиши про него, а используй при написании своего короткого комментария. Используй разговорный стиль, иногда эмодзи(если потребуется). Используй до 150 символов в ответе, отвечай на русском языке.'
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": task},
            {"role": "user", "content": prompt}
        ]
    )
    '''completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        top_p=0.3,
        frequency_penalty=0,
        presence_penalty=0
    )'''
    return completion.choices[0].message.content


async def create_image(text, size):
    response = openai.Image.create(
        prompt=text,
        n=1,
        size=f"{size}*{size}"
    )
    image_url = response['data'][0]['url']
    return image_url
