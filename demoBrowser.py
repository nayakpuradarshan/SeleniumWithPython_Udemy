from selenium import webdriver

# Browser expose an executable file
# through selenium test we need to invoke the executable file which will then invoke the actual browser
driver = webdriver.Chrome(executable_path="//Users//darshanpatel//PycharmProjects//pytest//PythonSeleniumUdemy"
                                          "//chromedriver")

driver.maximize_window()
driver.get('http://rahulshettyacademy.com')

print("Title is : ", driver.title)
print("Current url is : ", driver.current_url)

driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')

driver.back()
driver.refresh()

driver.close()  # This method will close a single window of browser
driver.quit()  # This method will close all the windows of the browser
