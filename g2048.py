#!usr/bin/env

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048')

htmlElem = browser.find_element_by_tag_name('html')
for i in range(500):
	rnum = randint(1,4)
	if rnum == 1:
		htmlElem.send_keys(Keys.UP)
	elif rnum == 2:	
		htmlElem.send_keys(Keys.RIGHT)
	elif rnum == 3:
		htmlElem.send_keys(Keys.DOWN)
	else:
		htmlElem.send_keys(Keys.LEFT)



