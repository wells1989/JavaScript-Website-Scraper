from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:

    chrome = webdriver.Chrome() # launches chrome and you can interact with it via chrome
    chrome.get("https://quotes.toscrape.com/search.aspx") # loads webpage

    page = QuotesPage(chrome) # as now chrome is running the page

    author = input("Enter author you want quotes from: ")
    page.select_author(author)
    tags = page.get_available_tags()

    print(("select one of these tags [{}]".format(" | ".join(tags)))) 
    selected_tag = input("Enter your tag: ")

    print(page.search_for_quotes(author, selected_tag))


    input("Press Enter to close the browser window")
    chrome.quit() # this block is needed to keep the browser window open (when script terminates it closes)

except InvalidTagForAuthorError as e:
    print(f'Error: {e}')

except Exception as e:
    print(f'Unknown error occurred: {e}')


