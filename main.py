from HINET import HINETLogin
from dotenv import load_dotenv
import asyncio
import aiohttp
import os
from slack import send_slack, SlackMessage
import socket

load_dotenv()
MAC_ADDRESSES = os.getenv("MAC_ADDRESSES", "").split(",")
MY_MAC_ADDRESS = os.getenv("MY_MAC_ADDRESS", "")

def check_internet_connection(timeout: float = 3.0) -> bool:
    try:
        # create_connection は成功するとソケットを返す
        socket.create_connection(("1.1.1.1", 443), timeout=timeout).close()
        return True
    except OSError:
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
        if check_internet_connection():
            print("Internet connection is available.")
            # await send_slack(
            #     webhook_url=os.getenv("WEBHOOK_URL"),
            #     payload=SlackMessage(text="Internet connection is available. Starting HINET login process.")),
        else:
            print("No internet connection. Retrying in 10 seconds...")
            await hinet()
        await asyncio.sleep(120)

if __name__ == "__main__":
    asyncio.run(main())
   