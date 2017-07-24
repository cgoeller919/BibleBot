#interactions with twitch

import string
import socket
from cfg import *

CHANNEL = ""
def ChannelSet(CHANNEL):
    CHANNEL = CHANNEL

def openSocket(): #open socket to twitch
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + IDENT + "\r\n")
    s.send("JOIN #" + CHANNEL + "\r\n")
    return s


def joinRoom(s): #join twitch channel
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

def loadingComplete(line): #confirms loading into twitch chat
    if("End of /NAMES list" in line):
        return False
    else:
        return True

def getUser(line): #gets username from each chat message
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user

def getMessage(line): #gets message from chat
    separate = line.split(":", 2)
    message = separate[2]
    return message

def sendMessage(s, message): #sends message to twitch chat
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(messageTemp + "\r\n")
    print("Sent: " + messageTemp)