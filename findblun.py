#!/usr/bin/env python

import chess as c
import chess.pgn
import chess.engine

ENGINE = "stockfish"
MTIME = 1
DEPTH = 21
THREADS = 12
MAXGAME = 1000
SKIP = 0

pgn = open('recent.pgn')

ofile = open("blunder.tsv", "w")

engine = chess.engine.SimpleEngine.popen_uci(ENGINE)
engine.configure({"Threads": THREADS})

gnum = 0

for qq in range(SKIP):
	print("*", end = "")
	chess.pgn.read_game(pgn)

while gnum < MAXGAME:
	gnum += 1
	print("+++ Game %u of %u" % (gnum, MAXGAME))
	game = chess.pgn.read_game(pgn)

	ml = list(game.mainline_moves())

	b = game.board()

	n = 1
	old = 0

	if b.fen() != c.STARTING_FEN:
		print("*** Not from startpos")
		continue

	if len(ml) < 10:
		print("*** Short game")
		continue

	if game.headers.get("Variant", ".") != "Standard":
		print("*** Wrong variant")
		continue

	if game.headers["White"] == "TuroBot":
		side = True
	else:
		side = False
	mm = []
	bm = []

	for m in ml:
		if n > 2 * DEPTH: break
		info = engine.analyse(b, chess.engine.Limit(time = MTIME))
		sc = info["score"].white().score(mate_score = 100000) / 100
		sm = info["pv"][0]
		print(sc, sm, str(m))
		mm.append((sc, str(sm), str(m)))
		bm.append(b.copy())
		b.push(m)
		n += 1


	if side:
		i = 2
	else:
		i = 1

	while i < len(mm) - 1:
		if side:
			d = mm[i+1][0] - mm[i][0]
			if d < -.5:
				ofile.write("WB\t%.2f\t%.2f\t%s\t%s\t%s\n" %
					(mm[i][0], d, mm[i][1], mm[i][2], bm[i].fen()))
				ofile.flush()
		else:
			d = mm[i+1][0] - mm[i][0]
			if d > .5:
				ofile.write("BB\t%.2f\t%.2f\t%s\t%s\t%s\n" %
					(mm[i][0], d, mm[i][1], mm[i][2], bm[i].fen()))
				ofile.flush()
		i += 2


#####

ofile.close()
engine.quit()

