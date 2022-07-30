from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ser = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.maximize_window()

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)

language_selector = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[12]/div/div[1]/div[1]/div[2]')
language_selector.click()

time.sleep(6)

options_button = driver.find_element(By.CLASS_NAME, "subButton")
options_button.click()

time.sleep(3)

import_save = driver.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[4]/a[2]')
import_save.click()

import_prompt = driver.find_element(By.ID, "textareaPrompt")
import_prompt.send_keys(Keys.SHIFT + Keys.INSERT)

save_button = driver.find_element(By.ID, "promptOption0")
save_button.click()

close_menu_button = driver.find_element(By.XPATH, '//*[@id="menu"]/div[1]')
close_menu_button.click()

big_cookie = driver.find_element(By.ID, "bigCookie")
while True:
	timeout = time.time() + 10
	while time.time() < timeout:
		big_cookie.click()

	store = driver.find_elements(By.XPATH, '//*[@id="upgrades"]/div')
	store_list = []
	for item in store:
		if item.get_attribute("class") == "crate upgrade enabled":
			store_list.append(item)
	if store_list:
		store_list[-1].click()

	items = driver.find_elements(By.XPATH, '//*[@id="products"]/div')
	item_list = []
	for item in items:
		if item.get_attribute("class") == "product unlocked enabled":
			item_list.append(item)
	if item_list:
		item_list[-1].click()
