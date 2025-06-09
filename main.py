from HINET import HINETLogin
from dotenv import load_dotenv
import asyncio
import aiohttp
import os
from slack import send_slack, SlackMessage


load_dotenv()
MAC_ADDRESSES = os.getenv("MAC_ADDRESSES", "").split(",")
MY_MAC_ADDRESS = os.getenv("MY_MAC_ADDRESS", "")
async def check_internet_connection() -> bool | aiohttp.ClientResponse:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.msftconnecttest.com/connecttest.txt", timeout=5) as response:
                return response.status == 200
    except:
        return False
    
async def hinet():
    mac_addresses = MAC_ADDRESSES + [MY_MAC_ADDRESS]
    for mac_address in mac_addresses:
        try:
            await HINETLogin(mac_address=mac_address).main()
        except Exception as e:
            pass

async def main():
    while True:
        if await check_internet_connection():
            print("Internet connection is available.")
            await send_slack(
                webhook_url=os.getenv("WEBHOOK_URL"),
                payload=SlackMessage(text="Internet connection is available. Starting HINET login process.")),
        
        else:
            print("No internet connection. Retrying in 10 seconds...")
            await hinet()
        await asyncio.sleep(120)

if __name__ == "__main__":
    asyncio.run(main())
   