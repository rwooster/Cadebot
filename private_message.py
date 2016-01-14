# Contains source for all the functions that are called when Cade receives a PM
# Each function should take two arguments : a Cade object and a message object

import threading
import re


class Poll(object):

    def __init__(self, cade, message):
        # init variables
        self.available_servers = []
        self.chosen_server = None
        self.available_channels = []
        self.channel = None
        self.question = None
        self.choices = []
        self.responses = []
        self.poll_author = None

        self.start_poll(cade, message)

    def start_poll(self, cade, message):
        
        # Find all servers that the sender and Cade have in common
        self.available_servers = filter(lambda s: message.author in s.members, cade.servers)
        self.poll_author = message.author
        
        cade.send_message(message.channel,
                "What server do you want this poll to be on? Options are: ")

        for counter, server in enumerate(self.available_servers):
            cade.send_message(message.channel,
                              "{0}) {1}".format(counter, server.name))
            
        cade.expect_message(message.author, self.choose_server, cade)

    def choose_server(self, message, cade):
        self.chosen_server = self.available_servers[int(message.content)]

        self.available_channels = filter(lambda c: c.type == "text", self.chosen_server.channels)
        cade.send_message(message.channel,
                "What channel do you want this poll to be on? Options are: ")

        for counter, channel in enumerate(self.available_channels):
            cade.send_message(message.channel,
                              "{0}) {1}".format(counter, channel.name))

        cade.expect_message(message.author, self.choose_channel, cade)

    def choose_channel(self, message, cade):
        self.channel = self.available_channels[int(message.content)]

        cade.send_message(message.channel,
                          "What is the poll question?")

        cade.expect_message(message.author, self.set_question, cade)

    def set_question(self, message, cade):
        self.question = message.content

        cade.send_message(message.channel, 
                "What are the choices? Write your choices all in one message, with each choice in double quotes.")

        cade.expect_message(message.author, self.set_choices, cade)

    def set_choices(self, message, cade):
        # Choices in the form "choice 1" "choice 2" ...

        # regex (?<=")[^"]*(?=") will match everything inbetween double quotes
        # (including the spaces). need to strip the spaces unless I come up with 
        # better regex
        regex = '(?<=")[^"]*(?=")'

        self.choices = filter(lambda c: c and not c.isspace(), re.findall(regex, message.content))

        cade.send_message(message.channel, "Ok, starting poll")

        cade.send_message(self.channel, "{0} has started a poll!".format(self.poll_author))
        cade.send_message(self.channel, "**" + self.question + "**")

        for counter, choice in enumerate(self.choices):
            cade.send_message(self.channel, "{0}) {1}".format(counter, choice))

