data = { 
    "main": "https://www.amazon.com/s?k=laptop",
    "laptops": "//div[@data-cy='title-recipe']/a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']",
    "prices": "//div[@class='a-row a-size-base a-color-secondary']/span[@class='a-color-base']",
    "brand": "//tr[@class='a-spacing-small po-brand']/td[@class='a-span9']/span",
    "model": "//tr[@class='a-spacing-small po-model_name']/td[@class='a-span9']/span",
    "screen": "//tr[@class='a-spacing-small po-display.size']/td[@class='a-span9']/span",
    "ram": "//tr[@class='a-spacing-small po-ram_memory.installed_size']/td[@class='a-span9']/span",
    "op": "//table[@id='productDetails_techSpec_section_2']//tr[th[contains(text(), 'Operating System')]]/td",
    "ssd": "//tr[@class='a-spacing-small po-hard_disk.size']/td[@class='a-span9']/span",
    "cpu": "//tr[@class='a-spacing-small po-cpu_model.family']/td[@class='a-span9']/span",
    "card": "//table[@id='productDetails_techSpec_section_1']//tr[th[contains(text(), 'Graphics Coprocessor')]]/td",
    "rating": "//span[@class='a-size-base a-color-base']",
    "review": "//span[@id='acrCustomerReviewText']"
}

brands = []
models = []
screens = []
rams = []
ssds = []
cpus = []
ops = []
pricess = []
ratings = []
reviews = []
cards = []

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = data['main']
for _ in range(3):
    driver.get(base_url)

for page in range(1,10):
    url = f"{base_url}&page={page}&ref=sr_pg{page}"
    driver.get(url)

    laptops = driver.find_elements(By.XPATH, data["laptops"])
    prices = driver.find_elements(By.XPATH, data["prices"])

    urls = []

    for i,b in zip(laptops,prices):
        urls.append(i.get_attribute("href"))
        pricess.append(b.text)
        print(b.text)

    for u in urls:
        driver.get(u)

        try:
            brand = driver.find_element(By.XPATH, data["brand"]).text
        except:
            brand= "No brand"
        brands.append(brand)
        try:
            model = driver.find_element(By.XPATH, data["model"]).text
        except:
            model= "No model"
        models.append(model)
        try:
            screen = driver.find_element(By.XPATH, data["screen"]).text
        except:
            screen= "No screen"
        screens.append(screen)
        try:
            cpu = driver.find_element(By.XPATH, data["cpu"]).text
        except:
            cpu= "No cpu"
        cpus.append(cpu)
        try:
            ram = driver.find_element(By.XPATH, data["ram"]).text
        except:
            ram = "No ram"
        rams.append(ram)
        try:
            ram = driver.find_element(By.XPATH, data["ram"]).text
        except:
            ram= "No ram"
        rams.append(ram)
        try:
            op = driver.find_element(By.XPATH, data["op"]).text
        except:
            op= "No op"
        ops.append(op)
        try:
            ssd = driver.find_element(By.XPATH, data["ssd"]).text
        except:
            ssd= "No ssd"
        ssds.append(ssd)
        try:
            card = driver.find_element(By.XPATH, data["card"]).text
        except:
            card= "No card"
        cards.append(card)
        try:
            rating = driver.find_element(By.XPATH, data["rating"]).text
        except:
            rating = "No rating"
        ratings.append(rating)
        try:
            review = driver.find_element(By.XPATH, data["review"]).text
        except:
            review= "No review"
        reviews.append(review)
        print(brand,'\n',model,'\n',screen,'\n',cpu,'\n',ram,'\n',op,'\n',ssd,'\n',rating,'\n',card,'\n',review)

df = pd.DataFrame({
    'brands':brands,
    'models':models,
    'screens':screens,
    'rams':rams,
    'ssds':ssds,
    'cpus':cpus,
    'ops':ops,
    'pricess':prices,
    'ratings':ratings,
    'reviews':reviews,
    'cards':cards
})

df.to_csv('data.csv', index=False)