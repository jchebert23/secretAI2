from engines import Engine
from copy import deepcopy

class StudentEngine(Engine):
    """ Game engine that you should you as skeleton code for your 
    implementation. """

    alpha_beta = False
    
    depthLimit = 2
    badSquares = [[0,1], [1,0], [6,0], [7,1], [7,6], [6,7], [0,6],[1,7],[1,1],[6,6],[1,6],[6,1]]
    

    maxAB = float("+inf")
    minAB = float("-inf")
    
    def coinParity(self, board, color):
        num_pieces_op = len(board.get_squares(color*-1))
        num_pieces_me = len(board.get_squares(color))
        output = (100*(num_pieces_me - num_pieces_op))/ (num_pieces_me + num_pieces_op)
        return output
    
    def mobility(self, board, color, myMoves, oppMoves):
    #could speed it up by remembering number of legal moves
        myMoves = len(myMoves)
        oppMoves = len(oppMoves)
        if(myMoves != 0 or oppMoves != 0):
            output = (100 * (myMoves - oppMoves)) / (myMoves + oppMoves)
        else:
            output = 0
        return output
    
    def cornersCaptured(self, board, color):
        myCol = 0
        oppCol = 0
        for coordinate in [[0,0], [0,7],[7,7], [7,0]]:
            x = coordinate[0]
            y = coordinate[1]
            if(board[x][y]==color):
                myCol += 1
            elif(board[x][y]==(color*-1)):
                oppCol +=1
        if(myCol != 0 or oppCol != 0):
            output = (100 * (myCol - oppCol)) / (myCol + oppCol)
        else:
            output = 0
        return output
    
    def stability(self, board, color):
        myVal = 0
        oppVal = 0
        i =0
        corners = [[0,0],[0,7],[7,7],[7,0]]
        for corner in corners:
            if(i<2):
                increment = 1
            else:
                increment = -1
            xCorn = corner[0]
            yCorn = corner[1]
            curColor = board[xCorn][yCorn]
            stableChain = 0
            stableCorner = 0
            tentChain = 0
            if(curColor != 0):
                stableCorner = 1
            for w in range(7):
                if(board[xCorn][yCorn] == curColor and curColor != 0):
                    if(stableCorner):
                        stableChain += 1
                    else:
                        tentChain += 1
                else:
                    stableCorner = 0
                    if(stableChain != 0):
                        if(curColor == color):
                            myVal += stableChain
                        else:
                            oppVal += stableChain
                    stableChain = 0
                    curColor = board[xCorn][yCorn]
                    if(curColor!= 0):
                        tentChain = 1
                if(i % 2 == 0):
                    yCorn += increment
                else:
                    xCorn += increment
            if(i < 3):
                newX = corners[i+1][0]
                newY = corners[i+1][1]
            else:
                newX = 0
                newY = 0
            if(tentChain != 0 and board[newX][newY] == curColor):
                if(curColor == color):
                    myVal += tentChain
                else:
                    oppVal += tentChain

            if(stableChain != 0 and board[newX][newY] == curColor):
                if(curColor == color):
                    myVal += stableChain
                else:
                    oppVal += stableChain
            i += 1
        if(myVal !=0 or oppVal != 0):
            return (100*(myVal-oppVal))/(myVal+oppVal)
        else:
            return 0

            
    def heuristicFunction(self, board, color, moves, oppMoves, flag):
        weight = 0
        weight += 25*self.coinParity(board, color)
        weight += 5*self.mobility(board, color, moves, oppMoves)
        weight += 30*self.cornersCaptured(board, color)
        weight += 25*self.stability(board, color)
        if(flag):
            weight = weight - abs(weight * .5)
        return weight
    
    def get_minimax_helper(self, board, color, depth, originalColor, flag):
        if depth==self.depthLimit:
            moves = board.get_legal_moves(originalColor)
            oppMoves = board.get_legal_moves(originalColor * -1)
            heuristicVal = self.heuristicFunction(board, originalColor, moves, oppMoves, flag)
            return heuristicVal
        else:
            moves = board.get_legal_moves(color)
            weights = []
            for move in moves:
                newboard = deepcopy(board)
                newboard.execute_move(move, color)
                if((move in self.badSquares) and color == originalColor):
                    flag = 1
                weight = self.get_minimax_helper(newboard, color*-1, depth+1, originalColor, flag)
                weights.append(weight)
            #means no moves, so this node can act as fringe node
            if(len(moves) == 0):
                moves = board.get_legal_moves(originalColor)
                oppMoves = board.get_legal_moves(originalColor * -1)
                heuristicVal = self.heuristicFunction(board, originalColor, moves, oppMoves, flag)
                return heuristicVal
            else:
                if(color == originalColor):
                    if(depth == 0):
                        return moves[weights.index(max(weights))]
                    else:
                        return max(weights)
                else:
                    return min(weights)

                        
    def get_ab_minimax_helper(self, board, color, depth, originalColor, flag, parentMinAB, parentMaxAB):
        if depth==self.depthLimit:
            #   moves = board.get_legal_moves(originalColor)
            #oppMoves = board.get_legal_moves(originalColor * -1)
            heuristicVal = self.heuristicFunction(board, originalColor, None, None, flag)
            return heuristicVal
        else:
            moves = board.get_legal_moves(color)
            weights = []
            localMinAB = float("-inf")
            localMaxAB = float("+inf")
            
            for move in moves:
                newboard = deepcopy(board)
                newboard.execute_move(move, color)
                if((move in self.badSquares) and color == originalColor):
                    flag = 1
                        #              if(depth==0):
                        #                  print(move)
                weight = self.get_ab_minimax_helper(newboard, color*-1, depth+1, originalColor, flag, localMinAB, localMaxAB)
                if(weight == None):
                    #          print("pruning")
                    #added this
                    weights.append(None)
                    continue
                if(color == originalColor):
                    if(weight > localMinAB):
                        localMinAB = weight
                    if(localMinAB > parentMaxAB):
                        return None
                else:
                    if(weight < localMaxAB):
                        localMaxAB = weight
                    if(localMaxAB < parentMinAB):
                        #           print("Parent Min: ", parentMinAB, " ", weights, " localMaxAB ", localMaxAB)
                        return None
                weights.append(weight)
                    #          if(depth ==1):
            #               print("Parent Min: ", parentMinAB, " weights ", weights)
            #means no moves, so this node can act as fringe node
            if(len(moves) == 0):
                # moves = board.get_legal_moves(originalColor)
                #oppMoves = board.get_legal_moves(originalColor * -1)
                heuristicVal = self.heuristicFunction(board, originalColor, None, None, flag)
                return heuristicVal
            else:
                if(color == originalColor):
                    if(depth == 0):
                        #      print("Max Weights", max(weights))
                        copy = weights.copy()
                        copy = [a for a in copy if a != None]
                        return moves[weights.index(max(copy))]
                    else:
                        weights = [a for a in weights if a != None]
                        return max(weights)
                else:
                    #                  print("Min Weights", min(weights))
                    weights = [a for a in weights if a != None]
                    return min(weights)

    def get_move(self, board, color, move_num=None,
             time_remaining=None, time_opponent=None):
        """ Wrapper function that chooses either vanilla minimax or alpha-beta. """
        f = self.get_ab_minimax_move if self.alpha_beta else self.get_minimax_move
        return f(board, color, move_num, time_remaining, time_opponent)
    
    def get_minimax_move(self, board, color, move_num=None,
                 time_remaining=None, time_opponent=None):
        """ Skeleton code from greedy.py to get you started. """
        # Get a list of all legal moves.
        # Return the best move according to our simple utility function:
        # which move yields the largest different in number of pieces for the
        # given color vs. the opponent?
        pos = self.get_minimax_helper(board, color, 0, color, 0)
        return pos

    def get_ab_minimax_move(self, board, color, move_num=None,
                 time_remaining=None, time_opponent=None):
        """ Skeleton code from greedy.py to get you started. """
        # Get a list of all legal moves.

        # Return the best move according to our simple utility function:
        # which move yields the largest different in number of pieces for the
        # given color vs. the opponent?
        self.depthLimit = 4

        pos = self.get_ab_minimax_helper(board, color, 0, color, 0, self.minAB, self.maxAB)

        return pos

    def _get_cost(self, board, color, move):
        """ Return the difference in number of pieces after the given move 
        is executed. """
        
        # Create a deepcopy of the board to preserve the state of the actual board
        newboard = deepcopy(board)
        newboard.execute_move(move, color)

        # Count the # of pieces of each color on the board
        num_pieces_op = len(newboard.get_squares(color*-1))
        num_pieces_me = len(newboard.get_squares(color))

        # Return the difference in number of pieces
        return num_pieces_me - num_pieces_op
        
engine = StudentEngine
