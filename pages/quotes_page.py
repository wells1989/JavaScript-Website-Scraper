from selenium.webdriver.common.by import By
from typing import List
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.quotes_page_locators import QuotesPageLocators 
from parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    # quotes from all the page
    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e)
            for e in self.browser.find_elements(
                By.CSS_SELECTOR, QuotesPageLocators.QUOTE
            )
            ]


    # selecting author_dropdown and the author inside of it
    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(
                By.CSS_SELECTOR, QuotesPageLocators.AUTHOR_DROPDOWN
            )
        return Select(element) # takes the element and wraps it in a Select wrapper (element needs to be a dropdown)


    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name) # opens the dropdown, sees what's there and selects the one that matches
    

    # selecting tags_dropdown and the selected tag
    @property
    def tags_dropdown(self) -> Select:
        element = self.browser.find_element(
                By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN
            )
        return Select(element)

    def get_available_tags(self):
        return [option.text.strip() for option in self.tags_dropdown.options] # returns the text for all of the options from the tag_dropdown (the select object has the options.text properties)

    def select_tag(self, tag_name: str):
        available_tags = self.get_available_tags()

        if tag_name not in available_tags:
            raise InvalidTagForAuthorError(f'Tag "{tag_name}" not found.')

        self.tags_dropdown.select_by_visible_text(tag_name)


    # defining the search_button and searhc_for_quotes functionality
    @property
    def search_button(self):
        return self.browser.find_element(
                By.CSS_SELECTOR, QuotesPageLocators.SEARCH_BUTTON
            )
    

    def search_for_quotes(self, author, tag) -> List[QuoteParser]:
        self.select_author(author)
        
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, QuotesPageLocators.VALUE_OPTION)
            )
        )

        self.select_tag(tag)
        
        self.search_button.click()

        return self.quotes

class InvalidTagForAuthorError(ValueError):
    pass