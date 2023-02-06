from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/egoranucin/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org/')

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


# driver.close()
driver.quit()
