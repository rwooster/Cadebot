# Contains source for all the functions that are called when Cade receives a PM
# Each function should take two arguments : a Cade object and a message object

import poll
from github import Github

def start_poll(cade, message):
    obj = poll.Poll(cade, message)

def request_feature(cade, message):
    import pdb; pdb.set_trace()
    repo = cade.github.get_repo("rwooster/Cadebot")
    repo.create_issue(title="FR: {0}".format(message.content))

