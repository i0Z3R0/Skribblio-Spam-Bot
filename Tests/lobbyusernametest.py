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
url = 'https://skribbl.io/'
botcount = 1

disconnect = False
pause = False
kicked = False
autoguess = False
botName = "DrawDetectorBot"

print('Starting...')

def playercountupdate():
	driver.implicitly_wait(3)
	playerCount = 0
	while playerCount < 1:
		playerCount = driver.find_element(By.XPATH, '//*[@id="containerGamePlayers"]').size['height'] / 48
	return int(playerCount)

def getlastchat():
	lastmsg = driver.find_element(By.XPATH, '//*[@id="boxMessages"]/p[last()]').text
	return lastmsg

def limitcheck():
	lastmsg = driver.find_element(By.XPATH, '//*[@id="boxMessages"]/p[last()]').text
	print(lastmsg)
	if lastmsg == "Spam detected! You're sending too many messages.":
		pause = True
		time.sleep(5)
		pause = False
		lastmsg = ''

def chatsend(message):
	print('Sending ' + message)
	driver.implicitly_wait(3)
	time.sleep(0.2)
	driver.find_element(By.XPATH, '//*[@id="inputChat"]').send_keys(message)
	driver.find_element(By.XPATH, '//*[@id="inputChat"]').submit()

def sendall(message):
	for i in tablist:
		driver.switch_to.window(i)
		try:
			chatsend(message)
		except Exception as e:
			pass


def initfunc():
	global driver
	global tablist
	global botcount
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--mute-audio")
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
	os.system('clear')

def findlobby():
	driver.get(url)
	driver.implicitly_wait(1)
	driver.find_element(By.XPATH, '//*[@id="inputName"]').clear()
	driver.find_element(By.XPATH, '//*[@id="inputName"]').send_keys(botName)
	time.sleep(0.2)
	# driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()
	print('1 Bot Ready to Join Game')
	driver.implicitly_wait(0.2)
	driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()
	# //*[@id="divFullscreenLoading"]
	# Adinplay Ad Xpath
	print('Joined Game')

initfunc()
findlobby()
os.system('clear')
print('Bots Are In The Game!')
samelobby = True
found = 0
fails = 0
while True:
	if found == 1:
		break
	if samelobby == True:
		try:
			driver.implicitly_wait(5)
			print("Typing in chat")
			driver.find_element(By.XPATH, '//*[@id="inputChat"]').send_keys("Connection Test")
			driver.find_element(By.XPATH, '//*[@id="inputChat"]').submit()
			print("Message sent")
			time.sleep(2)
		except:
			fails += 1
			if fails > 3:
				fails = 0
				driver.refresh()
				time.sleep(0.2)
				print('1 Bot Ready to Join Game')
				driver.implicitly_wait(0.2)
				driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()
				# //*[@id="divFullscreenLoading"]
				# Adinplay Ad Xpath
				print('Joined Game')
			else:
				continue

		try:
			print("Finding User With Name Draw")
			players = driver.find_elements(By.CLASS_NAME, 'name')
			for player in players:
				if "draw" in player.text:
					found = 1
					break

			print("Draw not found")
			chatsend('Hi, I am a bot and have detected no users with the word "draw" in their name. This is just a test.')
			time.sleep(0.3)
			driver.refresh()
			time.sleep(0.2)
			print('1 Bot Ready to Join Game')
			driver.implicitly_wait(0.2)
			driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()
			# //*[@id="divFullscreenLoading"]
			# Adinplay Ad Xpath
			print('Joined Game')
			continue
		except:
			pass

print("SAME LOBBY")
chatsend('Hi, I am a bot and have detected an user with the word "draw" in their name. This is just a test.')

aaaa = input("Any key to continue")

driver.quit()
