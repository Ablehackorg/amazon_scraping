from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd

url = 'https://www.amazon.com/s?k=books&i=stripbooks-intl-ship&ref=nb_sb_noss'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

titles = []
authors = []
prices = []
ratings = []
descriptions = []
read_ages = []
pub_dates = []
publishers = []
languages = []
reviews = []
pages = []


for i in range(3):
    driver.get(url)

# while True:
for i in range(1):
    driver.get(url)
    book_links = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
    book_urls = []
    for link in book_links:
        book_urls.append(link.get_attribute('href'))
    print(len(book_urls))
    print(book_urls)
    count = 1
    for burl in book_urls:
        driver.get(burl)

        title = driver.find_element(By.XPATH, "//span[@id='productTitle']").text
        titles.append(title)
        print(f"{count} - {title}")

        author = driver.find_element(By.XPATH, "//span[@class='author notFaded']"
                                              "//a").text
        authors.append(author)
        print(f"{author}")

        try:
            price = driver.find_element(By.XPATH, "//span[@class='a-size-base a-color-price a-color-price']").text
            prices.append(price)
            print(f"{price}")
        except:
            price = driver.find_element(By.XPATH, "//a[@class='a-link-normal mm-grid-aod-popover-format-entry']")
            price = price.get_attribute('aria-label')
            prices.append(price)
            print(f"{price}")

        try:
            rating = driver.find_element(By.XPATH, "//span[@id='acrPopover']")
            rating = rating.get_attribute('title')

        except:
            rating = 'No rating'
        ratings.append(rating)
        print(f"{rating}")

        try:
            read_age = driver.find_element(By.XPATH, "//ul[@class='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                                     "//span[contains(text(), 'Reading age')]"
                                                     "/following-sibling::span").text

        except:
            read_age = 'No read_age'
        read_ages.append(read_age)
        print(f"{read_age}")

        try:
            pub_date = driver.find_element(By.XPATH, "//ul[@class='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                                     "//span[contains(text(), 'Publisher')]"
                                                     "/following-sibling::span").text
            pub_dates.append(pub_date)
            publishers.append(pub_date)
            print(f"Publisher: {pub_date}")
            print(f"Date: {pub_date}")

        except:
            pub_date = driver.find_element(By.XPATH,
                                           "//tr[@id='detailsReleaseDate']"
                                           "//td//span").text
            pub_dates.append(pub_date)
            publisher = driver.find_element(By.XPATH,
                                           "//tr[@id='detailspublisher']"
                                           "//td//a").text
            publishers.append(publisher)
            print(f"(Audio)Publisher: {publisher}")
            print(f"Date: {pub_date}")

        try:
            language = driver.find_element(By.XPATH,
                                           "//ul[@class='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                           "//span[contains(text(), 'Language')]"
                                           "/following-sibling::span").text
            languages.append(language)
            print(f"Language: {language}")
        except:
            language = driver.find_element(By.XPATH,
                                           "//tr[@id='detailsLanguage']"
                                           "//td//span").text
            languages.append(language)
            print(f"Language: {language}")


        try:
            review = driver.find_element(By.XPATH, "//div[@id='product-summary']"
                                                     "//span").text
        except:
            review = 'No review'
        reviews.append(review)
        print(f"Review: {review}")

        try:
            # page = driver.find_element(By.XPATH, "//ul[@class='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
            #                                          "//span[contains(text(), 'Hardcover')]"
            #                                          "/following-sibling::span").text
            # page = driver.find_element(By.XPATH, "//div[@id='rpi-attribute-book_details-fiona_pages']"
            #                                           "//div[@class='a-section a-spacing-none a-text-center rpi-attribute-value']"
            #                                           "//span").text
            page = driver.find_element(By.XPATH, "//div[@class='a-carousel-row-inner']"
                                                 "//span[contains(text(), 'pages')]").text
            pages.append(page)
            print(f"Page: {page}")

        except:
            duration = driver.find_element(By.XPATH,
                                           "//tr[@id='detailsListeningLength']"
                                           "//td//span").text
            pages.append(duration)

            print(f"Duration: {duration}")
        count += 1
        print('/' * 30)
    try:
        driver.get(url)
        next_page = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,
                            "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")))
        next_link = next_page.get_attribute('href')
        url = next_link
    except Exception as ex:
        print('No next page', ex)
        break

df = pd.DataFrame(
    {
        'title': titles,
        'author': authors,
        'price': prices,
        'rating': ratings,
        'read_age': read_ages,
        'pub_date': pub_dates,
        'publisher': publishers,
        'language': languages,
        'review': reviews,
        'page': pages
    }
)
df.to_csv('amazon_booksfin.csv')