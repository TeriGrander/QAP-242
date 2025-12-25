from selenium.webdriver.common.by import By
import time


def test_selenium_example(selenium):
    selenium.get('https://google.com')
    search_input = selenium.find_element(By.ID, "APjFqb")
    search_input.clear()
    search_input.send_keys(u'Теория струн')
    search_button = selenium.find_element(By.NAME, "btnK")
    time.sleep(1)
    search_button.click()
    time.sleep(1)
    selenium.save_screenshot('result.png')
