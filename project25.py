from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="C:/Users/1/PycharmProjects/pythonProject/chromdriver/chromedriver.exe")
@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/Users/1/PycharmProjects/pythonProject/chromdriver/chromedriver.exe')
   driver.implicitly_wait(10)

   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield


driver.set_window_size(1024, 600)
driver.maximize_window()

def test_show_my_pets():

   driver.get("http://petfriends1.herokuapp.com/login")
   element = driver.find_element_by_id('email')
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('Mavramira@yandex.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('321456')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')



def test_my_pets():
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')

    for i in range(len(names)):
       assert images[i].get_attribute('src') != ''
       assert names[i].text != ''
       assert descriptions[i].text != ''
       assert ', ' in descriptions[i]
       parts = descriptions[i].text.split(", ")
       assert len(parts[0]) > 0
       assert len(parts[1]) > 0


    element = WebDriverWait(pytest.driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")
    images = pytest.driver.find_elements_by_css_selector('.table.table-hover img')
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    pytest.driver.quit()

