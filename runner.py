from game.gamePlay import *
from config import *
import argparse
from agents.template import RandomAgent
from agents.mcts_agent import MCTSAgent
from agents.minimax_agent import MinimaxAgent
from agents.rl_agent import ReinforceAgent
import sys
from datetime import datetime

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--agent1',default="random",type=str,help="First agent playing this game")
    parser.add_argument('--agent2',default="random",type=str,help="Second agent playing this game")
    parser.add_argument('--testLayout',default=None,type=str,help="If you need pre-config gameBoard input")
    parser.add_argument('--output',default=False,type=bool,help="Print to txt or not")

    args = parser.parse_args()

    if args.testLayout:
        gameState = GameState(args.testLayout)
    else:
        gameState = GameState(None)

    if args.agent1 == "random":
        agent1 = RandomAgent(BLACK_PLAYER,gameState)
    elif args.agent1 == "minimax":
        agent1 = MinimaxAgent(BLACK_PLAYER,gameState)
    elif args.agent1 == "mcts":
        agent1 = MCTSAgent(BLACK_PLAYER,gameState)
    elif args.agent1 == "rl":
        agent1 = ReinforceAgent(BLACK_PLAYER,gameState)
    
    if args.agent2 == "random":
        agent2 = RandomAgent(WHITE_PLAYER,gameState)
    elif args.agent2 == "minimax":
        agent2 = MinimaxAgent(WHITE_PLAYER,gameState)
    elif args.agent2 == "mcts":
        agent2 = MCTSAgent(WHITE_PLAYER,gameState)
    elif args.agent2 == "rl":
        agent2 = ReinforceAgent(WHITE_PLAYER,gameState)
    
    if args.output:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        sys.stdout = open(f'output/{timestamp}.txt','w',encoding="utf-8")
    
    players = [agent1,agent2]
    currPlayer = 0
    while not gameState.gameEnd():
        players[currPlayer].play()
        gameState.printGameBoard()
        currPlayer = 1 - currPlayer
    if gameState.score[0] > gameState.score[1]:
        print("Black Win!")
    elif gameState.score[0] < gameState.score[1]:
        print("White Win!")
    elif gameState.score[0] == gameState.score[1]:
        print("Draw!")


if __name__ == "__main__":

    main()
    sys.stdout.close()