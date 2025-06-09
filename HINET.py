import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv

load_dotenv()

class HINETLogin:
    def __init__(self, mac_address: str) -> None:
        self.driver = None
        self.headless = False
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.hinet_url = os.getenv("HINET_URL")
        self.mac_address = mac_address
    async def start_driver(self) -> None:
        self.chrome_options = Options()
        if self.headless:
            self.chrome_options.add_argument("--headless=new")  
        self.driver = webdriver.Chrome(options=self.chrome_options)

    async def login_and_register_mac(self) -> None:
        await self.start_driver()
        print("Driver started")
        self.driver.get(self.hinet_url)

        await asyncio.sleep(5)
        account_input = self.driver.find_element(By.ID, "i0116")
        account_input.send_keys(self.email)
        print("Email entered")
        next_button = self.driver.find_element(By.ID, "idSIButton9")
        next_button.click()
        print("Next button clicked")
        await asyncio.sleep(2)

        password_input = self.driver.find_element(By.ID, "i0118")
        password_input.send_keys(self.password)
        print("Password entered")
        signin_button = self.driver.find_element(By.ID, "idSIButton9")
        signin_button.click()
        print("Signin button clicked")
        await asyncio.sleep(2)

        stay_signed_in_button = self.driver.find_element(By.ID, "idSIButton9")
        stay_signed_in_button.click()
        print("Stay signed in button clicked")
        await asyncio.sleep(5)

        # MACアドレスの登録処理
        mac_addr_input = self.driver.find_element(By.ID, "mac_addr")
        mac_addr_input.clear()
        mac_addr_input.send_keys(self.mac_address)
        print(f"MAC address {self.mac_address} entered")

        register_button = self.driver.find_element(
            By.XPATH, '//button[text()="登録 (Registration)"]'
        )
        register_button.click()
        print("Registration button clicked")

        await asyncio.sleep(5)

    async def close_driver(self) -> None:
        if self.driver:
            self.driver.quit()

    async def main(self) -> None:
        await self.login_and_register_mac()
        await self.close_driver()


if __name__ == "__main__":
    mac_address = ["00:11:22:33:44:55"] 
    hinet = HINETLogin(mac_address)
    asyncio.run(hinet.main())