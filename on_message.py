# Contains source for all the functions that are called when Cade hears a message
# Each function should take two arguments : a Cade object and a message object

import util

def print_hello(cade, message):
    cade.send_message(message.channel, 'Hello ' + message.author.name)

def print_source(cade, message):
    cade.send_message(message.channel, "Edit me at https://github.com/rwooster/Cadebot !!!")

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

    winner = max(rolls, key=lambda x: x[1])
    cade.send_message(message.channel, 
                      "The winner is " + winner[0].name + "!")
        
