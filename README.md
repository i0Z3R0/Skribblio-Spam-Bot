# Skribblio-Spam-Bot

[Github](https://github.com/i0Z3R0/Skribblio-Spam-Bot)

[Replit](https://replit.com/@0Z3R0/Skribblio-Spam-Bot)

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [About](#about)
- [Overview of Features](#overview-of-features)
  * [Single Lobby Swarm](#single-lobby-swarm)
  * [Multi Lobby Single Spam](#multi-lobby-single-spam)
- [Detailed Overview](#detailed-overview)
  * [Single Lobby Swarm](#single-lobby-swarm-1)
    + [Overview](#overview)
    + [Detailed Breakdown](#detailed-breakdown)
    + [Customization Options](#customization-options)
  * [Multi Lobby Single Spam](#multi-lobby-single-spam-1)
    + [Overview](#overview-1)
    + [Detailed Breakdown](#detailed-breakdown-1)
    + [Customization Options](#customization-options-1)

# Prerequisites
- Latest version of Python3
- Latest version of Pip

# Installation
1. git clone https://github.com/i0Z3R0/Skribblio-Spam-Bot.git
2. cd Skribblio-Spam-Bot
3. pip3.9 install -r requirements.txt
4. python3.9 MultiLobbySingleSpam.py **or** python3.9 SingleLobbySwarm.py
#### Note: ChromeDriver is NOT required, webdriver_manager will automatically download the matching version of ChromeDriver for your OS. 

# About
This is a tool to spam skribbl.io lobbies, either private lobbies or random public lobbies. Inspired by [this](https://github.com/michaelshumshum/skribbl-io_spamBot) previous Python2 spambot made by another user. 

This spambot is written in Python3, and offers a lot of functions to make your spamming experience more enjoyable. Currently, there are two versions of spambots. More will be added in the (near) future. 

In a nutshell, the spambots use ChromeDriver and Selenium and multiple tabs to spam in lobbies. 

# Overview of Features
## Single Lobby Swarm
- Joins many bots in a single private lobby
- Autoguess the current word from a wordlist
- Send messages from all bots at once
- Click on thumbs up, thumbs down, or votekick with all bots
- Anti-spam detection
## Multi Lobby Single Spam
- Joins one bot in a random public lobby
- Spams in that lobby from a list of messages
- Anti-spam detection
- Will draw "flashes" when it's the bot's turn to draw (more on this later)
- Automatically leaves if there's too little players (customizable)
- Kick detection
- Status updates
- Can be ran for (theoretically) forever

# Detailed Overview

## Single Lobby Swarm
### **Overview**
This tool lets you join up to 6 bots in a single private lobby. Skribblio will put you in a different lobby if there are over 6 connections to the same private lobby from 1 IP. Although this can by bypassed with proxies, rarely would you need more than 6 users in a single lobby. This should be used if you want to quickly ruin a single lobby's entire experience, as it try to guess the word and make the game unenjoyable for everyone. Mass reactions (thumbs up and down) will also make people mad. This tool does not have kick detection or automatic rejoining, it's more of a flood tool than a persistent tool (I personally haven't used this for more than 2 minutes at a time, people tend to recreate private lobbies after that). 
### **Detailed Breakdown**
This tool will join as many bots as you want into a single private game (the limit is 6 based on IP). If any bot is stuck on an ad, it will simply close the tab with that bot. Therefore, botCount should be set to one higher than the actual amount of bots you want to join. This tool will let you send messages as all the bots at once in the chat. 

Using regular expression and the current length of the word and hints, it will compile a list of all the possible words. Then, it will cycle through each tab containing the bots and send each possible messsage. The bots will also check the latest message to see if the word was guessed correctly. It will then send that in all tabs, thus allowing the bots to all guess the word correct. However, if autoguessing is used on words with too much possible options (4, 5, 6 letter), it will take too long autoguessing this isn't pauseable after started. If it is one of the bots' turn to draw, it will select the first word, get the word, and all the bots will send "The word is: word" and then send the word to quickly guess the word correctly. 

!ag or !autoguess, !c or !clear, !tu or !thumbsup, !td or !thumbsdown, and !vk or !votekick are all "commands" that you can enter when prompted to enter a message to send. They will do special actions, such as autoguess the current word, clear the terminal, or click on icons in the game. Additionally, !leave will have all the bots leave the game and the script will end. 
### **Customization Options**
- **URL** (Line 13): This is the url to a private lobby. Should be in the format https://skribbl.io/?XXXXXX
- **Headless Mode** (Line 14): This determines whether ChromeDriver runs in headless mode or not. Headless mode is highly highly recommended, it makes everything much faster, but you are unable to actually see the Chrome tabs. Therefore, you should join the lobby yourself (and set botCount to 6)
- **Bot Count** (Line 15): This sets the number of bots that will join the game. However, you must set the botCount to be 1 more than however many you want. This is because the second bot will (99% of the time) get stuck on an ad, and waiting for the ad to complete will take too long. If you want 5 bots to join, put 6. 
- **Bot Name** (Line 16): This sets the name that the bots will have when they join. Each individual bot will have a number (from 1 through botCount) appended. 
###### Note: Don't change other variables unless you know what you are doing. 

## Multi Lobby Single Spam
### **Overview**
This tool joins a single bot in random public lobbies. This should be used if you want to take a backseat and just watch chaos unfold. No action is necessary after the bot is started (do report errors and crashes by opening an [Issue](https://github.com/i0Z3R0/Skribblio-Spam-Bot/issues/new)). This bot consistently spams from a set of messages (customizable) and will flash colors while drawing. When kicked or disconnected, it will reload the page and join another lobby, letter this script run for, theoretically, all eternity. 
### **Detailed Breakdown**
The bot will go to https://skribbl.io/ and join a random public lobby. It will then loop through an array of predetermined messages to spam, and send them one by one. Every 10 messages, it will check if it's the bot's turn to draw. Every 20, it will check if the bot is kicked, and will rejoin a lobby if it is. Every 30, it will check if the player count is under a predetermined threshold, and join another lobby if applicable. 

When the bot detects it's its (lol) turn to draw, it will be as annoying as possible. After the bot detects the draw popup, it will first spew out a set of "legal messages" in the chat: 

*botName may not be held liable for any damage caused or sustained by the following actions, including any damage caused to third parties as a consequence of or during the implementation of the action. 
Photosensitivity warning!*

Then, the bot will proceed to (by default)\* paint the entire canvas black, then white, then black, then white, and repeat that until kicked or the draw turn is over. If the bot is kicked or disconnected at any time, it will reload the page and join another random public lobby, print out the current status, and it can run forever. The drawing portion of the bot is not super optimized because by the time the bot draws, everybody will likely have already votekicked it. 

If the bot detects it has been kicked or disconnected from a lobby, it will reload the page and attempt to join a new one. Then, it will print out the current status, including the number of lobbies spammed in, number of messages spammed, 
###### * All the X-Paths of all the possible color and drawing tool elements are located at the top of the code. This allows for some creativity in custom color flashing and annoyances. If you would like me to program you a specific sequence of flashing colors, open an [Issue](https://github.com/i0Z3R0/Skribblio-Spam-Bot/issues/new). 
### **Customization Options**
- **Headless Mode** - Boolean (Line 13): This determines whether ChromeDriver runs in headless mode or not. For this variation of spambot, headless mode makes everything only slightly faster, but you are unable to actually see the Chrome tab in action. Keep headless mode off if you want to see the spambot drawing, spamming, or just the reactions of others. Turn it on if you want to just have it run in the background when you're AFK or working on other things. 
- **playerMinThreshold** - Integer (Line 14): This determines the minimum number of players in a lobby for the spambot to stay and continue spamming. This number includes yourself, so if you set it to 5, it will only stay of 4 other players are in the game. 
- **Bot Name** - String (Line 15): This determines the name of the bot. Skribblio does have a 12 character name limit, and anything over that will be cut automatically. 
- **Obnoxious** - Boolean (Line 16): This determines if the bot should be extra annoying, and will send messages in the chat when it's checking for the draw popup, player count, or if the bot is kicked. 
- **Messages** - List (Line 17): This determines what the bot will spam in the game. Skribblio has a 100 character limit for messages. If you don't know how to create or format a list, go [here](https://arraythis.com/), enter your messages seperated by a new line on the left, click convert, and copy the second box on the right. 
###### Note: Don't change other variables unless you know what you are doing. 
