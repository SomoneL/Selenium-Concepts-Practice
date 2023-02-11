from selenium import webdriver
from selenium.webdriver.common.by import By  #MUST USE to use BY


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://itera-qa.azurewebsites.net/home/automation')
driver.maximize_window()

#Select specific checkbox
#driver.find_element(By.XPATH, "//input[@id='monday']").click()

#Select all the checkboxes (Monday - Sunday)
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#print(len(checkboxes))  #7..prints 7 to show it is identifying all 7 of our check boxes

#Approach 1
#for i in range(len(checkboxes)):
    #checkboxes[i].click()
    
#Approach 2  
for checkbox in checkboxes:
    checkbox.click()

#3) - select multiple checkboxes by choice
#for checkbox in checkboxes:
#   weekname = checkbox.get_attribute('id')
#  if weekname == 'monday' or weekname == 'sunday':
#     checkbox.click()
        
#4) - Select last 2 checkboxes
 #range(5,7) --> gives indexes 6,7
 #totalnumberofelements-2 = starting index (5)
#for i  in range(len(checkboxes)-2,len(checkboxes)):
 #   checkboxes[i].click()
    
 #5) - Select first 2 checkboxes   
#for i in range(len(checkboxes)):
 #   if i < 2:       #determines how many check boxes you want to check
  #      checkboxes[i].click()

#6)Uncheck all checked checkboxes -- uncomment Approach 2 as well to test this
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

