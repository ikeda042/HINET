from HINET import HINETLogin
from dotenv import load_dotenv
import asyncio
import aiohttp


load_dotenv()

async def check_internet_connection() -> bool | aiohttp.ClientResponse:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.google.com", timeout=5) as response:
                return True
    except:
        return False
    
async def main():
    mac_addresses = []
    for mac_address in mac_addresses:
        try:
            await HINETLogin(mac_address=mac_address).main()
        except Exception as e:
            print(e)
            pass

while True:
    if asyncio.run(check_internet_connection()):
        print("Internet connection is available.")
        asyncio.run(main())
    else:
        print("No internet connection. Retrying in 10 seconds...")
    asyncio.sleep(60)  