# Created By CallsMusic

import asyncio
import time
import tgcrypto

from pyrogram import Client

print("""

hey welcome to xmarty Session


Github: https://github.com/Itz-fork/Callsmusic-Plus
Docs: https://itz-fork.gitbook.io/callsmusic-plus
Website: https://musicsnexabot.netlify.app
""")
time.sleep(5) # Just for show off
print("Enter Your APP ID and API HASH To Generate Pyrogram String Session.")


async def main():
    async with Client(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        PYRO_SESSION = await app.export_session_string()
        await app.send_message("me", f"**Pyrogram String Session:** \n`{PYRO_SESSION}` \n\n**Powered by @NexaBotsUpdates 😇**")
        print(f"Here is your Pyrogram String Session: \n {PYRO_SESSION} \n\nPro tip: Check your saved message also, Backup of this session is also saved in there :)")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
