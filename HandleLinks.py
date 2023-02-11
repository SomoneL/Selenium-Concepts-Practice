from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://demo.nopcommerce.com/')
#driver.maximize_window()


#Links
#1) internal - link that will open a new webpage inside the site
#2) external - link that will open a new webpage
#3) broken - link that does not lead to anything usually a 404 error page

#Click On Link **Link Text names are case sensitive**
#driver.find_element(By.LINK_TEXT, "Digital downloads").click()

#We don't prefer partial because it may lead to other elements
#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital ").click()

#Find number of links in a page
#links=driver.find_elements(By.LINK_TEXT, 'a')  #prints 0 and idk why
links = driver.find_elements(By.XPATH, '//a') #use a for <a href </a> html tag
print("Total number of links:", len(links))

#Print all the link names
for link in links:
    print(link.text)