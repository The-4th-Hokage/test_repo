from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    # Открываем исходную страницу браузера
    driver.get("https://httpbin.qa-territory.online")
    driver.maximize_window()

    sleep(3)

    # Ищем и кликаем элемент кнопки "HTML Form"
    driver.find_element(By.CSS_SELECTOR,
                        "a.util-link[href='/forms/post']").click()

    # Получаем текущий урл страницы и сравниваем с нужным
    current_url = driver.current_url
    assert current_url == "https://httpbin.qa-territory.online/forms/post"

    # Возвращаемся на преддыущую страницу
    driver.back()
    # Ждем окончания перехода
    sleep(3)
    # Проверяем что урл равен первоначальному
    assert driver.current_url == "https://httpbin.qa-territory.online"

    driver.quit()
