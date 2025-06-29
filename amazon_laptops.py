from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

laptop_brands = []
laptop_models = []
laptop_screensizes = []
laptop_rams = []
laptop_storages = []
laptop_cpumodels = []
laptop_operating_systems = []
laptop_prices = []
laptop_ratings = []
laptop_review_counts = []
laptop_graphics_cards = []


# url = "https://www.amazon.com/s?k=laptop&ref=sr_pg_1"
base_url = "https://www.amazon.com/s?k=laptop"

for _ in range(3):
    driver.get(base_url)

for page in range(1, 10): 
    url = f"{base_url}&page={page}&ref=sr_pg_{page}"
    driver.get(url)
    
    print(f"\n📄 Страница {page}")

    laptops = driver.find_elements(By.XPATH, "//div[@data-cy='title-recipe']/a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
    laptop_prices_elements = driver.find_elements(By.XPATH, "//div[@class='a-row a-size-base a-color-secondary']/span[@class='a-color-base']")

    laptop_urls = []
    for i, b in zip(laptops, laptop_prices_elements):
        laptop_urls.append(i.get_attribute('href'))
        laptop_prices.append(b.text)
    
    print(len(laptop_prices))
    print(len(laptop_urls))

    for u in laptop_urls:
        driver.get(u)
        # try:
        try:
            laptop_brand = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-brand']/td[@class='a-span9']/span").text
        except:
            laptop_brand = "NO BRAND"
        laptop_brands.append(laptop_brand)
        print('BRAND:', laptop_brand)

        try:
            laptop_model = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-model_name']/td[@class='a-span9']/span").text
        except:
            laptop_model = "NO MODEL"
        laptop_models.append(laptop_model)
        print('MODEL:', laptop_model)

        try:
            laptop_screensize = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-display.size']/td[@class='a-span9']/span").text
        except:
            laptop_screensize = "NO SCREENSIZE"
        laptop_screensizes.append(laptop_screensize)
        print('SIZE:', laptop_screensize)

        try:
            laptop_ram = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-ram_memory.installed_size']/td[@class='a-span9']/span").text
        except:
            laptop_ram = "NO RAM"
        laptop_rams.append(laptop_ram)
        print('RAM:', laptop_ram)

        try:
            laptop_operating_system = driver.find_element(By.XPATH,"//table[@id='productDetails_techSpec_section_2']//tr[th[contains(text(), 'Operating System')]]/td").text.strip()
        except:
            laptop_operating_system = "NO OS"
        laptop_operating_systems.append(laptop_operating_system)
        print('OP:', laptop_operating_system)

        try:
            laptop_storage = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-hard_disk.size']/td[@class='a-span9']/span").text
        except:
            laptop_storage = "NO SSD"
        laptop_storages.append(laptop_storage)
        print('SSD:', laptop_storage)

        try:
            laptop_cpumodel = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-cpu_model.family']/td[@class='a-span9']/span").text
        except:
            laptop_cpumodel = "NO CPU"
        laptop_cpumodels.append(laptop_cpumodel)
        print('CPU:', laptop_cpumodel)

        try:
            laptop_graphics_card = driver.find_element(By.XPATH, "//table[@id='productDetails_techSpec_section_1']//tr[th[contains(text(), 'Graphics Coprocessor')]]/td").text.strip()
        except:
            laptop_graphics_card = "NO GRAPHIC CARD"
        laptop_graphics_cards.append(laptop_graphics_card)
        print('VIDEO CARD:', laptop_graphics_card)
        try:
            laptop_rating = driver.find_element(By.XPATH, "//span[@class='a-size-base a-color-base']").text
        except:
            laptop_rating = "NO RATING"
        laptop_ratings.append(laptop_rating)
        print('RATING:', laptop_rating)
        try:
            laptop_prices_elements = driver.find_elements(By.XPATH, "//div[@class='a-row a-size-base a-color-secondary']/span[@class='a-color-base']")
            for i in laptop_prices_elements:
                laptop_prices.append(i)
        except:
            print('No price')

        try:
            laptop_review_count = driver.find_element(By.XPATH, "//span[@id='acrCustomerReviewText']").text.split()[0]
        except:
            laptop_review_count = "NO REVIEWS"
        laptop_review_counts.append(laptop_review_count)
        print("REVIEWS:", laptop_review_count, '\n\n')


        # except:
        #     pass

print(
    len(laptop_brands),
    len(laptop_models),
    len(laptop_screensizes),
    len(laptop_rams),
    len(laptop_storages),
    len(laptop_cpumodels),
    len(laptop_operating_systems),
    len(laptop_prices),
    len(laptop_ratings),
    len(laptop_review_counts),
    len(laptop_graphics_cards)
)


df = pd.DataFrame({
    'Brand': laptop_brands,
    'Model': laptop_models,
    'Screen Size': laptop_screensizes,
    'RAM': laptop_rams,
    'Storage': laptop_storages,
    'CPU Model': laptop_cpumodels,
    'OS': laptop_operating_systems,
    'Price (INR)': laptop_prices,
    'Rating': laptop_ratings,
    'Review Count': laptop_review_counts,
    'Graphics': laptop_graphics_cards
})

# Export
file_name = "laptop_normativ.csv"
df.to_csv(file_name, index=False)
print(f"✅ Done! Data saved to {file_name}")

