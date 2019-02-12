Clayton Hebert
February 11th, 2019


PART III and IV Description
For this assignment, I found a heuristic function from Vaishnavi Sannidhanam and Muthukaruppan Annamalai from the University of Washington.
https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf

This paper brings up 4 factors for the heuristic function: coin parity, mobility, stability, and corners. Coin parity is simply a measure between the number of my disks versus my opponents. Mobility 
is the measure of given the current state, how many moves I have and how many potential moves my opponent has. Corners simply count how many corners I have compared to my opponent. This is such an important factor because corner pieces are unable to be flipped, and building out from corner creates more unflippable disks. Stability is a measure of how many coins disks on the board are unable to be flipped in the future. I calculated this by summing the chains of same color disks around the edges of the board that start at the corners. The paper also gave relative weights for these four factors in the heuristic (coin parity: 25, mobility: 5, stability: 25, corners: 30). The paper also mentionsa different heuristic function which solely looks at the value of getting one's piece on each square on the board. I combined these two heuristics by looking at the 12 strategically worst squares on the board (locations listed at the top of my student.py). I decided to substract 50% from the current value of the heuristic if the current move sequence involved putting one of my pieces on one of these squares. 


PART VI

Below I have listed the results of the experiments I conducted for PART VI of this assignment. I calculated Nodes Seen, Branching Factor, Duplicates Seen, and Runtime for the function that searches using Alpha-Beta Pruning and the one that does not (no AB stands for not using Alpha Beta Pruning, and AB stands for using Alpha Beta Pruning). I ran these results for both functions at tree depths of 1,2, and 3. For depths 1,2 I ran 100 iterations of the game and calculated the average values. For depth 3 for each, I ran 50 iterations just for time's sake. 

To calculate these four results, I had several class variables for my student.py. For context, I used a recursive function to loop through all the different nodes in the tree. To calculate nodes seen, I had a variable called nodesSeen, that I incremented each time I recalled my recursive function (Note: I include in my number the fringe nodes that I do not expand, but rather calculate the heuristic on). To calculate the branch factor, I incremented a variable called parentNodes every time I reached a parent, and for each of its kids I incremented a variable called branch Nodes. To get the branching factor, I divided the parentNodes by the number of branchNodes. To calculate the number of duplicates, for each board state I converted it to a string representation and added it into a dictionary. Then for each new node, I check if it was already seen by checking its existence in the dictionary.

Notable Results From the Data Below:

For each increase in the depth, the nodes seen increases by nearly a factor of 10 for the nonAB function and nearly a factor of 8 for the AB function. This makes sense because increasing the depth in a tree increases the number of nodes exponentially. The runtime too appears to increase by a factor of 10 and 8 (2.4-> 20.4, 1.2-> 8.586) which again makes sense since we are going through so many more nodes as we increase the depth. For depths 2 and 3, we also see that the branching factor is significantly lower for the AB function as opposed to the non AB function (8.38 vs 4.77 and 9.429 vs 6.139). This makes sense because the alpha beta pruning is able to get rid of nodes we know the minimax algorithm will not choose before looking at them.




#---------------------------------#
Depth 1, no AB
Average Nodes:  284.31 

Branch Factor Average:  8.649998701599658 

Average Duplicate Values:  1.32 

Average time:  ~0 (Program did not calculate any loss in time)

#---------------------------------#

#---------------------------------#
Depth 2, no AB
Average Nodes:  2446.67 

Branch Factor Average:  8.381914440719324 

Average Duplicate Values:  747.05 

Average time: 30- 27.567999999999998= 2.433 

#---------------------------------#
Depth 3, no AB

Average Nodes:  24686.7 

Branch Factor Average:  9.429777582866297 

Average Duplicate Values:  23157.6 

Average time: 30- 9.589999999999996 = 20.4101

#---------------------------------#

#---------------------------------#
Depth 1, AB
Average Nodes:  288.98 

Branch Factor Average:  8.816396417689042 

Average Duplicate Values:  1.0 

Average time:  ~0 (Program did not calculate any loss in time)
#---------------------------------#
#---------------------------------#
Depth 2, AB
Average Nodes:  1426.56 

Branch Factor Average:  4.770876906285923 

Average Duplicate Values:  285.72 

Average time:  30-28.70399999999999 = 1.2961
#---------------------------------#

#---------------------------------#

Depth 3, AB
Average Nodes:  8363.2 

Branch Factor Average:  6.135030127355221 

Average Duplicate Values:  6755.1 

Average time:  30-21.41499999999998 = 8.586 

#---------------------------------#
