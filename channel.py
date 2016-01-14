# Contains source for all the functions that are called when Cade hears a message in a channel
# Each function should take two arguments : a Cade object and a message object

import random
import time

import util

def print_hello(cade, message):
    cade.send_message(message.channel, 'Hello ' + message.author.name)

def print_source(cade, message):
    cade.send_message(message.channel, 
                      "Edit me at https://github.com/rwooster/Cadebot !!!")

def roll_dice(cade, message):
    # of the form "1d6"
    dice = message.content

    cade.send_message(message.channel, 
                      message.author.name + 
                      ' rolled {0}!'.format(util.roll_dice(dice)))

def roll_contest(cade, message):
    # of the form "1d6"
    dice = message.content

    cade.send_message(message.channel, 
                      message.author.name + " started a contest of " + dice)

    rolls = []
    for user in message.server.members:
        if user.id == cade.user.id:
            continue
        roll = util.roll_dice(dice)
        rolls.append((user, roll))
        cade.send_message(message.channel, user.name + " rolled a " + str(roll))
        time.sleep(1)

    winner = max(rolls, key=lambda x: x[1])
    cade.send_message(message.channel, 
                      "The winner is " + winner[0].name + "!")

def random_choice(cade, message):
    choices = message.content.split(" ")

    cade.send_typing(message.channel)
    time.sleep(2)
    cade.send_message(message.channel,
                      "I pick " + random.choice(choices) + "!")

def vote(cade, message):
    if message.channel in cade.polls: 
        poll = cade.polls[message.channel]

        if message.content.isdigit() and int(message.content) < len(poll.choices):
            poll.responses.append(message.content)

def endpoll(cade, message):
    if message.channel in cade.polls:
        poll = cade.polls[message.channel]
        poll.announce_winner()
