from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://demo.prestashop.com/')
driver.maximize_window()


#class name
slider=driver.find_element(By.CLASS_NAME, "container")
print(len(slider))