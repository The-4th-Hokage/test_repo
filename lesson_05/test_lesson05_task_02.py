from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome()
    #Открываем исходную страницу
    driver.get("https://httpbin.qa-territory.online/forms/post")
    driver.maximize_window()

    sleep(3)

    #Ищем и заполняем поле "custname" своим именем
    driver.find_element(By.ID, "custname").send_keys("Миша")

    sleep(3)

    #Ищем кнопку "Submit" и нажимаем на нее
    driver.find_element(By.XPATH, "//button[normalize-space() = 'Submit']").click()

    sleep(3)

    #Проверяем текущий урл (непонятно на что он должен был поменяться)
    driver.current_url

    driver.quit()

test_form_submission()
