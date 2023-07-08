from seventv import seventv
import asyncio

async def get():
    em=seventv()
    resp = await em.emote_search("")
    print(resp)
    em.close()

asyncio.run(get())