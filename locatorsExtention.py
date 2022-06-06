from selenium import webdriver

driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver")

driver.get("https://login.salesforce.com/?locale=eu")

# CSS using the ID ( EX : ID = username)
# driver.find_element_by_css_selector("input#username").send_keys("")

# CSS using the class name ( EX : class = input r4 wide mb16 mt8 username)
# driver.find_element_by_css_selector("input.username")

driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//div[@id='usernamegroup']/label")

