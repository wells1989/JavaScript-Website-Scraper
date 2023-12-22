from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:

    chrome = webdriver.Chrome() #
    chrome.get("https://quotes.toscrape.com/search.aspx") 

    page = QuotesPage(chrome)

    author = input("Enter author you want quotes from: ")
    page.select_author(author)
    tags = page.get_available_tags()

    print(("select one of these tags [{}]".format(" | ".join(tags)))) 
    selected_tag = input("Enter your tag: ")

    print(page.search_for_quotes(author, selected_tag))


    input("Press Enter to close the browser window")
    chrome.quit()

except InvalidTagForAuthorError as e:
    print(f'Error: {e}')

except Exception as e:
    print(f'Unknown error occurred: {e}')


