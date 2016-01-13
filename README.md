# Cadebot
Chatbot for Discord 

![alt tag](http://www.videogamesblogger.com/wp-content/uploads/2010/07/marcus-cade-starcraft-2-character-screenshot.jpg)

This is based on the unofficial discord API (the python port of which can be found at https://github.com/Rapptz/discord.py).

## Quick Start

First, need to have python installed. This runs on Python 2.7 (you may need to edit the shebang at the top of cade.py to reflect your installed location) on Linux (As of 1/12 it worked on OSX also).

Next, need to have discord.py and dependencies installed. If you use pip, pip install discord.py will take care of everything. 

You need to have two environmental variables set: DISCORD_CADE_EMAIL, which has the email of the discord account the bot will use and DISCORD_CADE_PASSWORD which has the account's password. 

Once all of this is setup, you should be able to run ./cade.py and the bot will be running. As of now, the bot has to be added to each of the servers you want by logging into the bot account and adding it manually.
