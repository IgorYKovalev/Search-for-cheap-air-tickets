from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time


options = Options()
# options.add_argument('--headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')

driver = webdriver.Firefox(options=options)


try:
    driver.get('https://www.aviasales.ru')
    driver.maximize_window()
    time.sleep(3)

    from_input = driver.find_element(By.ID, "avia_form_origin-input")
    from_input.clear()
    from_input.send_keys("Нижний Новгород")
    time.sleep(3)

    to_input = driver.find_element(By.ID, "avia_form_destination-input")
    to_input.clear()
    to_input.send_keys("Москва")
    time.sleep(3)

    iframe = driver.find_element(By.CSS_SELECTOR, "#credential_picker_container > iframe")
    driver.switch_to.frame(iframe)
    driver.find_element(By.ID, "close").click()
    driver.switch_to.default_content()
    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test-id="start-date-field"]')))
    element.click()
    time.sleep(3)

    month = Select(driver.find_element(By.CSS_SELECTOR, '[data-test-id="select-month"]'))
    month.select_by_visible_text('Май')
    time.sleep(3)

    data = driver.find_element(By.XPATH, '//div[text()="3"]')
    data.click()
    time.sleep(3)

    data_return = driver.find_element(By.XPATH, '//div[@aria-selected="false"]').send_keys(Keys.RETURN)
    time.sleep(3)

    return_ticket = driver.find_element(By.CSS_SELECTOR, '[data-test-id="calendar-action-button"]')
    return_ticket.click()
    time.sleep(3)

    button = driver.find_element(By.CSS_SELECTOR, '[data-test-id="form-submit"]')
    button.click()
    time.sleep(30)

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    time.sleep(5)

    driver.save_full_page_screenshot('/Users/kovalevigor/Desktop/screen.png')

    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # time.sleep(5)

    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)  # Прокрутка страницы вниз на один экран.
    time.sleep(5)
    body.send_keys(Keys.PAGE_UP)
    time.sleep(5)

    driver.save_screenshot('screenshot.png')
    
except Exception as es:
    print(es)
    print("Ошибка!!!")

finally:
    driver.quit()
