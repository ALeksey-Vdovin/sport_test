import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://aleksey-vdovin.github.io/sport_test/")
time.sleep(2)

row_one = driver.find_element_by_id('block1')  
row_one.click()
color = row_one.value_of_css_property('background-color')
valid_color = 'rgba(255, 0, 0, 1)'
if color == valid_color:
	print("Тест 1 пройден (цвет поменялся на красный)")
else:
	print('Тест 1 провален')
time.sleep(2)

row_two = driver.find_element_by_id('block2')  
row_two.click()
text = driver.find_element_by_id('block2').text
valid_text = 'Вы нажали на вторую колонку'
if text == valid_text:
	print("Тест 2 пройден (текст изменился)")
else:
	print('Тест 2 провален')
time.sleep(2)

button = driver.find_element_by_id('block3')  
button.click()
none = button.value_of_css_property('display')
valid_property = 'none'
if none == valid_property:
	print("Тест 3 пройден (третья колонка исчезла)")
else:
	print('Тест 3 провален')
time.sleep(4)

driver.quit()
