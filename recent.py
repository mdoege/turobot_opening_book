#!/usr/bin/python

import os, time, json
from urllib.request import urlopen

# update this to total number of games played after running recent.py:
oldnum = 22213

#days = 1
#t = 1000 * (time.time() - days * 24 * 60 * 60)
#r = "https://lichess.org/api/games/user/TuroBot?since=%u" % t

a = urlopen("https://lichess.org/api/user/TuroBot").read()
j = json.loads(a)
curnum = j["count"]["all"]
n = curnum - oldnum
r = "https://lichess.org/api/games/user/TuroBot?max=%u" % n
c = 'curl -o recent_all.pgn "%s"' % r
#c = 'curl -o recent.pgn "%s"' % r
os.system(c)
print("Fetched %u games" % n)

