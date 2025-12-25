from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password


def test_show_all_pets(web_browser):
    web_browser.implicitly_wait(5)
    # Вводим email
    web_browser.find_element(By.ID, 'email').send_keys(valid_email)
    # Вводим пароль
    web_browser.find_element(By.ID, 'pass').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    web_browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert web_browser.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    images = web_browser.find_elements(
        By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = web_browser.find_elements(
        By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = web_browser.find_elements(
        By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_all_user_pets_shown(web_browser):
    # enter email
    field_email = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "email")))
    field_email.clear()
    field_email.send_keys(valid_email)

    # enter password
    field_pass = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "pass")))
    field_pass.clear()
    field_pass.send_keys(valid_password)

    # click submit button
    btn_submit = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.XPATH, "//button[@type='submit']")))
    btn_submit.click()

    # find "My pets" link and click
    lnk_my_pets = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.LINK_TEXT, u'Мои питомцы')))
    lnk_my_pets.click()

    # find pets number in user info
    usr_info = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, 'div.\.col-sm-4.left')))
    user_text = usr_info.text.split('\n')
    pets_number = int(user_text[1][10:])

    # find number of rows in table
    rows_xpath = '//*[@id="all_my_pets"]/table/tbody/tr'
    rows = WebDriverWait(web_browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, rows_xpath)))
    assert len(rows) == pets_number


def test_half_pets_have_photo(web_browser):
    # enter email
    field_email = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "email")))
    field_email.clear()
    field_email.send_keys(valid_email)

    # enter password
    field_pass = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "pass")))
    field_pass.clear()
    field_pass.send_keys(valid_password)

    # click submit button
    btn_submit = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.XPATH, "//button[@type='submit']")))
    btn_submit.click()

    # find "My pets" link and click
    lnk_my_pets = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.LINK_TEXT, u'Мои питомцы')))
    lnk_my_pets.click()

    # find pets number
    usr_info = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, 'div.\.col-sm-4.left')))
    user_text = usr_info.text.split('\n')
    pets_number = int(user_text[1][10:])

    # find pets info
    images_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/th/img'
    rows = WebDriverWait(web_browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, images_xpath)))
    images_data = []
    for r in rows:
        images_data.append(r.get_attribute('src') != '')

    # figure out that at least half of pets have photos
    with_images = len(list(filter(lambda x: x, images_data)))
    assert with_images / pets_number >= 0.5


def test_all_user_pets_have_data(web_browser):
    # enter email
    field_email = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "email")))
    field_email.clear()
    field_email.send_keys(valid_email)

    # enter password
    field_pass = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "pass")))
    field_pass.clear()
    field_pass.send_keys(valid_password)

    # click submit button
    btn_submit = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.XPATH, "//button[@type='submit']")))
    btn_submit.click()

    # find "My pets" link and click
    lnk_my_pets = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.LINK_TEXT, u'Мои питомцы')))
    lnk_my_pets.click()

    # find pets info
    names_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[1]'
    types_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[2]'
    ages_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[3]'

    rows = WebDriverWait(web_browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, names_xpath)))
    names_data = []
    for r in rows:
        names_data.append(r.text)

    rows = WebDriverWait(web_browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, types_xpath)))
    types_data = []
    for r in rows:
        types_data.append(r.text)

    rows = WebDriverWait(web_browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, ages_xpath)))
    ages_data = []
    for r in rows:
        ages_data.append(r.text)

    # figure out that all pets have name, age and type
    no_name = len(list(filter(lambda x: x == '', names_data)))
    no_type = len(list(filter(lambda x: x == '', types_data)))
    no_age = len(list(filter(lambda x: x == '', ages_data)))
    assert (no_name == 0 and no_type == 0 and no_age == 0)


def test_all_user_pets_have_diff_names(web_browser):
    # enter email
    field_email = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "email")))
    field_email.clear()
    field_email.send_keys(valid_email)

    # enter password
    field_pass = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "pass")))
    field_pass.clear()
    field_pass.send_keys(valid_password)

    # click submit button
    btn_submit = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.XPATH, "//button[@type='submit']")))
    btn_submit.click()

    # find "My pets" link and click
    lnk_my_pets = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.LINK_TEXT, u'Мои питомцы')))
    lnk_my_pets.click()

    # find pets info
    names_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[1]'

    rows = WebDriverWait(web_browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, names_xpath)))
    names_data = []
    for r in rows:
        names_data.append(r.text)
    diff_names = True
    for i in range(1, len(names_data)):
        if names_data[i] == names_data[i-1]:
            diff_names = False
    assert diff_names


def test_no_duplicates_exist(web_browser):
    # enter email
    field_email = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "email")))
    field_email.clear()
    field_email.send_keys(valid_email)

    # enter password
    field_pass = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "pass")))
    field_pass.clear()
    field_pass.send_keys(valid_password)

    # click submit button
    btn_submit = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.XPATH, "//button[@type='submit']")))
    btn_submit.click()

    # find "My pets" link and click
    lnk_my_pets = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((
            By.LINK_TEXT, u'Мои питомцы')))
    lnk_my_pets.click()

    # find pets info
    names_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[1]'
    types_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[2]'
    ages_xpath = '//*[@id="all_my_pets"]/table/tbody/tr/td[3]'

    rows = WebDriverWait(web_browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, names_xpath)))
    names_data = []
    for r in rows:
        names_data.append(r.text)

    rows = WebDriverWait(web_browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, types_xpath)))
    types_data = []
    for r in rows:
        types_data.append(r.text)

    rows = WebDriverWait(web_browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, ages_xpath)))
    ages_data = []
    for r in rows:
        ages_data.append(r.text)

    # figure out if duplicates exist
    # will zip arrays into "pet" tuples, then compare tuples
    pets = list(zip(names_data, types_data, ages_data))
    no_dubs = True
    for i in range(1, len(pets)):
        if pets[i] == pets[i-1]:
            no_dubs = False
    assert no_dubs
