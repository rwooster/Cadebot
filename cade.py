#!/usr/bin/python

# Contains the Cade Client
# On run starts Cade, connecting him to discord

import os
import discord
from github import Github

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
            "vote"    : ch.vote,
            "endpoll" : ch.endpoll
    }

    # Functions that are executed over PM
    private_mapping = {
            "poll" : pm.start_poll,
            "feature" : pm.request_feature
    }

    def __init__(self):
        super(Cade, self).__init__()

        # Member variable inits
        self.__expect_message = None
        self.__expect_callback = None

        # Map Channel : Poll to ensure only 1 poll per channel at a time
        self.polls = {}

        # Connect to github
        self.github = Github(os.environ['GITHUB_EMAIL'], os.environ['GITHUB_PASSWORD'])

        # get account info
        self.email = os.environ['DISCORD_CADE_EMAIL']
        self.password = os.environ['DISCORD_CADE_PASSWORD']

        # login to discord
        self.login(self.email, self.password) 

        # start the bot
        self.run()
        
    def on_message(self, message):
        # First, if expecting a PM, handle it
        if self.__expect_message == message.author and message.server is None:
            self.__expect_message = None
            self.__expect_callback(message, *self.__expect_args)
            return

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

    # Tells cade to expect a PM from user
    # upon recieving the message, calls func passing the message as an argument, 
    # along with any other args provided
    def expect_message(self, user, func, *args):
        self.__expect_message = user
        self.__expect_callback = func
        self.__expect_args = args



if __name__ == "__main__":
    cade = Cade()
