#initalization for twitch

import string
from sock import sendMessage

def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMessage(s, "Hi, I'm Bible_Bot! Use !verse [book] [chapter] [verse] to print a verse to the chat!")

def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True