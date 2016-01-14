# Contains source for all the functions that are called when Cade receives a PM
# Each function should take two arguments : a Cade object and a message object

import poll

def start_poll(cade, message):
    obj = poll.Poll(cade, message)
