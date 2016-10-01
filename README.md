# Cadebot
Chatbot for Discord 

![alt tag](http://www.videogamesblogger.com/wp-content/uploads/2010/07/marcus-cade-starcraft-2-character-screenshot.jpg)

This is based on the unofficial discord API (the python port of which can be found at https://github.com/Rapptz/discord.py).

## Quick Start

First, need to have python installed. This runs on Python 2.7 (you may need to edit the shebang at the top of cade.py to reflect your installed location) on Linux (As of 1/12 it worked on OSX also).

Need the following dependencies (pip install):

	- discord.py
	- PyGithub

You need to have a config file filled out as per the sample.config given (currently renamed cade.config)

Once all of this is setup, you should be able to run ./cade.py and the bot will be running. As of now, the bot has to be added to each of the servers you want by logging into the bot account and adding it manually.

NOTE: No longer works due to breaking changes in discord.py
