from game.gamePlay import *
from config import *
import argparse
from agents.template import RandomAgent
from agents.mcts_agent import MCTSAgent
from agents.minimax_agent import MinimaxAgent
from agents.rl_agent import ReinforceAgent
import sys
from datetime import datetime
import copy


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--agent1',default="random",type=str,help="First agent playing this game")
    parser.add_argument('--agent2',default="random",type=str,help="Second agent playing this game")
    parser.add_argument('--testLayout',default=None,type=str,help="If you need pre-config gameBoard input")
    parser.add_argument('--output',default=False,type=bool,help="Print to txt or not")
    parser.add_argument('--turns',default=1,type=int,help="Number of turns you want to run")

    args = parser.parse_args()

        
    if args.output:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        sys.stdout = open(f'output/{timestamp}.txt','w',encoding="utf-8")

    if args.testLayout:
        gameState = GameState(args.testLayout)
    else:
        gameState = GameState(None)

    if args.agent1 == "random":
        agent1 = RandomAgent(BLACK_PLAYER)
    elif args.agent1 == "minimax":
        agent1 = MinimaxAgent(BLACK_PLAYER)
    elif args.agent1 == "mcts":
        agent1 = MCTSAgent(BLACK_PLAYER)
    elif args.agent1 == "rl":
        agent1 = ReinforceAgent(BLACK_PLAYER)
    
    if args.agent2 == "random":
        agent2 = RandomAgent(WHITE_PLAYER)
    elif args.agent2 == "minimax":
        agent2 = MinimaxAgent(WHITE_PLAYER)
    elif args.agent2 == "mcts":
        agent2 = MCTSAgent(WHITE_PLAYER)
    elif args.agent2 == "rl":
        agent2 = ReinforceAgent(WHITE_PLAYER)

    agent1Win = 0
    agent2Win = 0
    draw = 0
    agent1Score = 0
    agent2Score = 0
    num = 0
    for i in range(args.turns):
        currGameState = copy.deepcopy(gameState)
        agent1.setGameState(currGameState)
        agent2.setGameState(currGameState)
        players = [agent1,agent2]
        currPlayer = 0
        while not currGameState.gameEnd():
            players[currPlayer].play()
            #if not args.output:
                #print(f"One move from agent {currPlayer}, {sum(currGameState.score)}")
            currPlayer = 1 - currPlayer
            if args.output:
                currGameState.printGameBoard()
        if currGameState.score[0] > currGameState.score[1]:
            if args.output:
                print("Black Wins!")
            agent1Win += 1
        elif currGameState.score[0] < currGameState.score[1]:
            if args.output:
                print("White Wins!")
            agent2Win += 1
        else:
            if args.output:
                print("Draw!")
            draw += 1
        agent1Score += currGameState.score[0]
        agent2Score += currGameState.score[1]
        if not args.output:
            num += 1
            print(f"{num} out of {args.turns} games end")
    agent1AvgScore = agent1Score/args.turns
    agent2AvgScore = agent2Score/args.turns

    print(f"Black ({args.agent1}) won {agent1Win} out of {args.turns} with an average score of {agent1AvgScore}")
    print(f"White ({args.agent2}) won {agent2Win} out of {args.turns} with an average score of {agent2AvgScore}")
    print(f"Total of {draw} draws out of {args.turns}")



if __name__ == "__main__":

    main()
    sys.stdout.close()