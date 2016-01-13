# Contains source for all the functions that are called when Cade receives a PM
# Each function should take two arguments : a Cade object and a message object

import threading
import re

def start_poll(cade, message):
    # Poll is of format "Question" "Option 1" "Option 2" ...

    # regex (?<=")[^"]*(?=") will match everything inbetween double quotes
    # (including the spaces). need to strip the spaces unless i come up with 
    # better regex
    regex = '(?<=")[^"]*(?=")'

    content = filter(lambda c: c != " ", re.findall(regex, message.content))
    question = content[0]
    answers = content[1:]


