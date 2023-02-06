from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/egoranucin/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org/')

dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

list_of_dates = []
list_of_names = []
events = {}

for date in dates:
    list_of_dates.append(date.text)

for name in names:
    list_of_names.append(name.text)

for n in range(len(list_of_names)):
    events[n] = {
        "time": list_of_dates[n],
        "name": list_of_names[n],
    }

print(list_of_dates)
print(list_of_names)
print(events)