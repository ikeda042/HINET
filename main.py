from HINET import HINETLogin
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    mac_addresses = []
    for mac_address in mac_addresses:
        try:
            await HINETLogin(mac_address=mac_address).main()
        except Exception as e:
            print(e)
            pass