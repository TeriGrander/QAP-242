import time
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password


def test_petfriends(web_browser):

    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(0.1)  # because I don't know yet how to wait for element to appear!

    # click on the new user button
    btn_newuser = web_browser.find_element(By.XPATH,
                                           "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # click existing user button
    btn_exist_acc = web_browser.find_element(By.LINK_TEXT,
                                          u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(valid_email)

    # add password
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    # click submit button
    btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(0.1)  # because I don't know yet how to wait for element to appear!
    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "login error"

    # find "My pets" link and click
    lnk_my_pets = web_browser.find_element(By.LINK_TEXT, u'Мои питомцы')
    lnk_my_pets.click()
    time.sleep(0.1)  # because I don't know yet how to wait for element to appear!
    # find element with user info
    usr_info = web_browser.find_element(By.CSS_SELECTOR, 'div.\.col-sm-4.left')
    user_text = usr_info.text
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(user_text)
        log_file.write('\n')
    t_lines = user_text.split('\n')
    pets_number = int(t_lines[1][10:])

    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(str(t_lines))
        log_file.write('\n')
        log_file.write(str(pets_number))
        log_file.write('\n')

    # find pets info
    images_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/th/img'
    names_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[1]'
    types_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[2]'
    ages_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[3]'
    rows = web_browser.find_elements(By.XPATH, images_xpath)
    images_data = []
    for r in rows:
        images_data.append(r.get_attribute('src') != '')

    rows = web_browser.find_elements(By.XPATH, names_xpath)
    names_data = []
    for r in rows:
        names_data.append(r.text)

    rows = web_browser.find_elements(By.XPATH, types_xpath)
    types_data = []
    for r in rows:
        types_data.append(r.text)

    rows = web_browser.find_elements(By.XPATH, ages_xpath)
    ages_data = []
    for r in rows:
        ages_data.append(r.text)
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(str(images_data))
        log_file.write('\n')
        log_file.write(str(names_data))
        log_file.write('\n')
        log_file.write(str(types_data))
        log_file.write('\n')
        log_file.write(str(ages_data))
        log_file.write('\n')

    # figure out that at least half of pets have photos
    with_images = len(list(filter(lambda x: x, images_data)))
    assert with_images / pets_number >= 0.5

    # figure out that all pets have name, age and type
    no_name = len(list(filter(lambda x: x == '', names_data)))
    no_type = len(list(filter(lambda x: x == '', types_data)))
    no_age = len(list(filter(lambda x: x == '', ages_data)))
    assert no_name == 0
    assert no_type == 0
    assert no_age == 0

    # figure out if duplicates exist
    # will zip arrays into "pet" tuples, then compare tuples
    pets = list(zip(names_data, types_data, ages_data))
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(str(pets))
        log_file.write('\n')
    no_dubs = True
    for i in range(1, len(pets)):
        if pets[i] == pets[i-1]:
            no_dubs = False
    assert no_dubs
