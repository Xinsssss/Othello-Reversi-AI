from config import *
import random

class Agent:

    def __init__(self,playerId,gameState):
        self.playerId = playerId
        self.gameState = gameState
    
    def nextMove(self):
        return
    

class RandomAgent(Agent):


    def __init__(self,playerId,gameState):
        super().__init__(playerId,gameState)
    
    def play(self):
        move = self.nextMove()
        if move:
            self.gameState.updateMove(move,self.playerId)
    
    def nextMove(self):
        validMoves = self.gameState.getValidMoves(self.playerId)
        if validMoves:
            return random.choice(validMoves)
        return None
