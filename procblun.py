#!/usr/bin/env python

import chess as c
import chess.pgn
import chess.polyglot

tsv = open("filtered.tsv")
reader = chess.polyglot.open_reader("/usr/share/scid/books/z3mod.bin")
bfile = open("blunder.bin", "wb")

def get_zobrist_key_hex(board):
	return "%0.16x" % chess.polyglot.zobrist_hash(board)


allentries=[]

for l in tsv.readlines():
	l = l.strip()
	x = l.split("\t")
	if x[3] == x[4]:
		continue
	b = c.Board(x[5])
	book = list(reader.find_all(b))
	if len(book) == 0:
		#print(l)
		zobrist_key = get_zobrist_key_hex(b)
		zbytes = bytes.fromhex(zobrist_key)				
		m = chess.Move.from_uci(x[3])
		mi = m.to_square+(m.from_square << 6)					
		if not m.promotion == None:
			mi += ((m.promotion - 1) << 12)
		mbytes = bytes.fromhex("%0.4x" % mi)										
		wbytes = bytes.fromhex("%0.4x" % 1)					
		lbytes = bytes.fromhex("%0.8x" % 0)
		allbytes = zbytes + mbytes + wbytes + lbytes
		allentries.append(allbytes)
					
sorted_weights = sorted(allentries, key = lambda entry:entry[10:12], reverse = True)
sorted_entries = sorted(sorted_weights, key = lambda entry:entry[0:8])
print("%u moves added" % len(allentries))
for entry in sorted_entries:
	bfile.write(entry)

