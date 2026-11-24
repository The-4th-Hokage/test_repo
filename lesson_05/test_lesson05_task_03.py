from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_multiple_elements():
    driver = webdriver.Chrome()
    #Переходим на изначальную страницу
    driver.get("https://httpbin.qa-territory.online/links/10")
    driver.maximize_window()

    sleep(3)

    #Ищем все эелменты тега "а"
    tag_a_links = driver.find_elements(By.TAG_NAME, "a")

    #проверяем что количество элементов = 9
    assert len(tag_a_links) == 9

    #проверяем что все ссылки отображаются на странице
    for elem in tag_a_links:
        if elem.is_displayed():
            print(f"Ссылка {elem} отображается на странице")
        else:
            print(f"Ссылка {elem} не отображается на странице")

    #Проверяем что первая запись в списке содержит "1"
    if tag_a_links:
        first_link = tag_a_links[0].text.strip()
        symbol = "1"
        if symbol in first_link:
            print("Символ есть в первой ссылке")
        else:
            print("Символа нет в первой ссылке")
    else:
        print("Список пуст")
        
    driver.quit()

test_multiple_elements()
