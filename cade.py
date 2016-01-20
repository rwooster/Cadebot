#!/usr/bin/python

# Contains the instantiation of Cade

import sys

import bot

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: ./cade config_file"
        exit(-1)
    else:
        cade = bot.Bot(sys.argv[1])
    



