import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(storage_state="context\\context__2bdcc2ba-7c08-4c05-8e67-f98cf7340176.json")
    page = await context.new_page()
    await page.goto("http://localhost:8080/cadenza/login")
    await page.get_by_label("Benutzername *").click()
    await page.get_by_label("Benutzername *").fill("Admin")
    await page.get_by_placeholder(" ").click()
    await page.get_by_placeholder(" ").fill("Admin")
    await page.get_by_role("button", name="Anmelden").click()
    await page.get_by_role("link", name="Management Center").click()
    await page.get_by_role("link", name="Repositorys").click()
    await page.close()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
