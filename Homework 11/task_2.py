# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
site = "https://fix-online.sbis.ru/"
site_authentication = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
wait = WebDriverWait(browser, 5, poll_frequency=1)

try:
    browser.get(site)
    wait.until(EC.url_to_be(site_authentication))
    browser.maximize_window()
    print("Проверить открытие авторизации")
    assert browser.current_url == site_authentication, "Неверный адрес сайта"
    sleep(1)
    login_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"]'
                                                                          ' .controls-Field')))
    login_field.click()
    login_field.send_keys("proletariat5")
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.controls-BaseButton__icon')))
    login_button.click()
    password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[type="password"]')))
    password_field.click()
    password_field.send_keys("Proletariat55")
    password_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.controls-BaseButton__icon')))
    password_button.click()

    print('Проверить адрес сайта')
    wait.until(EC.url_changes(site_authentication))
    assert browser.current_url == site, "Неверный адрес сайта"

    sleep(1)
    contacts_tab = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-name="contacts"] .NavigationPanels-Accordion__title')))
    contacts_tab.click()
    contacts_inner_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa='
                                                                                 '"NavigationPanels-SubMenu__head"]')))
    contacts_inner_tab.click()
    print('Проверить открытие вкладки "Контакты"')
    wait.until(EC.url_to_be('https://fix-online.sbis.ru/page/dialogs'))
    assert browser.current_url == 'https://fix-online.sbis.ru/page/dialogs', "Неверный адрес сайта"

    print('Отправляем сообщение самому себе')
    name = browser.find_element(By.CSS_SELECTOR, '[data-name="myProfile"] .NavigationPanels-Accordion__title')
    plus_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.icon-RoundPlus')))
    plus_button.click()
    search_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.controls-StackTemplate'
                                                                                 '__headerContentTemplate'
                                                                                 ' .controls-InputBase__nativeField')))
    sleep(1)
    search_field.send_keys(name.text)
    sleep(1)
    name_in_search_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.msg-addressee-item')))
    print("Проверить открытый диалог")
    name_in_search_field.click()
    yay = "Yay"
    message_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')))
    message_field.send_keys(yay)
    sleep(1)
    send_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')))
    send_button.click()
    sleep(1)
    message = browser.find_element(By.CSS_SELECTOR, ".msg-entity-layout__message-content")
    print("Проверить отправку сообщения")
    assert yay in message.text, "Сообщение не отправлено"
    message_2 = browser.find_element(By.CSS_SELECTOR, ".msg-entity-layout__message-content")
    action_chains = ActionChains(browser)
    action_chains.move_to_element(message_2)
    action_chains.context_click(message_2)
    action_chains.perform()
    delete_message = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.controls-icon_style-danger')))
    delete_message.click()
    print('Проверить подтверждение удаления')
    sleep(1)
    delete_popup_confirmation = browser.find_element(By.CSS_SELECTOR, '.controls-Confirmation_popup')
    assert delete_popup_confirmation.is_displayed(), "Попап не отображается"
    delete_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog'
                                                                            '__button-true"]')))
    delete_button.click()
    sleep(1)
    delete_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog'
                                                                            '__button-true"]')))
    delete_button.click()
    print('Проверить отсутствие сообщений')
    dialog = browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item')
    assert len(dialog) == 0, "Сообщение не удалилось"

finally:
        browser.quit()
