from .template import Agent
from copy import deepcopy
from config import *

class MinimaxAgent(Agent):

    def __init__(self,playerId):
        super().__init__(playerId)
    
    def setGameState(self,gameState):
        super().setGameState(gameState)
    
    def play(self):
        super().play()
    
    def nextMove(self):
        
        validMoves = self.gameState.getValidMoves(self.playerId)
        scores = {}
        nextStates = {}
        for move in validMoves:
            nextState = deepcopy(self.gameState)
            nextState.updateMove(move,self.playerId)
            nextStates[nextState] = nextState.score[self.playerId]
        nextStates = sorted(nextStates, key=nextStates.get, reverse=True)
        if len(nextStates) > REDUCED_MOVE_LENGTH:
            nextStates = nextStates[:REDUCED_MOVE_LENGTH]

        for nextState in nextStates:
            bestScore = self.miniMax(self.playerId,MAX_SCORE,MIN_SCORE,nextState,MINIMAX_DEPTH)
            scores[move] = bestScore

        if scores:
            bestMove = max(scores,key=scores.get)
            return bestMove
        return None


    
    def miniMax(self, Id, alpha, beta, gameState, depth):

        if gameState.gameEnd() or depth == 0:
            return gameState.score[self.playerId] - gameState.score[1-self.playerId]
        
        if Id == self.playerId: # Maximising player
            bestScore = MAX_SCORE
            validMoves = gameState.getValidMoves(Id)
            for move in validMoves:
                nextState = deepcopy(gameState)
                nextState.updateMove(move,Id)
                score = self.miniMax(1-Id, alpha, beta, nextState,depth-1)
                bestScore = max(score,bestScore)
                alpha = max(alpha,bestScore)
                if beta <= alpha:
                    break
            return bestScore
        
        if Id == 1 - self.playerId: #Minimising player
            bestScore = MIN_SCORE
            validMoves = gameState.getValidMoves(Id)
            for move in validMoves:
                nextState = deepcopy(gameState)
                nextState.updateMove(move,Id)
                score = self.miniMax(1-Id,alpha, beta, nextState,depth-1)
                bestScore = min(score,bestScore)
                beta = min(beta,bestScore)
                if beta <= alpha:
                    break
            return bestScore

        

