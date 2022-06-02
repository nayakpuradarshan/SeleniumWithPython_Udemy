from selenium import webdriver

driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver")
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


