#!/usr/bin/env python

import chess as c
import chess.pgn
import chess.polyglot

tsv = open("filtered.tsv")
reader = chess.polyglot.open_reader("/usr/share/scid/books/z3mod.bin")

pawns = .5

ignore = (
"rnbqkbnr/pppp1ppp/8/4p3/3P4/4P3/PPP2PPP/RNBQKBNR b KQkq - 0 2",
"r1bqkbnr/pp1ppppp/2n5/2p5/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3",
"rnb1kb1r/1pq2ppp/p2ppn2/6B1/3NPP2/2N2Q2/PPP3PP/R3KB1R b KQkq - 2 8",
"rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1",
"rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1",
"rnbqkb1r/pp2pppp/3p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R b KQkq - 2 5",
"rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1",
"rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
"rnbqkb1r/ppp2ppp/8/3pP3/4n3/2N2Q2/PPPP2PP/R1B1KBNR b KQkq - 1 5",
"r1bqkbnr/pp1p1ppp/2n1p3/2p5/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 b kq - 1 4",


)

for l in tsv.readlines():
	l = l.strip()
	x = l.split("\t")
	if x[3] == x[4]:
		continue
	if x[5] in ignore:
		continue
	b = c.Board(x[5])
	book = list(reader.find_all(b))
	moves = [str(a.move) for a in book]
	if len(book) > 0:
		if ( x[4] in moves and x[0] == "WB"
		  and abs(float(x[2])) < -pawns ):
			print(x[4], book)
			print(b.fen())
			print(30 * "-")
		if ( x[4] in moves and x[0] == "BB"
		  and abs(float(x[2])) > pawns ):
			print(x[4], book)
			print(b.fen())
			print(30 * "-")

