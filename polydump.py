#!/usr/bin/env python

import sys, chess
import chess.polyglot

fen = "r2q1rk1/pp3pbp/2pp1np1/4n3/P1PQ4/2N2BP1/1P2PP1P/R1B1K2R w KQ - 1 13"
fen = "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 5" # O-O

board = chess.Board(fen)

f = "blunder1.bin"
f = "merged.bin"

with chess.polyglot.open_reader(f) as reader:
    for entry in reader.find_all(board):
        print(entry.move, entry.weight, entry.learn)


