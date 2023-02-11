from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY
import time
from selenium.webdriver.common import alert

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://the-internet.herokuapp.com/javascript_alerts')

#opens window
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
time.sleep(5)

#command to switch to alert window
alertWindow = driver.switch_to.alert

print(alertWindow.text)
alertWindow.send_keys('Welcome')

#alertWindow.accept()        #Close alert window by using OK button
alertWindow.dismiss()           #Close alert window using CANCEL button..will show "null" meaning window closed