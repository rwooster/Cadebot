#!/usr/bin/python

import os
import sys
import random
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
        elif message.content.startswith('!source'):
            self.send_message(message.channel, "Edit me at https://github.com/rwooster/Cadebot !!!")
        elif message.content.startswith('!roll'):
            self.send_message(message.channel, message.author.name + ' rolled {0}!'.format(roll_dice(message.content)))

    def on_ready(self):
        print('Logged in as {0}'.format(self.user.name))

def roll_dice(message):
    # of the form "!roll 1d6"
    words = message.split()
    roll = words[1].split('d') 

    random.seed()
    total = 0
    for i in range(int(roll[0])):
        total += random.randint(1, int(roll[1]))

    return total

        



if __name__ == "__main__":
    cade = Cade()
