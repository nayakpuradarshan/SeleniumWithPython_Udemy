from selenium import webdriver
from selenium.webdriver.support.select import Select

# Using chromeoptions method we can give orders to chrome browser
chrome_option = webdriver.ChromeOptions()
# Given argument as work as headless browser
chrome_option.add_argument("headless")

driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver", options=chrome_option)
# Go to this URL
driver.get('http://rahulshettyacademy.com/angularpractice/')

# find element by name
# driver.find_element_by_name('name').send_keys('Rahul')

# find element by CSS Selector
driver.find_element_by_css_selector("input[name='name']").send_keys("Darshan")

# find element by name
driver.find_element_by_name("email").send_keys('darshan@gmail.com')

# find element by ID
driver.find_element_by_id('exampleCheck1').click()

# Selecting value from dropdown using the Select
dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')

# find element by xpath
driver.find_element_by_xpath("//input[@type='submit']").click()

# find element by name Selector
# success = driver.find_element_by_class_name("alert-success").text
# print(success)

# find element by CSS Selector
# print(driver.find_element_by_css_selector("[class='alert alert-success alert-dismissible']").text)

# other way of using CSS Selector ( Regular Expression in CSS )
# print(driver.find_element_by_css_selector("[class='alert alert-success alert-dismissible']").text)

# find element by Xpath   ( Regular Expression in Xpath )
# print(driver.find_element_by_xpath("//*[contains(@class, 'alert-success')]").text)

message = driver.find_element_by_class_name('alert-success').text

assert "Success" in message;

print(">>> Code Completed Successfully !")

driver.close()
