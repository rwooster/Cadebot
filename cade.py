#!/usr/bin/python

# Contains the Cade Client
# On run starts Cade, connecting him to discord

import os
import discord

import channel as ch
import private_message as pm

class Cade(discord.Client):

    # Functions that can be executed in a channel
    channel_mapping = {
            "hello"   : ch.print_hello,
            "source"  : ch.print_source,
            "roll"    : ch.roll_dice,
            "contest" : ch.roll_contest,
            "choose"  : ch.random_choice,
    }

    # Functions that are executed over PM
    private_mapping = {
            "poll" : pm.start_poll,
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
            split = message.content.split(" ", 1)
            message.content = split[1] if len(split) > 1 else message.content

            # Check for PM
            if message.server is None:
                self.private_mapping[split[0][1:]](self, message)
            else:
                self.channel_mapping[split[0][1:]](self, message)

    def on_ready(self):
        print('Logged in as {0}'.format(self.user.name))


if __name__ == "__main__":
    cade = Cade()
