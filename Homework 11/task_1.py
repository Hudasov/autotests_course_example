# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sbis_site = "https://sbis.ru/"

try:
    driver.get(sbis_site)
    driver.maximize_window()
    print("Проверить адрес сайта")
    assert driver.current_url == sbis_site, "Неверный адрес сайта"

    contacts = driver.find_element(By.CSS_SELECTOR, ".sbisru-Header__menu-link[href='/contacts']")
    print('Проверить наличие кнопки "Контакты"')
    assert contacts.is_displayed(), '"Контакты" не отображаются'

    print('Перейти в раздел "Контакты"')
    contacts.click()
    sbis_site_contacts_title = 'СБИС Контакты — Ярославская область'
    print('Проверить текущее положение - вкладка "Контакты"')
    assert driver.title == sbis_site_contacts_title

    tensor_banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor') # [title="tensor.ru"]
    print('Проверить наличие баннера Тензор')
    assert tensor_banner.is_displayed(), "Баннер не отображается"

    print("Перейти на https://tensor.ru/")
    tensor_banner.click()
    driver.switch_to.window(driver.window_handles[-1])
    print("Проверить адрес страницы == tensor.ru")
    assert driver.current_url == 'https://tensor.ru/'

    print('Проверить наличие блока "Сила в людях"')
    mens_power = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert mens_power.is_displayed(), 'Блок "Сила в людях" отсутствует'
    print('Перейти в раздел "О компании" по кнопке "Подробнее"')
    more_details = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link')
    driver.execute_script("return arguments[0].scrollIntoView(true);", more_details)
    more_details.click()
    print("Проверить текущее положение - страница https://tensor.ru/about")
    assert driver.current_url == "https://tensor.ru/about"

finally:
    driver.quit()


