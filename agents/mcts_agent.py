from .template import Agent

class MCTSAgent(Agent):

    def __init__(self,playerId,gameState):
        super.__init__(playerId,gameState)