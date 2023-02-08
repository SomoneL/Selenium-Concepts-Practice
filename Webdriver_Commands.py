import time
from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC                #Imported for Explicit Wait


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)




#===============================================================================
# 1. Application Commands..get url, html etc of a page
# get() - opening the application URL
# title - to capture the title of the current webpage
# current_url - to capture the curent url of the webpage
# page_source - to capture source code of the webpage
#     
# driver.get('https://www.saucedemo.com/')
# print(driver.title)               #Swag Labs
# print(driver.current_url)   #https://www.saucedemo.com/
# print(driver.page_source)   #prints all page HTML
# 
# driver.quit()
#===============================================================================


#===============================================================================
# 2. Conditional Commands
# is_displayed()- verifies if an element is displayed on the web page and can be executed on all web elements
# is_enabled() - verifies if an element is enabled on the web page and can be executed on all web elements
# 
# driver.get('https://demo.nopcommerce.com/')
# 
# searchbox=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print("Display status:", searchbox.is_displayed())  #True
# print("Enabled status:" , searchbox.is_enabled())   #True
# 
# driver.quit()
# 
# is_selected() = for radio buttons and check boxes
# driver.get('https://demo.nopcommerce.com/register')
# radio_btn_male=driver.find_element(By.XPATH, "//input[@id='gender-male']")
# radio_btn_female=driver.find_element(By.XPATH, "//input[@id='gender-female']")
# 
# print("Default radio buttons status: ")
# print('Female button:',radio_btn_female.is_selected()) #False
# print('Male button:',radio_btn_male.is_selected()) #False
# 
# 
# radio_btn_female.click() #Select female radio button
# 
# 
# print("After selecting female button: ")
# print('Female button:',radio_btn_female.is_selected()) #True
# print('Male button:' ,radio_btn_male.is_selected()) #False
# 
# 
# radio_btn_male.click()
# print("After selecting male button: ")
# print('Female button:' , radio_btn_female.is_selected()) #False
# print('Male button:' , radio_btn_male.is_selected()) #True
# driver.quit()
#===============================================================================


#===============================================================================
# 3. Browser Commands
# close() - closes single browser window (where driver focused)
# quit() - closes multiple browser windows
# 
# 
# 
# 4. Navigational Commands
# 
# back() - press browser back button
# forward() - press browser forward button
# refresh() - refresh current webpage
#===============================================================================



#5. Wait Commands

#1. Implicit wait
#Advantages: 1. Single Statement 2. Performance will not be reduced. (If the element is available within the time, it proceeds to execute further statements
#Disadvantages: If the element is not available within the time mentioned, still there is a chance of getting exception
#driver.implicitly_wait(10) #10 seconds... implicit wait ..usually inserted at beginning of code instead of before automation section
#Why? When writing one statement at beginning, it works for ALL statements. Wherever there is a synchronization problem, it will fix them all
#Must be before the automations not at end, it will only capture what it is before


#time.sleep
 #Advantage: simple to use
 #Disadvantage: 1. performance of the script is very poor 2. If the element is not available within the time mentioned, still there is a change of getting an exception
 #Waits for maximum time
#time.sleep(5)  --- pause for 5 seconds before continuing automation



#2. Explicit wait..must import WebDriverWait
#Explicit wait works based on condition
#Advantages: More effectively works
#Disadvantages:1. Multiple places feel some difficulty

mywait = WebDriverWait(driver,10) #explicit wait declaration.. we want to wait for the driver element

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')

searchbox.send_keys("Selenium")
searchbox.submit()

#mywait = webdriver class object...#until is a condition that should be true..#if the element (By.XPath...) is present...#the statement will return the element 'searchlink'
searchlink = mywait.until(EC.presence_of_all_elements_located((By.XPATH, "//h3[text()='Selenium']")))

searchlink.click()

driver.quit()
