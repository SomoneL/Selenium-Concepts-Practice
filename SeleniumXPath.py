
#XPath is defined as XML Path.
#It is a syntax or language for finding any element on the web page using XML path expression
#XPath is used to find the location of any element on a webpage using HTML DOM structure
#XPath can be used to navigate through elements and attributes in DOM
#XPath is an address of the element

#Types of xpath
#1. Absolute/Full
#Ex./html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[1]/ytd-topbar-logo-renderer/a/div/ytd-logo/yt-icon
#2. Relative/Partial xpath
#Ex. //*[@id="logo-icon"]

#Diff between Absolute & Relative XPaths
#-----------------------------------------------------#
#1. Absolute xpath starts from root html node
# Relative xpath directly jump to element on DOM

#2. Absolute xpath start with /
# Relative xpath starts with //

#3.In Absolute xpath we use only tags/nodes
# In Relative xpath we use attributes


#How to write xpaths manually ****GOOD IN INTERVIEWS****
#Write tags using Bottom to top analysis, starting from inner most tag
#Ex. html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a

#Syntax of writing relative xpath
#tagname[@attribute='value']
#Ex. input[@id='small-searchterms']
#if you do not know tag name, you can just use a '*'... Ex. *[@id='small-searchterms']

#How to capture xpath automatically
#1. Firebug, firepath -> Firefox   BUT ->deprecated/ not available anymore
#2. Right click on element -> Inspect -> Highlight html code ->Right click -> Copy Xpath... STILL WORKS
#3. SelectorsHub.com

# 2 reasons to prefer relative xpath
#1. if developer introduced new element then absolute xpath will be broken
#2. if developer changed the location then absolute xpath will be broken 

#absoluate xpath is unstable..

#Which Xpath is prefered? Why?
#Ans: Relative

#xpath method options
#and
#or
#contains()
#starts-with()
#text()

from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://www.automationexercise.com/products')
#driver.maximize_window()

#Absolute xpath
#driver.find_element(By.XPATH, "/html/body/section[1]/div/input").send_keys("jeans")
#driver.find_element(By.XPATH, "/html/body/section[1]/div/button").click()

#Relative xpath
#driver.find_element(By.XPATH, "//*[@id='search_product']").send_keys("jeans")
#driver.find_element(By.XPATH, "//*[@id='submit_search']").click()

#Xpath with and
#driver.find_element(By.XPATH, "//*[@id='search_product'   and  @name='search' ]").send_keys("jeans")

#Xpath with or
#driver.find_element(By.XPATH, "//*[@id='search_product'   or  @name='search' ]").send_keys("jeans")

#Xpath  with contains(), starts-with()   .....Scenario is a button when first selected has an id='start' and then after selction
#the id='stop' you can use the following Xpaths to make sure both ids are included..st to include both STart and STop
#driver.find_element(By.XPATH, "//*[contains(@id,st')]")
#driver.find_element(By.XPATH, "//*[starts-with(@id,st')]")

#Xpath with text()
#driver.find_element(By.XPATH, "//a[text()='Women']" ).click()
