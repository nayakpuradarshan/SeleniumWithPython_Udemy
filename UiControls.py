from selenium import webdriver

# Path
driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver")

# open URL
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# find all checkboxs
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

# iterate over the checkboxes
for checkbox in checkboxes:
    # Click on the all the checkboxes
    checkbox.click()

# select all rediio buttons
radiobuttons = driver.find_elements_by_xpath("//input[@class='radioButton']")
print(len(radiobuttons))

radiobuttons[1].click()
assert radiobuttons[1].is_selected()





