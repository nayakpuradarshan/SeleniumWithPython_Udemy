
# JavaScript Dom can access any element on web page just like selenium provide
# Selenium have method to execute javasript code in it

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver")
# Go to this URL
driver.get('http://rahulshettyacademy.com/angularpractice/')

driver.find_element_by_name("name").send_keys("hello")

# Using get attribute method you'll be able to get the enter values in the browser
print(driver.find_element_by_name("name").get_attribute("value"))

# execute script is the javascript method
driver.execute_script()

