class Node:
    def __init__(self, state, cost, accumulated_cost, heuristic):
        self.state = state
        self.cost = cost
        self.accumulated_cost = accumulated_cost
        self.heuristic = heuristic

    def __gt__(self, other):
        if (self.accumulated_cost+self.heuristic) > (other.accumulated_cost + other.heuristic):
            return True
        if (self.accumulated_cost+self.heuristic) == (other.accumulated_cost + other.heuristic):
            return self.state > other.state

