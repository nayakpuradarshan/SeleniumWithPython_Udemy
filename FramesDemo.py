from selenium import webdriver

# Path
driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver")

# open URL
driver.get('https://the-internet.herokuapp.com/iframe')

# Frame id or frame name or frame value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)


