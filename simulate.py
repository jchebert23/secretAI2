import os
import subprocess
from engines import Engine
from copy import deepcopy
from board import Board
import argparse, copy, signal, sys, timeit, traceback
from board import Board, move_string, print_moves
import re


fullOut = ""
nGames = 30
for i in range(nGames):
    #    result = subprocess.run(["python3", "othello.py", "student", "random1"], capture_output=True, text=True)
    result = subprocess.run(["python3", "othello.py", "student", "random1"], stdout=subprocess.PIPE)
    if result:
        fullOut += result.stdout.decode("utf-8")

f = open("simulationOut.txt", "w")
f.write(fullOut)

allMatches = re.findall(r"\((.*)\) wins the game!", fullOut)

me = 0
comp = 0
for winner in allMatches:
	if (winner == 'black'):
		me += 1
	else:
		comp += 1

print("Final Score:")
print("Me: " + str(me) + " vs. " + "Computer: " + str(comp))
print("Winning percentage:" + str(100 * (me/nGames)) + "%")
