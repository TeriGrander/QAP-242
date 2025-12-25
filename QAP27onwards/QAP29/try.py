from selenium import webdriver  # подключение библиотеки
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://google.com')
search_input = driver.find_element(By.ID, "APjFqb")
search_input.send_keys(u'Теория струн')
search_input.submit()
driver.save_screenshot('result.png')
driver.quit()
