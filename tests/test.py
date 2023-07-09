import seventv
import asyncio

async def get():
    em=seventv.seventv()
    query = "wow huh"
    resp = await em.emote_search(query, limit=1, query="url")
    print(resp[0].name)
    print(f'https:{resp[0].host_url}/2x.webp')
    await em.close()

asyncio.run(get())