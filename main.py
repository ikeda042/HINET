from HINET import HINETLogin
from dotenv import load_dotenv
import asyncio
import aiohttp


load_dotenv()

async def check_internet_connection() -> bool | aiohttp.ClientResponse:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://www.msftconnecttest.com/connecttest.txt", timeout=5) as response:
                print(f"Response status: {response.status}")
                return response.status == 200
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
        print("Checking internet connection...")
        if await check_internet_connection():
            print("Internet connection is available.")
        else:
            print("No internet connection. Retrying in 10 seconds...")
            await hinet()
        await asyncio.sleep(10)

if __name__ == "__main__":
    # asyncio.run(main())
    internet_connection = asyncio.run(check_internet_connection())
    if internet_connection:
        print("Internet connection is available.")
    else:
        print("No internet connection. Please check your connection.")