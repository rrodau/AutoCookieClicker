from selenium import webdriver
from selenium.webdriver.common.keys import Keys

mozilla_drive_path = "/home/robert/Development/geckodriver"
driver = webdriver.Firefox(executable_path=mozilla_drive_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")

while True:
    #items = driver.find_elements_by_css_selector(".storeBulk div")
    #money = driver.find_element_by_id(".cookies")
    #money = money.text.split(" ")[0]
    for i in range(50):
        cookie.click()
    for i in range(4, -1, -1):
        money = driver.find_element_by_id("cookies")
        money = money.text.split(" ")[0]
        item = driver.find_element_by_id(f"productPrice{i}")
        #print(f"Money: {money}")
        #print(f"Item Price: {item.text}")
        #print(f"Type Item Price: {type(item.text)}")
        if len(item.text) > 1:
            item = item.text.replace(",","")
            if int(money) > int(item):
                product = driver.find_element_by_id(f"product{i}")
                product.click()