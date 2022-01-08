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
url = 'https://skribbl.io/?abl7KtJTRwJp'
botcount = 6

disconnect = False
pause = False
kicked = False
autoguess = False
botName = "prodrawer69"

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


def initfunc():
	global driver
	global tablist
	global botcount
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--mute-audio")
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
	os.system('clear')
	tablist = []
	for i in range(botcount):
		driver.switch_to.new_window('tab')
		driver.get(url)
		driver.implicitly_wait(2)
		driver.find_element(By.XPATH, '//*[@id="inputName"]').clear()
		driver.find_element(By.XPATH, '//*[@id="inputName"]').send_keys(botName)
		time.sleep(0.2)
		tablist.append(driver.current_window_handle)
		print('1 Bot Ready to Join Game')
	choice =  input("Press Enter to Join ")
	for i in tablist:
		driver.switch_to.window(i)
		driver.implicitly_wait(0.2)
		driver.find_element(By.XPATH, '//*[@id="formLogin"]/button[1]').click()
		# //*[@id="divFullscreenLoading"]
		# Xpath for Adinplay Ads
		print('Sent 1 Bot to Join Game')

initfunc()
os.system('clear')
print('Bots Are In The Game!')
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
				else:
					wordlength = len(guessword)
			except Exception as e:
				pass

		print('Length of Word: ' + str(wordlength))

		f = open('wordlist.txt', 'r')

		for line in f:
			testword = line.strip('\n')
			if len(testword) == wordlength:
				possible.append(testword)

		if correctword != ' ':
			autoguess = False
			sendall(correctword)
			print('Word: ' + correctword)
			continue
		for word in possible:
			if count == botcount - 1:
				count = 0
			driver.switch_to.window(tablist[count])
			try:
				chatsend(word)
				time.sleep(0.15)
				lastchat = getlastchat()
				successmsg = botName + " guessed the word"
				if successmsg.lower() in lastchat.lower():
					print("Word Was Guessed")
					correctword = possible[totalcount]
					autoguess = False
					sendall(correctword)
					break
				else:
					print("Last Chat: " + lastchat)
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

	time.sleep(0.75)

	# print(f'Player Count: {playercountupdate()}')

driver.quit()
