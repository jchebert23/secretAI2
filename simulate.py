import os
import subprocess
from engines import Engine
from copy import deepcopy
from board import Board
import argparse, copy, signal, sys, timeit, traceback
from board import Board, move_string, print_moves
import re


fullOut = ""
nGames = 100
for i in range(nGames):

    result = subprocess.run(["python3", "othello.py","-aB", "student", "random1"], stdout=subprocess.PIPE)
    print("Done ", i , " of ", nGames)
    if result:
        fullOut += result.stdout.decode("utf-8")

f = open("simulationOut.txt", "w")
f.write(fullOut)

allMatches = re.findall(r"\((.*)\) wins the game!", fullOut)
allNodesSeen = re.findall(r"Nodes Seen :  ([0-9]*)", fullOut)
parentNodesSeen = re.findall(r"Parent Seen :  ([0-9]*)", fullOut)
branchNodesSeen = re.findall(r"Branch Seen :  ([0-9]*)", fullOut)
duplicatedSeen = re.findall(r"Duplicated Seen :  ([0-9]*)", fullOut)
times = re.findall(r"Black: [0-9]* / ([0-9]*.[0-9]*)", fullOut)

me = 0
comp = 0

for winner in allMatches:
	if (winner == 'black'):
		me += 1
	else:
		comp += 1

total = 0
for n in allNodesSeen:
    total+= int(n)

print("\nAverage Nodes: ", total/nGames, "\n")

total = 0
for i in range(0, len(parentNodesSeen)):
    total += (int(branchNodesSeen[i])/int(parentNodesSeen[i]))

print("Branch Factor Average: ", total/nGames, "\n")

total = 0
for duplicate in duplicatedSeen:
    total += int(duplicate)

print("Average Duplicate Values: ", total/nGames, "\n")

total = 0
for time in times:
    total += float(time)

print("Average time: ", total/nGames,"\n")

print("Final Score:")
print("Me: " + str(me) + " vs. " + "Computer: " + str(comp))
print("Winning percentage:" + str(100 * (me/nGames)) + "%")
