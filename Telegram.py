from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import ChatAdminRequiredError

api_id = '28460720'
api_hash = '3f5ecbcf317b0795ec051498d4281d73'
phone_number = '+14752791529'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    print("Client created!")
    try:
        async for message in client.iter_messages('https://t.me/H1B_H4_Visa_Dropbox_slots'):
            print(message.text)
    except ChatAdminRequiredError as e:
        print(f"Error: {e}")

with client:
    client.loop.run_until_complete(main())

    
