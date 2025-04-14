from config import *

class GameState:

    def __init__(self,gameBoard):
        # score: [black,white]
        if not gameBoard:
            self.gameBoard = self.initialiseGameBoard()
            self.score = [2,2]
        else:
            self.gameBoard = self.readPreconfigBoard(gameBoard)
            self.score = self.calculateScore()

    def initialiseGameBoard(self):
        
        gameBoard = [[EMPTY for i in range(0,DIMENSION)] for j in range(0,DIMENSION)]
        gameBoard[3][3] = WHITE
        gameBoard[3][4] = BLACK
        gameBoard[4][3] = BLACK
        gameBoard[4][4] = WHITE

        return gameBoard

    def readPreconfigBoard(self,path):
        with open(path,'r') as f:
            gameBoard = [[EMPTY for i in range(0,DIMENSION)] for j in range(0,DIMENSION)]
            row = -1
            col = -1
            for line in f:
                if line == "----------------------------------\n":
                    row += 1
                    continue
                else:
                    for j, char in enumerate(line):
                        if j % 2 == 0:
                            if char == "|":
                                col += 1
                            elif char == " ":
                                gameBoard[row][col] = EMPTY
                            elif char == BLACK:
                                gameBoard[row][col] = BLACK
                            elif char == WHITE:
                                gameBoard[row][col] = WHITE
                    col = -1
        return gameBoard

    def calculateScore(self):
        score = [0,0]
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.gameBoard[i][j] == WHITE:
                    score[1] += 1
                elif self.gameBoard[i][j] == BLACK:
                    score[0] += 1
        self.score = score

    def printGameBoard(self):

        print("White Score: " + str(self.score[0]))
        print("Black score: " + str(self.score[1]))
        print("")

        for i in range(0,DIMENSION):
            print("----------------------------------")
            for j in range(0,DIMENSION):
                if self.gameBoard[i][j] == EMPTY:
                    print("|   ", end="")
                if self.gameBoard[i][j] == BLACK:
                    print("| ● ",end="")
                if self.gameBoard[i][j] == WHITE:
                    print("| ○ ",end="")
            print("|")
        print("----------------------------------")
                
    def getValidMoves(self,playerId):

        validMoves = []
        if playerId == WHITE_PLAYER:
            us = WHITE
            opp = BLACK
        elif playerId == BLACK_PLAYER:
            us = BLACK
            opp = WHITE
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.gameBoard[i][j] == us:
                    validMoves = validMoves + self.checkOpposite(i,j,opp,NORTH)
                    validMoves = validMoves + self.checkOpposite(i,j,opp,SOUTH)
                    validMoves = validMoves + self.checkOpposite(i,j,opp,WEST)
                    validMoves = validMoves + self.checkOpposite(i,j,opp,EAST)
                    validMoves = validMoves + self.checkOpposite(i,j,opp,NORTH_WEST)
                    validMoves = validMoves + self.checkOpposite(i,j,opp,NORTH_EAST)
                    validMoves = validMoves + self.checkOpposite(i,j,opp,SOUTH_WEST)
                    validMoves = validMoves + self.checkOpposite(i,j,opp,SOUTH_EAST)

        return validMoves
    
    def checkOpposite(self,row,col,opp,direction):

        row,col = row+direction[0], col+direction[1]
        if self.inRange(row,col) and self.gameBoard[row][col] != opp:
            return []
        else:
            while self.inRange(row,col) and self.gameBoard[row][col] == opp:
                row,col = row+direction[0], col+direction[1]
            if self.inRange(row,col) and self.gameBoard[row][col] == EMPTY:
                return[(row,col)]
            return []
    
    def inRange(self,row,col):
        return row >= 0 and row < DIMENSION and col >= 0 and col < DIMENSION

    def gameEnd(self):
        return sum(self.score) == DIMENSION * DIMENSION
    
    def updateMove(self,move,playerId):
        # move = (row, col)
        if playerId == BLACK_PLAYER:
            piece = BLACK
        elif playerId == WHITE_PLAYER:
            piece = WHITE
        self.gameBoard[move[0]][move[1]] = piece
        self.flip(move,piece,NORTH)
        self.flip(move,piece,SOUTH)
        self.flip(move,piece,WEST)
        self.flip(move,piece,EAST)
        self.flip(move,piece,NORTH_WEST)
        self.flip(move,piece,NORTH_EAST)
        self.flip(move,piece,SOUTH_WEST)
        self.flip(move,piece,SOUTH_EAST)
        self.calculateScore()
    
    def flip(self,origin,piece,direction):

        origin = (origin[0] + direction[0], origin[1] + direction[1])
        cells = []
        while self.inRange(origin[0],origin[1]) and self.gameBoard[origin[0]][origin[1]] != piece and self.gameBoard[origin[0]][origin[1]] != EMPTY:
            cells.append(origin)
            origin = (origin[0] + direction[0], origin[1] + direction[1])
        if self.inRange(origin[0],origin[1]) and self.gameBoard[origin[0]][origin[1]] == piece:
            for cell in cells:
                self.gameBoard[cell[0]][cell[1]] = piece

            

    