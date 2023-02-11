from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://the-internet.herokuapp.com/dropdown')

#Select checks to make sure given tag is a SELECT tag 
dropOption = Select(driver.find_element(By.XPATH,"//select[@id='dropdown']" ))  

#Select option from the dropdown, three different ways select by visible text, by value, by index
#Approach 1
#dropOption.select_by_visible_text("Option 2")
#Approach 2
#dropOption.select_by_value("2")
#Approach 3
#dropOption.select_by_index(2)

allOptions = dropOption.options         #.options returns a list of all options belonging to this select tag
print("Total number of options:",len(allOptions))   #3 because it is counting 'Please select an option"

#for opt in allOptions:
#   print(opt.text) #"Please select an option,Option 1, Option 2"

#Select option from dropdown without using built - in method 
#for opt in allOptions:
#   if opt.text == "Option 2":
#      opt.click()
#      break


