#!/usr/bin/python

import os
import sys
import discord

import daemon

class Cade(discord.Client):

    # Override the daemon classes run

    def __init__(self):
        super(Cade, self).__init__()

        # get account info
        self.email = os.environ['DISCORD_CADE_EMAIL']
        self.password = os.environ['DISCORD_CADE_PASSWORD']

        # login to discord
        self.login(self.email, self.password) 

        # start the bot
        self.run()
        
    def on_message(self, message):
        if message.content.startswith('!hello'):
            self.send_message(message.channel, 'Hello ' + message.author.name)
        if message.content.startswith('!source'):
            self.send_message(message.channel, "Edit me at https://github.com/rwooster/Cadebot !!!")

    def on_ready(self):
        print('Logged in as {0}'.format(self.user.name))

if __name__ == "__main__":
    cade = Cade()
