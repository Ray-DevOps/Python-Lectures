
# Selenium WebDriver is a collection of open-source APIs which are used to automate the testing of a web application.
# Selenium WebDriver tool is used to automate web application testing to verify that it works as expected. It automates browsers
# It supports many browsers such as Firefox, Chrome, IE, and Safari.
# Everything that a human can do on a website such as type, click, scroll, etc. can be done using Selenium.
# You can use Selenium to automate things like form-filling, data-entry (transferring information from an Excel spreadsheet to an online google form, 
# or anything that is repetitive and tedious.

# Unlike BeautifulSoup, Selenium allows us to find elements by so many attributes such as by name, by link, by class, by ID, by partial link, by CSS selector, etc.
 

#
#                                                ILLUSTRATION
#                                     -----------------------------------


from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()                                                             # We create a Chrome options object and add an experimental option
chrome_options.add_experimental_option("detach", True)                                                 # to true, so as to keep our chrome browser open after program finishes

driver = webdriver.Chrome(options=chrome_options)                                                      # We create an object from the webdriver class and instantiate a chrome browser
driver.get("https://www.amazon.ca/Instant-Electric-Sterilizer-One-Touch-Stainless/dp/B01NBKTPTS/ref=sr_1_1?")

price_dollar= driver.find_element(By.CLASS_NAME, value="a-price-whole")                                # The By.CLASS_NAME method allows us to find an element in the HTML code by class
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")                             # Here the price in the HTML code is made of 2 components. The dollar portion and the cents portion

print(f"The full price is {price_dollar.text}.{price_cents.text}")                                     # We add .text so as to get just the text component of the results and not the HTML tags

driver.quit()                                                                                          # This allows us to quit the program after the code runs



# NOTE: With Selenium, the find_element() method only returns the first element that matches the criteria. To get all the elements that 
# match that criteria, you'd need to use the find_elements() method.
