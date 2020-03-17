'''
driver for graph search problem
'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies


class Timer:
    """Timer class
    Usage:
      t = Timer()
      # figure out how long it takes to do stuff...
      elapsed_s = t.elapsed_s() OR elapsed_min = t.elapsed_min()
    """
    
    def __init__(self):
        "Timer - Start a timer"
        self.s_per_min = 60.0  # Number seconds per minute
        self.start = time.time()

    def elapsed_s(self):
        "elapsed_s - Seconds elapsed since start (wall clock time)"
        return time.time() - self.start

    def elapsed_min(self):
        "elapsed_min - Minutes elapsed since start (wall clock time)"

        # Get elapsed seconds and convert to minutes
        return self.elapsed_s() / self.s_per_min
    
def driver() :
    bfsLengthList = []
    bfsNodesExpandedList = []
    bfsTimeList = []

    dfsLengthList = []
    dfsNodesExpandedList = []
    dfsTimeList = []

    manLengthList = []
    manNodesExpandedList = []
    manTimeList = []

    for i in range(2):      #change back to 31
        tempBoard = TileBoard(8)        #force_state=(1,2,3,4,5,6,7,8,None)

        #Breadth First Search
        bfs = NPuzzle(8,g=BreadthFirst.g,force_state=tempBoard.state_tuple())
        tempTimer = Timer()
        path,numNodes = graph_search(bfs, verbose=True)
        bfsTimeList.append(tempTimer.elapsed_s())
        bfsNodesExpandedList.append(numNodes)
        bfsLengthList.append(len(path))

        #Depth First Search
        dfs = NPuzzle(8,g=DepthFirst.g,force_state=tempBoard.state_tuple())
        tempTimer = Timer()
        path,numNodes = graph_search(dfs, verbose=True)
        dfsTimeList.append(tempTimer.elapsed_s())
        dfsNodesExpandedList.append(numNodes)
        dfsLengthList.append(len(path))

        #Manhattan Search
        manhattan = NPuzzle(8, h=Manhattan.h, force_state=tempBoard.state_tuple())
        tempTimer = Timer()
        path, numNodes = graph_search(manhattan, verbose=True)
        manTimeList.append(tempTimer.elapsed_s())
        manNodesExpandedList.append(numNodes)
        manLengthList.append(len(path))

    print("BFS Average Path Length:",mean(bfsLengthList))
    print("BFS Average Nodes Expanded:",mean(bfsNodesExpandedList))
    print("BFS Average Time Elapsed:",mean(bfsTimeList))

    print("DFS Average Path Length:", mean(dfsLengthList))
    print("DFS Average Nodes Expanded:",mean(dfsNodesExpandedList))
    print("DFS Average Time Elapsed:",mean(dfsTimeList))

    print("Manhattan Average Path Length:", mean(manLengthList))
    print("Manhattan Average Nodes Expanded:", mean(manNodesExpandedList))
    print("Manhattan Average Time Elapsed:", mean(manTimeList))

    print("BFS Standard Deviation Path Length:", stdev(bfsLengthList))
    print("BFS Standard Deviation Nodes Expanded:", stdev(bfsNodesExpandedList))
    print("BFS Standard Deviation Time Elapsed:", stdev(bfsTimeList))
  
    print("DFS Standard Deviation Path Length:", stdev(dfsLengthList))
    print("DFS Standard Deviation Nodes Expanded:", stdev(dfsNodesExpandedList))
    print("DFS Standard Deviation Time Elapsed:", stdev(dfsTimeList))

    print("Manhattan Standard Deviation Path Length:", stdev(manLengthList))
    print("Manhattan Standard Deviation Nodes Expanded:", stdev(manNodesExpandedList))
    print("Manhattan Standard Deviation Time Elapsed:", stdev(manTimeList))


if __name__ == '__main__':
    driver()
