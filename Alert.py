from selenium import webdriver

# Path
driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver")

validateText = "option3"
# open URL
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# find element by CSS selector and send details in that field
driver.find_element_by_css_selector("#name").send_keys(validateText)
# find element by ID and click on it
driver.find_element_by_id("alertbtn").click()

# switch to alert from the browser
alert = driver.switch_to.alert

# store alert text in the alerttext variable
alerttext = alert.text

# varify that validateText and alerttext is matching
assert validateText in alerttext

alert.accept()                      # This will click on Ok button in alert
# alert.dismiss()                     # This will click on the cancel button

