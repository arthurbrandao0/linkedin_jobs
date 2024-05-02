# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
import time
import user_iterations
import constants


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def scroll_div_to_bottom(driver, div_element):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div_element)


chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1000,800")

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)


browser.get(constants.linkedin_url)
print("You are in Linkedin !")

# try:

username = browser.find_element(By.XPATH, constants.username_input_text_xpath)
password = browser.find_element(By.XPATH, constants.password_input_text_xpath)

username.send_keys(user_iterations.your_username)
password.send_keys(user_iterations.your_password)
print("You can see your account info written.")


login = browser.find_element(By.XPATH, constants.press_login_button_xpath)
login.click()
print("You can Logged In ! You can see your dashboard.")


browser.get(constants.jobs_linkedin_url)

time.sleep(3)

elementos = []
# Enquanto houver elementos novos, role a página e encontre mais elementos
while True:
    # Encontre todos os elementos correspondentes ao XPath atual
    novos_elementos = browser.find_elements(By.XPATH, constants.job_cards)

    # Se não houver novos elementos, pare de rolar
    if len(novos_elementos) == len(elementos):
        break

    # Adicione os novos elementos à lista de elementos
    elementos.extend(novos_elementos)

    # Role a página até o final
    scroll_div_to_bottom(browser, browser.find_element(By.XPATH, constants.scroll_div))

# # Agora, você pode fazer o que quiser com a lista de elementos encontrados
# for elemento in elementos:
#     print(elemento.text)
#
# elementos = browser.find_elements(By.XPATH, constants.job_cards)
#
# for i in elementos:
#     ActionChains(browser).move_to_element(i).perform()
#
#     try:
#         child = i.find_element(By.XPATH, constants.job_cards)
#         print('é patrocinado')
#     except:
#         print('não é patrocinado')
#

    # Aguarde alguns segundos para ver o destaque
    time.sleep(2)
print(len(elementos))
#
# messages = browser.find_element(By.XPATH, constants.messages_in_dashboard_xpath)
# messages.click()
# print("You can see Your Message Page.")
#
# time.sleep(3)
#
# new_messages = browser.find_element(By.XPATH, constants.new_message_button_xpath)
# new_messages.click()
# print("You can see Login Page.")
#
# time.sleep(4)
#
# message_for_who = browser.find_element_by_class_name(constants.message_for_who_input_text)
# message_for_who.send_keys(user_iterations.person_you_want_to_send_message)
# print("You can write the person who want to send a message.")
#
# time.sleep(4)
#
# message_text = browser.find_element_by_css_selector(constants.message_text_css_selector)
# message_text.send_keys(user_iterations.message_you_want_to_send)
# print("You can see your message.")
#
# print("Browser will close in 10 seconds")
# time.sleep(10)
browser.close()

# except Exception as error:
#     browser.close()
#     print("There is an error :", error.message)