from HINET import HINETLogin
from dotenv import load_dotenv
import asyncio
import aiohttp


load_dotenv()

async def check_internet_connection() -> bool | aiohttp.ClientResponse:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://www.msftconnecttest.com/connecttest.txt", timeout=5) as response:
                return response.status == 200
    except:
        return False
    
async def hinet():
    mac_addresses = ["a"]
    for mac_address in mac_addresses:
        try:
            await HINETLogin(mac_address=mac_address).main()
        except Exception as e:
            pass

async def main():
    while True:
        if await check_internet_connection():
            print("Internet connection is available.")
        else:
            print("No internet connection. Retrying in 10 seconds...")
            await hinet()
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
   