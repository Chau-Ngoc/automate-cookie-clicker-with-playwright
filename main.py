import time

from playwright.sync_api import sync_playwright

from player import Player

GAMEPLAY_SESSION_MINUTES = 5


def on_action(action, selector):
    def wrapper_func():
        return action(selector)

    return wrapper_func


playwright = sync_playwright().start()
chromium = playwright.chromium
browser = chromium.launch(
    channel="msedge", headless=False, chromium_sandbox=True
)
page = browser.new_page()
page.goto("https://orteil.dashnet.org/cookieclicker/")
page.locator("text=Got it!").click()
page.locator("#langSelect-EN").click()
page.locator("div.framed.close.sidenote").click()

player = Player(page)

click_cookie = on_action(player.click_on_selector, "#bigCookie")
buy_cursor = on_action(player.click_on_selector, "#product0")
buy_grandma = on_action(player.click_on_selector, "#product1")
buy_farm = on_action(player.click_on_selector, "#product2")
buy_mine = on_action(player.click_on_selector, "#product3")
buy_factory = on_action(player.click_on_selector, "#product4")
buy_bank = on_action(player.click_on_selector, "#product5")
buy_temple = on_action(player.click_on_selector, "#product6")
buy_wizard_tower = on_action(player.click_on_selector, "#product7")

game_over = time.time() + 60 * GAMEPLAY_SESSION_MINUTES

while True:
    click_cookie()

    if page.locator("div.framed.close.sidenote").is_visible():
        page.locator("div.framed.close.sidenote").click()

    if time.time() > game_over:
        break

browser.close()
playwright.stop()
