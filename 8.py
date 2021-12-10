from functools import reduce
from operator import mul

nums = [[int(c) for c in l.strip()] for l in open('8.txt')]
assert(all(len(l) == len(nums[0]) for l in nums))
N, M = len(nums), len(nums[0])

def adjacent(i, j):
  return {(i+k, j+l)
    for k in range(-1, 2)
    for l in range(-1, 2)
    if k != l and not (k and l)
    if i+k in range(N) and j+l in range(M)
  }

def isLower(i, j, k, l): return nums[i][j] < nums[k][l]
def is9(i, j): return nums[i][j] == 9

lowPoints = [(i, j)
  for i in range(N) 
  for j in range(M) 
  if all(isLower(i, j, *adj) 
    for adj in adjacent(i, j))]
print(sum(nums[i][j]+1 for i, j in lowPoints))

# part 2
def getBasinSize(point, basinPoints): # ret size
  assert(point not in basinPoints)
  basinPoints |= {point}
  return 1 + sum(getBasinSize(adj, basinPoints)
  for adj in adjacent(*point)
    if isLower(*point, *adj)
    and not adj in basinPoints
    and not is9(*adj))

basinSizes = [getBasinSize(p, set()) for p in lowPoints]
print(reduce(mul, sorted(basinSizes, reverse=True)[:3]))


    

