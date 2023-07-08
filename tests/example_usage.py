import asyncio
from sevenTV import sevenTV

async def getemote():
    emoji = sevenTV()
    emotes = await emoji.emote_search("pepe", case_sensitive=True)
    print(emotes[2])
    await emoji.close()

asyncio.run(getemote())