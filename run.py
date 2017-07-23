#master function

import string, time, logging
import scriptures
from cfg import *
from biblegateway import biblegateway_api
from twitch import *

readBuffer = ""
s = openSocket()
logging.basicConfig(level=logging.DEBUG, filename='errorlog.txt')

def BibleBot():
    while True:
        readbuffer = readBuffer + s.recv(1024)
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
                if "!verse" in message: #looks for !verse command in twitch chat
                    scriptFind = message.split()
                    book, chapter, verse = scriptFind[1], scriptFind[2], scriptFind[3]
                    passage = scriptures.reference_to_string(bookname=book, chapter=chapter, verse=verse)
                    scripture = str(biblegateway_api.get_passage(passage, VERSION,))
                    sendMessage(s, passage + " (" + VERSION + "): "+ scripture)
                    time.sleep(CMDDELAY)
                elif "!votd" in message: #looks for votd command in twitch chat
                    votd = biblegateway_api.jsonText
                    votdRef = biblegateway_api.jsonRef
                    sendMessage(s, "Verse of the Day: " + votdRef + " (" + VERSION + "): "+ votd)
                    time.sleep(CMDDELAY)
                elif "!biblebot" in message:
                    sendMessage(s, HELP)
                else:
                    pass
            except Exception:
                logging.exception(time.localtime() + ': ')

def bibleOn():
    joinRoom(s)
    BibleBot()

if __name__ == "__main__":
    bibleOn()