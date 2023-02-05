from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# id and name locator
#searchStore = driver.find_element("id","small-searchterms").send_keys("iphone 14")
#searchStore = driver.find_element("name","q").send_keys("iphone 14")

#linktext & partial linktext
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()




