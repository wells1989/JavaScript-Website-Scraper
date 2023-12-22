# JavaScript Website Scraper: 

A site to interact with a dynamic JavaScript website using selenium.webdriver

## Project Requirements

Python 3.11.1

```python
autopep8==2.0.4
bcrypt==4.0.1
beautifulsoup4==4.12.2
black==23.12.0
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
idna==3.6
mypy-extensions==1.0.0
packaging==23.2
pathspec==0.12.1
platformdirs==4.1.0
pycodestyle==2.11.1
requests==2.31.0
soupsieve==2.5
urllib3==2.1.0

```

## Usage

```python
QuotesPage class:

@property
BooksPage.quotes
    # returns a QuoteParser instance for each element found in the browser using CSS_SELECTOR

@property
BooksPage.author_dropdown
    # returns the author element in a Select wrapper

select_author(author_name)
    # selects the author in the dropdown menu

@property
tags_dropdown
    # returns the tag element in a Select wrapper

get_available_tags()
    # returns all tags on the site

select_tag(tag_name)
    # selects the tag in the dropdown menu

@property
search_button
    # selects the searcn button via CSS_SELECTOR

search_for_quote()
    # runs the search function, with an implicit wait imposed by WebDriverWait to check for matching tags
```

```python
QuoteParser class:

@property
content   
    # returns the quote content via find_element()

author    
    # returns the author via find_element()

tags    
    # returns all tags via find_elements()

```


app.py (user UI)
```python

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


```

## Personal notes
- This project aimed to build on the previous scraping project, which focused on more static pages and introduced advanced concepts for interacting with a dynamic site using Python
- Due to the above focus, I did not include a menu component to separate the UI, but if the app grew in size this would be the logical next step
