#Test Case
#------------------
# 1) Open Web Browser (Chrome)
# 2) Open URL https://www.saucedemo.com/
# 3) Enter username (standard_user)
# 4) Enter password (secret_sauce)
# 5) Click on Login
# 6) Capture title of the home page. (Actual title)
# 7) Verify title of the page: Swag Labs (Expected)
# 8) close browser


from selenium import webdriver
from select import select

#this code on line 4 and 5 (and parameter on line 6) keeps the browser from force closing after completion of automation
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.saucedemo.com/')

#input user name
inputUsername = driver.find_element("id" , "user-name").send_keys('standard_user')
#input password
inputPassword = driver.find_element("id", "password").send_keys('secret_sauce')
#click login
selectLogin = driver.find_element("id", "login-button").click()
#verify title is accurate
actualTitle = driver.title
expectedTitle='Swag Labs'
if actualTitle==expectedTitle:
    print("Login Test Passed")
else:
    print("Login Test Failed")
    

#close browser
driver.close()


