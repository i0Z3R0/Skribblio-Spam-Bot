import time
import string
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import fnmatch

#url = 'https://skribbl.io/?XXXXXXXXXXXX'
url = 'https://skribbl.io/?acx2xZISexim'
headlessmode = True
botcount = 6
botName = "ProSpammer"
avatarv = "[0,28,13,-1]"

print('Starting...')

amogus = ["ඞඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞ SUS ඞඞ", "ඞඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞ SUSSY BAKA ඞඞ", "ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ", "ඞඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞ AMOGUS ඞඞ"]
pause = False
kicked = False
autoguess = False

def playercountupdate():
	driver.implicitly_wait(3)
	playerCount = 0
	while playerCount < 1:
		playerCount = driver.find_element(By.XPATH, '//*[@id="containerGamePlayers"]').size['height'] / 48
	return int(playerCount)

#def kickcheck():
#	for i in tablist:
#		driver.switch_to.window(i)
#		try:
#			driver.find_element(By.XPATH, '//*[@id="modalKicked"]')
#			print('One Bot Kicked, Trying to Rejoin')
#			driver.refresh()
#			driver.implicitly_wait(0.2)
#			driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()


def getlastchat():
	lastmsg = driver.find_element(By.XPATH, '//*[@id="boxMessages"]/p[last()]').text
	return lastmsg

def limitcheck():
	lastmsg = driver.find_element(By.XPATH, '//*[@id="boxMessages"]/p[last()]').text
	if lastmsg == "Spam detected! You're sending too many messages.":
		pause = True
		time.sleep(5)
		pause = False
		lastmsg = ''

def chatsend(message):
	print('Sending ' + message)
	driver.implicitly_wait(2)
	driver.find_element(By.XPATH, '//*[@id="inputChat"]').send_keys(message)
	driver.find_element(By.XPATH, '//*[@id="inputChat"]').submit()

def sendall(message):
	for i in tablist:
		driver.switch_to.window(i)
		try:
			chatsend(message)
		except Exception as e:
			pass

def updateword():
	global drawword
	global correctword
	global wordlength
	global halfword
	for i in tablist:
		driver.switch_to.window(i)

		try:
			drawword = driver.find_element(By.XPATH, '//*[@id="overlay"]/div/div[3]/div[1]')
			drawword.click()
			correctword = drawword.text
			wordlength = len(correctword)
			break
		except Exception as e:
			pass

		try:
			guessword = driver.find_element(By.XPATH, '//*[@id="currentWord"]').text
			if "_" not in guessword:
				correctword = guessword
				wordlength = len(guessword)
			elif len(set(guessword)) > 1:
				halfword = guessword
				wordlength = len(guessword)
			else:
				wordlength = len(guessword)
		except Exception as e:
			pass

def initbot():
	global driver
	global tablist
	global botcount
	caps = DesiredCapabilities().CHROME
	caps["pageLoadStrategy"] = "none"
	chrome_options = Options()
	if headlessmode:
		chrome_options.add_argument("--headless")
	chrome_options.add_argument("--mute-audio")
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, desired_capabilities=caps)
	os.system('clear')
	tablist = []

	# Avatar Bot
	driver.get(url)
	time.sleep(3)
	driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", "avatar", avatarv)
	print('Bot Avatar Change Successful')
	driver.refresh()
	driver.implicitly_wait(1.5)
	driver.find_element(By.XPATH, '//*[@id="inputName"]').clear()
	driver.find_element(By.XPATH, '//*[@id="inputName"]').send_keys(botName + str(1))
	time.sleep(0.1)
	tablist.append(driver.current_window_handle)
	print('1 Bot Ready to Join Game')
	for i in range(botcount - 1):
		driver.switch_to.new_window('tab')
		driver.get(url)
		driver.implicitly_wait(1.5)
		driver.find_element(By.XPATH, '//*[@id="inputName"]').clear()
		driver.find_element(By.XPATH, '//*[@id="inputName"]').send_keys(botName + str(i))
		time.sleep(0.1)
		tablist.append(driver.current_window_handle)
		print('1 Bot Ready to Join Game')
	tempvar = input("Press Enter to Join")
	for i in tablist:
		driver.switch_to.window(i)
		driver.implicitly_wait(0.2)
		driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()
		#try:
		#	driver.find_element(By.XPATH, '//*[@id="divFullscreenLoading"]')
		#	print("One Bot Stuck On Ad, Closing Window")
		#	tablist.remove(i)
		#	driver.close()
		#except:
		#	pass
		# //*[@id="divFullscreenLoading"]
		# Xpath for Adinplay Ads
		print('Sent 1 Bot to Join Game')

initbot()
os.system('clear')
print('Bots Are In The Game!')
tempvar = input("Press Enter to Test Connection")
try:
	for i in tablist:
		driver.switch_to.window(i)
		chatsend("Connection Test")
except Exception as e:
	if "Message: element not interactable" in str(e):
		print('One Bot Stuck On Ad, Closing Window')
		tablist.remove(i)
		driver.close()

while True:
	if autoguess == False:
		chatmsg = input("Message to Send: ")

	if chatmsg == "!ag" or chatmsg == "!autoguess":
		autoguess = True

	if chatmsg == "!au" or chatmsg == "!amogus":
		for message in amogus:
			sendall(message)

	if chatmsg == "!c" or chatmsg == "!clear":
		os.system('clear')
		continue

	if chatmsg == "!tu" or chatmsg == "!thumbsup":
		for i in tablist:
			driver.switch_to.window(i)
			try:
				driver.find_element(By.XPATH, '//*[@id="rateDrawing"]/div[1]/div').click()
			except Exception as e:
				pass
		time.sleep(0.5)
		continue

	if chatmsg == "!td" or chatmsg == "!thumbsdown":
		for i in tablist:
			driver.switch_to.window(i)
			try:
				driver.find_element(By.XPATH, '//*[@id="rateDrawing"]/div[2]/div').click()
			except Exception as e:
				pass
		time.sleep(0.5)
		continue

	if chatmsg == "!vk" or chatmsg == "!votekick":
		for i in tablist:
			driver.switch_to.window(i)
			try:
				time.sleep(1)
				driver.implicitly_wait(1)
				driver.find_element(By.XPATH, '//*[@id="votekickCurrentplayer"]').click()
			except Exception as e:
				pass
		time.sleep(0.75)
		continue

	if autoguess == True:
		possible = []
		count = 0
		totalcount = 0
		correctword = ' '
		halfword = ''
		wordlength = 0

		updateword()

		print('Length of Word: ' + str(wordlength))

		if correctword != ' ':
			autoguess = False
			sendall(f"The word is: {correctword}")
			sendall(correctword)
			print('Word: ' + correctword)
			continue

		f = open('wordlist.txt', 'r')
		for line in f:
			testword = line.strip('\n')
			if halfword != '':
				halfdot = halfword.replace("_", ".")
				if len(testword) == wordlength:
					reg = re.compile(halfdot)
					if bool(re.match(reg, testword)):
						possible.append(testword)
			else:
				if len(testword) == wordlength:
					possible.append(testword)

		for word in possible:
			if count == botcount - 1:
				count = 0
			driver.switch_to.window(tablist[count])
			try:
				chatsend(word)
				time.sleep(0.15)
				lastchat = getlastchat()

				if botName in lastchat and "guessed the word" in lastchat:
					print("Word Was Guessed")
					correctword = possible[totalcount]
					autoguess = False
					sendall(correctword)
					break
				else:
					if "Spam detected" in lastchat:
						time.sleep(2)
			except Exception as e:
				if "Message: element not interactable" in str(e):
					print('One Bot Stuck On Ad, Closing Window')
					tablist.remove(i)
					driver.close()
			count += 1
			totalcount += 1
		print("Done")
		autoguess = False
		continue
	elif autoguess == False:
		for i in tablist:
			driver.switch_to.window(i)
			try:
				chatsend(chatmsg)
			except Exception as e:
				if "Message: element not interactable" in str(e):
					print('One Bot Stuck On Ad, Closing Window')
					tablist.remove(i)
					driver.close()

	if chatmsg == "!leave":
		time.sleep(1)
		break

	time.sleep(0.25)

	# print(f'Player Count: {playercountupdate()}')

driver.quit()
