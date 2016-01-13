#!/usr/bin/python

# Contains the Cade Client
# On run, starts Cade connecting him to discord

import os
import discord

import on_message as om

class Cade(discord.Client):

    function_mapping = {
            "hello"   : om.print_hello,
            "source"  : om.print_source,
            "roll"    : om.roll_dice,
            "contest" : om.roll_contest,
    }

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
        if message.content.startswith('!'):
            command, rest = message.content.split(" ", 1)
            message.content = rest 
            self.function_mapping[command[1:]](self, message)

    def on_ready(self):
        print('Logged in as {0}'.format(self.user.name))


if __name__ == "__main__":
    cade = Cade()
