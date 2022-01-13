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
playerMinThreshold = 5 # Includes you
botName = "SpammerBot"
obnoxious = True
messages = ["You all suck at this game LOL",
"Hi I am here to annoy you",
"How is everybody today?",
"Please let me know if you like my ☣️spamming",
"Thank you for your valuable feedback!",
"Does anybody here play Fortnite?",
"👍Like, subscribe, and hit that notification 🔔bell!",
"Guys let's votekick this person",
"Wait until I draw, I have great artistic talent",
"#🌊TeamSeasOP #🌊TeamSeasOP SAY IT WITH ME!!!",
"Imagine playing skribbl.io😂",
"Please don't kick me, I like it here 🥺",
"Watch this video to install the bot: youtube com/watch?v=dQw4w9WgXcQ"]

pause = False
kicked = False
attempt = 1
spamcount = 0
drawcount = 0
strokecount = 0
lobbycount = 0
playerspammed = 0

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
'canvas': '//*[@id="canvasGame"]'}

print('Starting...')

def playercountupdate():
	driver.implicitly_wait(3)
	playerCount = 0
	if obnoxious:
		chatsend('Checking player count...')
	while playerCount < 1:
		try:
			playerCount = driver.find_element(By.XPATH, '//*[@id="containerGamePlayers"]').size['height'] / 48
		except:
			return 0
	return int(playerCount)

def kickcheck():
	if obnoxious:
		try:
			chatsend("Checking if kicked...")
		except:
			return True
	try:
		if (driver.find_element(By.XPATH, '//*[@id="modalKicked"]/div/div/div[1]/h4').text) == "You have been kicked.":
			return True
		if (driver.find_element(By.XPATH, '//*[@id="modalDisconnect"]/div/div/div[1]/h4').text) == "Connection lost.":
			return True
	except:
		return False

def getlastchat():
	lastmsg = driver.find_element(By.XPATH, '//*[@id="boxMessages"]/p[last()]').text
	return lastmsg

def limitcheck():
	try:
		lastmsg = driver.find_element(By.XPATH, '//*[@id="boxMessages"]/p[last()]').text
	except:
		# Don't need to initiate lobby rejoin, it'll happen automatically later
		# This optimizes the code a bit
		pass
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
		if obnoxious:
			chatsend(botName + " may not be held liable for any damage caused or sustained by...")
			time.sleep(0.9)
			chatsend("the following actions, including any damage caused to third parties as a consequence of...")
			time.sleep(0.9)
			chatsend("or during the implementation of the action.")
			time.sleep(0.9)
			chatsend("Photosensitivity warning!")
	except:
		return False
	# Added this part below because sometimes the draw popup
	# would time out and the game would choose a random word
	# Then the bot would think it's not its turn to draw
	# So this is my temporary fix
	try:
		drawword.click()
		return True
	except:
		return True

def drawspam():
	global drawcount
	global strokecount
	print("Starting to Draw")
	try:
		driver.find_element(By.XPATH, drawtools["fill"]).click()
		driver.implicitly_wait(0.5)
		time.sleep(0.01)
		driver.find_element(By.XPATH, colors["black"]).click()
	except:
		# Spawnnkilled on draw turn...oof
		# Didn't even add this until people spawnkilled me lol
		return True
	drawcount += 1
	while True:
		try:
			driver.implicitly_wait(0.1)
			time.sleep(0.1)
			driver.find_element(By.XPATH, drawtools["canvas"]).click()
			strokecount += 1
			driver.implicitly_wait(0.1)
			time.sleep(0.1)
			driver.find_element(By.XPATH, drawtools["clear"]).click()
			strokecount += 1
			if (strokecount % 10 == 0 or strokecount % 21 == 0) and strokecount != 0:
				try:
					chatsend("Are you guys enjoying my drawing?")
					if kickcheck() == True:
						print('Kicked, Rejoining')
						return True
					driver.find_element(By.XPATH, drawtools["fill"]).click()
					driver.implicitly_wait(0.5)
				except:
					print('Kicked, Rejoining')
					return True
		except:
			return True

def printupdates():
	global spamcount
	global drawcount
	global strokecount
	global lobbycount
	print(f'Spammed a total of {spamcount} messages in {lobbycount} lobbies')
	print(f'Drawed a total of {drawcount} times in {lobbycount} lobbies')
	print(f'Flashed lights a total of {strokecount} times in {lobbycount} lobbies')
	print(f'Annoyed a total of {playerspammed} players in {lobbycount} lobbies')

def initbot():
	global driver
	caps = DesiredCapabilities().CHROME
	caps["pageLoadStrategy"] = "normal"
	chrome_options = Options()
	if headlessmode:
		chrome_options.add_argument("--headless")
	chrome_options.add_argument("--mute-audio")
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, desired_capabilities=caps)
	os.system('clear')

def initspam():
	global spamcount
	print('Starting Spam')
	scounter = 0
	while True:
		for message in messages:
			if scounter % 10 == 0 and scounter != 0:
				if checkdraw() == True:
					drawspam()
			if scounter == 20:
				if kickcheck() == True:
					print("Kicked, Rejoining")
					return True
			if scounter == 30:
				if playercountupdate() < playerMinThreshold:
					print('Not enough players, leaving lobby')
					time.sleep(0.75)
					if obnoxious:
						chatsend("Not enough players, I'm out of here")
					return True
				else:
					scounter = 0
			try:
				chatsend(message)
			except:
				print('Kicked, Rejoining')
				return True
			spamcount += 1
			scounter += 1
			time.sleep(0.85)
			limitcheck()

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

while True:
	joinlobby()
	initspam()
	printupdates()

driver.quit()
