import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(storage_state="context\\context__198db716-fc79-470a-818e-776d0e24c94f.json")
    page = await context.new_page()
    await page.goto("http://localhost:8080/cadenza/login")
    await page.get_by_label("Username *").click()
    await page.get_by_label("Username *").fill("Admin")
    await page.get_by_label("Username *").press("Tab")
    await page.get_by_placeholder(" ").fill("Admin")
    await page.get_by_placeholder(" ").press("Enter")
    await page.get_by_text("Directory Gewässergüte").click()
    await page.get_by_role("link", name="Übersicht Messstellen").click()
    async with page.expect_popup() as page1_info:
        await page.get_by_role("link", name="Messstellenliste").click()
    page1 = await page1_info.value
    await page1.get_by_test_id("worksheet-view-of-type-table").get_by_label("More …").click()
    await page1.get_by_role("menuitem", name="Duplicate", exact=True).click()
    
    

    return page1, context, browser


    # ---------------------
    
    


async def modified_main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)