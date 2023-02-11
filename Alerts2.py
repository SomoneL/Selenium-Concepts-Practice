from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY
import time
from selenium.webdriver.common import alert

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#opens window
driver.get('https://mypage.rediff.com/login//dologin')

#Trigger alert 
driver.find_element(By.XPATH, "//*[@id='pass_div']/input[3]").click()   #Login Button
time.sleep(5)

#Select okay on alert
driver.switch_to.alert.accept()

#close browser
driver.close()