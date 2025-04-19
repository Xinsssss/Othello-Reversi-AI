from config import *
import random

class Agent:

    def __init__(self,playerId):
        self.playerId = playerId
        self.gameState = None
    
    def play(self):
        move = self.nextMove()
        if move:
            self.gameState.updateMove(move,self.playerId)
        
    
    def nextMove(self):
        return
    
    def setGameState(self,gameState):
        self.gameState = gameState

    

class RandomAgent(Agent):


    def __init__(self,playerId):
        super().__init__(playerId)
    
    def setGameState(self,gameState):
        super().setGameState(gameState)
    
    def play(self):
        super().play()
    
    def nextMove(self):
        validMoves = self.gameState.getValidMoves(self.playerId)
        if validMoves:
            return random.choice(validMoves)
        return None
