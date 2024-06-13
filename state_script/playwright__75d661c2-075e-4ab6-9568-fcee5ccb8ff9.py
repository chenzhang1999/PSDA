
from playwright.async_api import async_playwright
import asyncio

async def combined_operations():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        

        await page.goto("http://localhost:8080/cadenza/login")
        await page.close()
        await browser.close()



asyncio.run(combined_operations())
