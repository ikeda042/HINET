from HINET import HINETLogin
from dotenv import load_dotenv
import asyncio
import os
from slack import send_slack, SlackMessage

load_dotenv()
MAC_ADDRESSES = os.getenv("MAC_ADDRESSES", "").split(",")
MY_MAC_ADDRESS = os.getenv("MY_MAC_ADDRESS", "")

    
async def hinet():
    mac_addresses = MAC_ADDRESSES + [MY_MAC_ADDRESS]
    for mac_address in mac_addresses:
        try:
            await HINETLogin(mac_address=mac_address).main()
        except Exception as e:
            pass

async def main():
    while True:
        await hinet()
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
   