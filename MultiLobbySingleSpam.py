import time
import string
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

playerMinThreshold = 1 # Includes you
url = 'https://skribbl.io/'

colors = {'white': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[1]',
'black': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[1]',
'lgrey': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[2]',
'dgrey': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[2]',
'red': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[3]',
'dred': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[3]',
'orange': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[4]',
'dorange': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[4]',
'yellow': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[5]',
'dyellow': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[5]',
'green': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[6]',
'dgreen': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[6]',
'lblue': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[7]',
'dlblue': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[7]',
'blue': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[8]',
'dblue': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[8]',
'purple': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[9]',
'dpurple': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[9]',
'pink': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[10]',
'dpink': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[10]',
'brown': '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[11]',
'dbrown': '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[11]'}
drawtools = {'pen': '//*[@id="containerBoard"]/div[2]/div[3]/div[1]',
'eraser': '//*[@id="containerBoard"]/div[2]/div[3]/div[2]',
'fill': '//*[@id="containerBoard"]/div[2]/div[3]/div[3]',
'brush1': '//*[@id="containerBoard"]/div[2]/div[4]/div[1]',
'brush2': '//*[@id="containerBoard"]/div[2]/div[4]/div[2]',
'brush3': '//*[@id="containerBoard"]/div[2]/div[4]/div[3]',
'brush4': '//*[@id="containerBoard"]/div[2]/div[4]/div[4]',
'clear': '//*[@id="buttonClearCanvas"]',
'canvas': '//*[@id="canvasGame"]'
}
pause = False
kicked = False
botName = "BestSpamBot"
attempt = 1
obnoxious = True
messages = ["You all suck at this game", "Hi I am here to annoy you", "How is everybody today?", "Please let me know if you like my spamming"]

print('Starting...')

def playercountupdate():
	driver.implicitly_wait(3)
	playerCount = 0
	while playerCount < 1:
		playerCount = driver.find_element(By.XPATH, '//*[@id="containerGamePlayers"]').size['height'] / 48
	return int(playerCount)

def kickcheck():
	if obnoxious:
		chatsend("Checking if kicked...")
	try:
		if (driver.find_element(By.XPATH, '//*[@id="modalKicked"]/div/div/div[1]/h4').text) == "You have been kicked.":
			return True
	except:
		return False

def getlastchat():
	lastmsg = driver.find_element(By.XPATH, '//*[@id="boxMessages"]/p[last()]').text
	return lastmsg

def limitcheck():
	lastmsg = driver.find_element(By.XPATH, '//*[@id="boxMessages"]/p[last()]').text
	if lastmsg == "Spam detected! You're sending too many messages.":
		pause = True
		time.sleep(3)
		pause = False
		lastmsg = ''

def chatsend(message):
	driver.implicitly_wait(2)
	try:
		driver.find_element(By.XPATH, '//*[@id="inputChat"]').send_keys(message)
		driver.find_element(By.XPATH, '//*[@id="inputChat"]').submit()
	except:
		pass

def checkdraw():
	if obnoxious:
		chatsend("Checking for draw popup...")
	try:
		drawword = driver.find_element(By.XPATH, '//*[@id="overlay"]/div/div[3]/div[1]')
		drawword.click()
		return True
	except:
		return False

def drawspam():
	print("Starting to Draw")
	try:
		driver.find_element(By.XPATH, drawtools["fill"]).click()
	except:
		# Spawnnkilled on draw turn oof
		# Didn't even add this until people spawnkilled me lol
		return True
	while True:
		try:
			driver.implicitly_wait(0.5)
			time.sleep(0.05)
			driver.find_element(By.XPATH, colors["black"]).click()
			driver.implicitly_wait(0.5)
			time.sleep(0.05)
			driver.find_element(By.XPATH, drawtools["canvas"]).click()
			driver.implicitly_wait(0.5)
			time.sleep(0.075)
			driver.find_element(By.XPATH, drawtools["clear"]).click()
		except:
			return True

def initbot():
	global driver
	caps = DesiredCapabilities().CHROME
	caps["pageLoadStrategy"] = "normal"
	chrome_options = Options()
	# chrome_options.add_argument("--headless")
	chrome_options.add_argument("--mute-audio")
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, desired_capabilities=caps)
	os.system('clear')

def initspam():
	print('Starting Spam')
	scounter = 0
	while True:
		for message in messages:
			if scounter % 10 == 0 and scounter != 0:
				if checkdraw() == True:
					drawspam()
			if scounter % 20 == 0 and scounter != 0:
				if kickcheck() == True:
					print("Kicked, Rejoining")
					return True
				else:
					scounter = 0
					continue
			chatsend(message)
			scounter += 1
			time.sleep(0.85)
			limitcheck()

def joinlobby():
	global attempt
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
		joinlobby()
	try:
		chatsend('Connection Test')
	except Exception as e:
		print('Error: ' + str(e))
	print(f'Found a Lobby! Attempts Taken: {attempt}\nPlayer Count: {pcount}')
	attempt = 0

initbot()

while True:
	joinlobby()
	initspam()

driver.quit()
