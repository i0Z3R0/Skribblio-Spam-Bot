import time
import string
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = 'https://skribbl.io/' # No need to change this, unless you want the bot to join a single lobby every time...

headlessmode = False
botName = "ඞSussyBotඞ"
obnoxious = True
messages = ["ඞඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞඞ", "ඞඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞඞ", "ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ", "ඞඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞඞ"]
avatarv = "[0,28,13,-1]"

pause = False
kicked = False
attempt = 1
spamcount = 0
drawcount = 0
strokecount = 0
lobbycount = 0
playerspammed = 0
counter = 0

print('Starting...')

def chatsend(message):
	driver.implicitly_wait(2)
	driver.find_element(By.XPATH, '//*[@id="inputChat"]').send_keys(message)
	driver.find_element(By.XPATH, '//*[@id="inputChat"]').submit()

def initbot():
	global driver
	global avatarv
	caps = DesiredCapabilities().CHROME
	caps["pageLoadStrategy"] = "normal"
	chrome_options = Options()
	if headlessmode:
		chrome_options.add_argument("--headless")
	chrome_options.add_argument("--mute-audio")
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, desired_capabilities=caps)
	driver.get(url)
	time.sleep(2)
	driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", "avatar", avatarv)
	time.sleep(2)
	driver.refresh()
	print('Avatar Change Successful')
	os.system('clear')

def initspam():
	ctmp = input("Done? ")

def joinlobby():
	global attempt
	global lobbycount
	global playerspammed
	driver.get(url)
	driver.implicitly_wait(1.5)
	driver.find_element(By.XPATH, '//*[@id="inputName"]').clear()
	driver.find_element(By.XPATH, '//*[@id="inputName"]').send_keys(botName)
	time.sleep(0.2)
	driver.implicitly_wait(0.2)
	driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()
	try:
		driver.find_element(By.XPATH, '//*[@id="divFullscreenLoading"]')
		attempt += 1
		print('Ad Detected, Rejoining')
		joinlobby()
	except:
		pass
	print('Joined a Game')
	print('Checking Player Count')
	driver.implicitly_wait(1)
	pcount = playercountupdate()
	if pcount < playerMinThreshold:
		attempt += 1
		print("Too Little Players, Retrying")
		chatsend('Sorry, this lobby is too small for me to spam in')
		time.sleep(1)
		joinlobby()
	try:
		chatsend('Connection Test')
	except Exception as e:
		print('Error: ' + str(e))
	print(f'Found a Lobby! Attempts Taken: {attempt}\nPlayer Count: {pcount}')
	attempt = 1
	lobbycount += 1
	playerspammed += pcount

initbot()
joinlobby()
initspam()
os.system('clear')
printupdates()
kicked = False
while True:
	counter += 1
	joinlobby()
	initspam()
	os.system('clear')
	printupdates()
	kicked = False
	if counter == 10:
		print("Restarting Bot...")
		time.sleep(10)
		counter = 0
		driver.quit()
		initbot()

driver.quit()
