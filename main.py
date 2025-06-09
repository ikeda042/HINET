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
    
async def hinet():
    mac_addresses = []
    for mac_address in mac_addresses:
        try:
            await HINETLogin(mac_address=mac_address).main()
        except Exception as e:
            print(e)
            pass

async def main():
    while True:
        is_connected = await check_internet_connection()
        if is_connected:
            print("Internet connection is available.")
            await hinet()
        else:
            print("No internet connection. Retrying in 10 seconds...")
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())