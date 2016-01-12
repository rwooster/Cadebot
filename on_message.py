# Contains source for all the functions that are called when Cade hears a message
# Each function should take two arguments : a Cade object and a message object

import random

def print_hello(cade, message):
    cade.send_message(message.channel, 'Hello ' + message.author.name)

def print_source(cade, message):
    cade.send_message(message.channel, "Edit me at https://github.com/rwooster/Cadebot !!!")

def roll_dice(cade, message):
    # of the form "!roll 1d6"
    words = message.content.split()
    roll = words[1].split('d') 

    random.seed()
    total = 0
    for i in range(int(roll[0])):
        total += random.randint(1, int(roll[1]))

    cade.send_message(message.channel, message.author.name + 
                      ' rolled {0}!'.format(total))
