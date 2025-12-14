import heapq


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []

    def neighbors(self, vertex):
        return self.edges.get(vertex, [])


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph.edges}
    distances[start] = 0

    heap = [(0, start)]

    previous = {vertex: None for vertex in graph.edges}

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.neighbors(current_vertex):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))

    return distances, previous


def print_shortest_paths(distances, previous, start):
    print(f"The shortest paths from the vertex '{start}':")
    for vertex in distances:
        path = []
        current = vertex
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        print(f"To '{vertex}': distance = {distances[vertex]}, path = {' → '.join(path)}")


g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

start_vertex = 'A'
distances, previous = dijkstra(g, start_vertex)

print_shortest_paths(distances, previous, start_vertex)
