# Based on projectPxl and dionyziz

import heapq

risk = [list(map(int, l.strip())) for l in open('15.txt')]
N = len(risk)

def neighbours(x, y):
  return ((x+dx, y+dy) 
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)) 
    if x+dx in range(N) and y+dy in range(N))

def dijkstra(graph, start, end):
  frontier  = [(0, (0, 0))]
  visited = set()

  while frontier:
    cost, current = heapq.heappop(frontier)
    if current in visited:
      continue # optimization
    visited.add(current)

    for neigh in neighbours(*current):
      if neigh not in visited:
        neigh_cost = cost + graph[neigh[0]][neigh[1]]
        if neigh == end:
          return neigh_cost
        heapq.heappush(frontier, (neigh_cost, neigh))

print(dijkstra(risk, (0, 0), (N-1, N-1)))# dijkstra(risk2, len(risk2), len(risk2[0])))

# Relaxation step is missing because we don't care from which node we are comming from. All edge weights are the same. Also we don't need the path.
