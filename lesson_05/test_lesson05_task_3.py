from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    # Переходим на изначальную страницу
    driver.get("https://httpbin.qa-territory.online/links/10")
    driver.maximize_window()

    sleep(3)

    # Ищем все эелменты тега "а"
    tag_a_links = driver.find_elements(By.TAG_NAME, "a")

    # Проверяем что количество элементов = 9
    assert len(tag_a_links) == 9

    # Проверяем что все ссылки отображаются на странице
    for elem in tag_a_links:
        assert elem.is_displayed(), f"Ссылка {elem} не отображается"

    # Проверяем что первая запись в списке содержит "1"
    first_link = tag_a_links[0].text.strip()
    assert "1" in first_link, f"В первой ссылке нет '1': {first_link}"

    driver.quit()
