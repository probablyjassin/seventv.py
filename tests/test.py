""" import seventv
import asyncio
import random

async def get():
    em=seventv.seventv()
    resp = await em.emote_search(page=10000, limit=999)
    print(random.choice(resp))
    await em.close()

asyncio.run(get()) """

respo = {'errors': [{'message': '70429 Rate Limit Reached', 'path': ['emotes'], 'extensions': {'code': 70429, 'fields': {}, 'message': 'Rate Limit Reached'}}], 'data': {'emotes': None}}
print(bool(respo.get('errors', {})))
print(respo.get('errors', {})[0].get('message', {}))