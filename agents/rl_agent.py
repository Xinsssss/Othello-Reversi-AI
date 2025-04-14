from .template import Agent

class ReinforceAgent(Agent):

    def __init__(self,playerId,gameState):
        super.__init__(playerId,gameState)