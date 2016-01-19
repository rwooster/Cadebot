# Contains code that implements running a poll

import re

class Poll(object):

    def __init__(self, cade, message):
        # init variables
        self.available_servers = []
        self.server = None
        self.available_channels = []
        self.channel = None
        self.question = None
        self.choices = []
        self.responses = []
        self.responders = []
        self.poll_author = None
        self.client = cade

        self.ask_server(message)

    def ask_server(self, message):
        
        # Find all servers that the sender and Cade have in common
        self.available_servers = filter(lambda s: message.author in s.members, self.client.servers)
        self.poll_author = message.author
        
        self.client.send_message(message.channel,
                "What server do you want this poll to be on? Options are: ")

        for counter, server in enumerate(self.available_servers):
            self.client.send_message(message.channel,
                              "{0}) {1}".format(counter, server.name))
            
        self.client.expect_message(message.author, self.choose_server)

    def choose_server(self, message):
        self.server = self.available_servers[int(message.content)]

        self.available_channels = filter(lambda c: c.type == "text", self.server.channels)
        self.client.send_message(message.channel,
                "What channel do you want this poll to be on? Options are: ")

        for counter, channel in enumerate(self.available_channels):
            self.client.send_message(message.channel,
                              "{0}) {1}".format(counter, channel.name))

        self.client.expect_message(message.author, self.choose_channel)

    def choose_channel(self, message):
        self.channel = self.available_channels[int(message.content)]
        
        if (self.channel in self.client.polls):
            self.client.send_message(message.channel, 
                                     "Sorry, a poll is already in progress in this channel")
            return 


        self.client.send_message(message.channel,
                          "What is the poll question?")

        self.client.expect_message(message.author, self.set_question)

    def set_question(self, message):
        self.question = message.content

        self.client.send_message(message.channel, 
                "What are the choices? Write your choices all in one message, with each choice in double quotes.\
 The first listed choices will have priority in ties.")

        self.client.expect_message(message.author, self.set_choices)

    def set_choices(self, message):
        # Choices in the form "choice 1" "choice 2" ...

        # regex (?<=")[^"]*(?=") will match everything inbetween double quotes
        # (including the spaces). need to strip the spaces unless I come up with 
        # better regex
        regex = '(?<=")[^"]*(?=")'

        self.choices = filter(lambda c: c and not c.isspace(), re.findall(regex, message.content))

        self.client.send_message(message.channel, "Ok, starting poll")
        self.start_poll()

    def start_poll(self):
        # Mark a poll on this channel in the client
        self.client.polls[self.channel] = self

        self.client.send_message(self.channel, "{0} has started a poll!".format(self.poll_author))
        self.client.send_message(self.channel, "Vote with: !vote vote1, vote2, vote3")
        self.client.send_message(self.channel, "Remember, you can only vote once!")
        self.client.send_message(self.channel, "**" + self.question + "**")

        for counter, choice in enumerate(self.choices):
            self.client.send_message(self.channel, "{0}) {1}".format(counter, choice))

    def announce_winner(self, author):
        if self.poll_author != author:
            return

        if len(self.responses) < 0:
            self.client.send_message("** No winner **")
        else:
            for count, choice in enumerate(self.choices):
                self.client.send_message(self.channel, "{0} votes for {1}!".format(self.responses.count(count), choice))

            winner = max(set(self.responses), key=self.responses.count)
            self.client.send_message(self.channel, 
                                     "The winning choice is:** {0}! **".format(self.choices[int(winner)]))


        del self.client.polls[self.channel]

    def vote(self, message):
        if message.author not in self.responders:
            answers = [int(x.strip()) for x in message.content.split(',')] 
            answers_valid = [x for x in answers if x < len(self.choices)]
            answers_no_dup = set(answers_valid)

            self.responses.extend(answers_no_dup)
            self.responders.append(message.author)


