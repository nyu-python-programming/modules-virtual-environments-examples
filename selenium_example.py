# This example requires that you have also installed the Selenium Chrome WebDriver
# from https://sites.google.com/a/chromium.org/chromedriver/downloads
#
# Download the appropriate version for your version of Chrome and your operating system.
#
# Install by placing the chromedriver file into the following directory:
# - On Mac, place it into /usr/lib/bin
# - On Windows, place it into the same directory where chrome.exe is, typically C:\Program Files (x86)\Google\Chrome\Application

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://knowledge.kitchen/Modules_in_Python')

# print title of page
print(driver.title)

# infinite loop
while True:
  # move the cursor to a particular link on the page
  elem = driver.find_element_by_css_selector(".toclevel-2.tocsection-6 a") # find the element by its CSS-style selector
  ActionChains(driver).move_to_element(elem).perform() # move mouse to the element
  elem.click() # click the element!

  # move the cursor to a particular link on the page
  elem = driver.find_element_by_css_selector(".toclevel-1.tocsection-14 a") # find the element by its CSS-style selector
  ActionChains(driver).move_to_element(elem).perform() # move mouse to the element
  elem.click() # click the element!

driver.close()
