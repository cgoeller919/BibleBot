#master function

import string, time
import scriptures
from cfg import VERSION, CMDDELAY
from biblegateway import biblegateway_api
from read import getUser, getMessage
from sock import openSocket, sendMessage
from initalize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        print(line)
        if "PING" in line: #looks for twitch's ping and sends response back
            s.send(line.replace("PING", "PONG"))
            break
        user = getUser(line)
        message = getMessage(line)
        print(user) + " typed: " + message
        try:
            if "!verse niggalations 4 20" in message:
                sendMessage(s, "Haha, Nice try.")
            elif "!verse" in message: #looks for !verse command in twitch chat
                scriptFind = message.split()
                book, chapter, verse = scriptFind[1], scriptFind[2], scriptFind[3]
                passage = scriptures.reference_to_string(bookname=book, chapter=chapter, verse=verse)
                scripture = str(biblegateway_api.get_passage(passage, VERSION,))
                sendMessage(s, passage + " (" + VERSION + "): "+ scripture)
                time.sleep(CMDDELAY)
            elif "!votd" in message: #looks for votd command in twitch chat
                votd = str(biblegateway_api.getVotd(VERSION))
                sendMessage(s, votd)
                time.sleep(CMDDELAY)
        except:
            sendMessage(s, "I'm sorry, " + user + ", the correct format is \"!verse book chapter versenum\"")
            pass