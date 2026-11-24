from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    #Открываем исходную страницу браузера
    driver.get("https://httpbin.qa-territory.online")
    driver.maximize_window()

    sleep(3)

    #Ищем и кликаем элемент кнопки "HTML Form"
    driver.find_element(By.CSS_SELECTOR, "a.util-link[href='/forms/post']").click()

    sleep(3)
    #получаем текущий урл страницы и сравниваем с нужным
    current_url = driver.current_url
    assert current_url == "https://httpbin.qa-territory.online/forms/post"

    sleep(3)
    #возвращаемся на преддыущую страницу
    driver.back()
    #ждем окончания перехода
    sleep(60)
    #проверяем что урл равен первоначальному
    assert current_url == "https://httpbin.qa-territory.online/"

    sleep(3)

    driver.quit()


test_navigation()
