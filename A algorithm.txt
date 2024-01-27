import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic
    
    def __lt__(self, other):
        return self.total_cost < other.total_cost

class AStar:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic
    
    def find_path(self, start, goal):
        open_list = []
        closed_set = set()
        start_node = Node(start, cost=0, heuristic=self.heuristic(start, goal))
        heapq.heappush(open_list, start_node)
        
        while open_list:
            current_node = heapq.heappop(open_list)
            
            if current_node.state == goal:
                return self._construct_path(current_node)
            
            closed_set.add(current_node.state)
            
            for neighbor, cost in self.graph[current_node.state].items():
                if neighbor in closed_set:
                    continue
                
                new_cost = current_node.cost + cost
                new_heuristic = self.heuristic(neighbor, goal)
                new_total_cost = new_cost + new_heuristic
                
                existing_node = self._find_node(open_list, neighbor)
                if existing_node and existing_node.total_cost <= new_total_cost:
                    continue
                
                new_node = Node(neighbor, parent=current_node, cost=new_cost, heuristic=new_heuristic)
                heapq.heappush(open_list, new_node)
        
        return None  # No path found
    
    def _find_node(self, node_list, state):
        for node in node_list:
            if node.state == state:
                return node
        return None
    
    def _construct_path(self, node):
        path = []
        current = node
        while current:
            path.insert(0, current.state)
            current = current.parent
        return path

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def heuristic(state, goal):
    return 0  # Trivial heuristic for this example

astar = AStar(graph, heuristic)
start = 'A'
goal = 'D'
path = astar.find_path(start, goal)

if path:
    print("Path:", path)
else:
    print("No path found")
