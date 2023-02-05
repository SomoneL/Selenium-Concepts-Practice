from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://facebook.com/')
#driver.maximize_window()



#CSS Selector tag & id.. "input" is a tag name, "email" is an id name. syntax = tagname#valueofID
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
#OR another option for syntax, tag name is ALWAYS optional. Gives same input
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")


#CSS Selector: tag and class. syntax = tagname.valueofClass input is tag name,inputtext _55r1 _6luy is class name... removed everything after the space in tag name as sometimes depending on how developers make the page, it will not be read by Selenium. but it still works.
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
#OR just use .inputtext, this works as well
#driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")

#GOAL IS TO USE A UNIQUE ATTRIBUTE FOR EACH TIME YOU SELECT SOMETHING. AN ATTRIBUTE NOT SHARED BY MANY ELEMENTS ON THE PAGE SO YOU CAN FIND YOUR SPECIFIC ONE


#CSS Selector: tag attribute.. syntax = tagname[attribute=value]... input[data-testid=royal_email] 
#driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc@gmail.com")
#This works too, removing input tag name, remember tag name is usually optional
#driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc@gmail.com")


#CSS Selector: tag class attribute... syntax = tagname.valueofClass[attribute=value]
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("abc@gmail.com")


