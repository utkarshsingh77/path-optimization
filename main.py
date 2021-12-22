class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

	def solution(self, dist):
		print("Vertex-Source")
		for node in range(self.vertices):
			print(node, "-", dist[node])

	def min_distance(self, dist, spt_set):
		min_index = 0
		min_val = float("inf")
		for v in range(self.vertices):
			if dist[v] < min_val and not spt_set[v]:
				min_val = dist[v]
				min_index: int = v
		return min_index

	def dijkstra(self, src):
		dist = [sys.maxsize] * self.vertices
		dist[src] = 0
		spt_set = [False] * self.vertices

		for cout in range(self.vertices):
			u = self.min_distance(dist, spt_set)
			spt_set[u] = True

			for v in range(self.vertices):
				if self.graph[u][v] > 0 and not spt_set[v] and dist[v] > dist[u] + self.graph[u][v]:
					dist[v] = dist[u] + self.graph[u][v]

		self.solution(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
