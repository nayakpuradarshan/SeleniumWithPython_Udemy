from selenium import webdriver

# Path
driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver")

validateText = "option3"
# open URL
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()

alert = driver.switch_to.alert

alerttext = alert.text
assert validateText in alerttext
alert.accept()                      # This will click on Ok button in alert
# alert.dismiss()                     # This will click on the cancel button

