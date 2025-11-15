#!/usr/bin/env python

import chess as c
import chess.pgn
import chess.polyglot

tsv = open("filtered.tsv")
reader = chess.polyglot.open_reader("/usr/share/scid/books/z3mod.bin")

for l in tsv.readlines():
	l = l.strip()
	x = l.split("\t")
	if x[3] == x[4]:
		continue
	b = c.Board(x[5])
	if b.fullmove_number > 2:
		continue
	book = list(reader.find_all(b))
	moves = [str(a.move) for a in book]
	if len(book) > 1:
		print(x[3], book)
		print(b.fen())
		print(30 * "-")
			
