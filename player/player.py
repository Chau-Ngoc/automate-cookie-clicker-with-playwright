class Player:
    def __init__(self, page):
        self.page = page

    def click_on_selector(self, selector: str):
        self.page.locator(selector).click()
