# Contains code implementing a generic discord bot

import os
import discord
from github import Github

import channel 
import config
import private_message 

class Bot(discord.Client):

    # Functions that can be executed in a channel
    channel_mapping = {
            "choose"  : channel.random_choice,
            "contest" : channel.roll_contest,
            "endpoll" : channel.endpoll,
            "hello"   : channel.print_hello,
            "roll"    : channel.roll_dice,
            "source"  : channel.print_source,
            "vote"    : channel.vote,
    }

    # Functions that are executed over PM
    private_mapping = {
            "feature" : private_message.request_feature,
            "poll"    : private_message.start_poll,
    }

    def __init__(self, config_file):
        super(Bot, self).__init__()

        # Member variable inits
        self.__expect_message = None
        self.__expect_callback = None

        # Map Channel : Poll to ensure only 1 poll per channel at a time
        self.polls = {}

        # Open config file
        self.config = config.Config(config_file)

        # Connect to github
        self.github = Github(self.config['GITHUB_EMAIL'], self.config['GITHUB_PASSWORD'])

        # login to discord
        self.login(self.config['DISCORD_CADE_EMAIL'], self.config['DISCORD_CADE_PASSWORD'])

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

    # Tells bot to expect a PM from user
    # upon recieving the message, calls func passing the message as an argument, 
    # along with any other args provided
    def expect_message(self, user, func, *args):
        self.__expect_message = user
        self.__expect_callback = func
        self.__expect_args = args

