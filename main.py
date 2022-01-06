import time
import random
import string
import os
from threading import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


playerMinThreshold = 3 #Enter the minimum player threshold you desire (Note that the threshold includes the bot as well)
url = 'https://skribbl.io/?leObnzUv5UdR'

disconnect = False
pause = False
endthreads = False
kicked = False

print('Starting...')

def playercountupdate():
	driver.implicitly_wait(3)
	playerCount = 0
	while playerCount < 1:
		playerCount = driver.find_element(By.XPATH, '//*[@id="containerGamePlayers"]').size['height'] / 48
	return playerCount

def limitcheck():
	lastmsg = driver.find_element(By.XPATH, '//*[@id="boxMessages"]/p[last()]').text
	print(lastmsg)
	if lastmsg == "Spam detected! You're sending too many messages.":
		pause = True
		time.sleep(5)
		pause = False
		lastmsg = ''

def chatsend(message):
	# print('Sending ' + message)
	driver.implicitly_wait(5)
	driver.find_element(By.XPATH, '//*[@id="inputChat"]').send_keys(message)
	driver.find_element(By.XPATH, '//*[@id="inputChat"]').submit()

def initfunc():
	global driver
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--mute-audio")
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
	os.system('clear')
	tablist = []
	botcount = 12
	for i in range(botcount):
		driver.switch_to.new_window('tab')
		driver.get(url)
		driver.implicitly_wait(3)
		driver.find_element(By.XPATH, '//*[@id="inputName"]').clear()
		driver.find_element(By.XPATH, '//*[@id="inputName"]').send_keys('sub 2 mr beast')
		time.sleep(0.75)
		# driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()
		tablist.append(driver.current_window_handle)
		print('1 Bot Ready to Join Game')
	for i in range(botcount):
		driver.switch_to.window(tablist[i])
		time.sleep(0.5)
		driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()
		print('Sent 1 Bot to Join Game')

#Bot function
initfunc()
#print(f'Player Count: {playercountupdate()}')
#while True:
#	limitcheck()
#	if pause == False:
#		chatsend("hi")
#		time.sleep(1.1)
#	else:
#		time.sleep(0.5)
# driver.quit()
