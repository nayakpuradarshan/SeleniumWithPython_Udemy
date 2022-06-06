from selenium import webdriver

# Path
driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver")

# open URL
driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element_by_link_text("Click Here").click()

# switch to child (New) window
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
# print text of the h3 tag 
print(driver.find_element_by_tag_name("h3").text)

# switch to again parent window
driver.switch_to.window(driver.window_handles[0])
# print text which is stored in h3 tag
print(driver.find_element_by_tag_name("h3").text)
