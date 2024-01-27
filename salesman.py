import sys

class TSP:
    def __init__(self, num_cities, distances):
        self.num_cities = num_cities
        self.distances = distances
        self.visited = [False] * num_cities
        self.route = []
    
    def nearest_neighbor(self, start_city):
        self.route.append(start_city)
        self.visited[start_city] = True
        current_city = start_city
        
        for _ in range(self.num_cities - 1):
            next_city = self._find_nearest_neighbor(current_city)
            self.route.append(next_city)
            self.visited[next_city] = True
            current_city = next_city
        
        self.route.append(start_city)  # Return to the starting city
    
    def _find_nearest_neighbor(self, city):
        min_distance = sys.maxsize
        nearest_city = None
        
        for i in range(self.num_cities):
            if not self.visited[i] and self.distances[city][i] < min_distance:
                min_distance = self.distances[city][i]
                nearest_city = i
        
        return nearest_city
    
    def get_route(self):
        return self.route
    
    def get_total_distance(self):
        total_distance = 0
        for i in range(self.num_cities):
            total_distance += self.distances[self.route[i]][self.route[(i + 1) % self.num_cities]]
        return total_distance

# Example usage
num_cities = 4
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp_solver = TSP(num_cities, distances)
start_city = 0
tsp_solver.nearest_neighbor(start_city)
route = tsp_solver.get_route()
total_distance = tsp_solver.get_total_distance()

print("Optimal route:", route)
print("Total distance:", total_distance)
