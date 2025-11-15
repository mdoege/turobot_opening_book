#!/usr/bin/env python3

# Find quick bot losses

# p shortloss.py > recent.pgn

#MINLEN, MAXLEN = 10, 30
MINLEN, MAXLEN = 10, 50
MAXGAMES = 500

import chess.pgn

ng = 0
pgn = open('recent_all.pgn')

while True:
    game = chess.pgn.read_game(pgn)
    if game == None: break
    #if (game.headers.get("BlackTitle", "") == "BOT" 
    #  and game.headers.get("WhiteTitle", "") == "BOT"):
    #    continue
    board = game.board()
    nn = 0
    for m in game.mainline_moves():
        board.push(m)
        nn += 1
    if nn > 2 * MAXLEN or nn < 2 * MINLEN:
        continue
    wn, bn = game.headers["White"], game.headers["Black"]
    r = "????"
    if wn == "TuroBot":
        un = bn
        if game.headers["Result"] == "1-0":
            r = 1
        if game.headers["Result"] == "0-1":
            r = 0
    else:
        un = wn
        if game.headers["Result"] == "0-1":
            r = 1
        if game.headers["Result"] == "1-0":
            r = 0
    if r == 0 or r == "????":
        print(game, end="\n\n")
        ng += 1
        if ng == MAXGAMES:
            break
            
