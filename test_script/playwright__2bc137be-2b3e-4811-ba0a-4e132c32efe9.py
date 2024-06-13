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
    await page.get_by_placeholder(" ").press("Enter")
    await page.get_by_text("Verzeichnis Gewässergüte", exact=True).click()
    await page.get_by_text("Verzeichnis Einzelsichten").click()
    await page.goto("http://localhost:8080/cadenza/processingChain?repositoryItemGlobalId=ROOT.Gew%C3%A4sserg%C3%BCte.Einzelsichten.gewaesser%3AMst.Messstelle.sel&conditionValuesSetHash=B68D242&selector=ROOT.Gew%C3%A4sserg%C3%BCte.Einzelsichten.gewaesser%3AMst.Messstelle.sel&sourceOrderAsc=false&offset=0&limit=2147483647")
    await page.close()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
