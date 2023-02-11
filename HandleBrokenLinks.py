#we need to install requests package through Eclipse - Preferences - Pydev - Intepreters - PythonInterpreters
import requests as requests
 
from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('http://www.deadlinkcity.com/')
#driver.maximize_window()


#Links
#1) internal - link that will open a new webpage inside the site
#2) external - link that will open a new webpage
#3) broken - link that does not lead to anything usually a 404 error page


#Print number of broken links
allLinks = driver.find_elements(By.TAG_NAME,'a')
count = 0

for link in allLinks:
    url=link.get_attribute('href')  #get all html attributes with 'href'
    res=requests.head(url)  #whatever url you pass, will be sent to server as a request (not clicked on). API request.
    try:
        res=requests.head(url)
    except:
        None
        
    if res.status_code>=400:
        print(url, "    is broken link")
        count+=1
    else:
        print(url, "    is valid link")
print("Total number of broken links: ",count)
