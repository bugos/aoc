# 0:10 - 0:35 - 0:52
from collections import defaultdict

adj = defaultdict(list)
for l in open('12.txt'):
  a, b = l.strip().split('-')
  adj[a].append(b)
  adj[b].append(a)

def countPaths(pos, visited = set(), done2nd = False):
  assert(adj[pos])

  if pos == 'end':
    return 1

  visited = visited.copy()
  if not pos.isupper():
    visited.add(pos)

  paths_to_end = 0
  for edge in adj[pos]:
    if edge not in visited:
      paths_to_end += countPaths(edge, visited, done2nd)
    elif not done2nd and edge != 'start':
      paths_to_end += countPaths(edge, visited, True)
  return paths_to_end

print(countPaths('start', done2nd=True), 4775)
# print(countPaths('start', done2nd=False), 152480)
