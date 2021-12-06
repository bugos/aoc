from collections import namedtuple
import numpy as np

DIM = 1024

Point = namedtuple('Point', ['x', 'y'])
Segment = namedtuple('Segment', ['A', 'B'])

segments = [Segment(*[Point( \
  *map(int, segm.split(','))) \
  for segm in l.split(' -> ')]) \
  for l in open('5.txt')]

B = np.zeros(shape=(DIM,DIM), dtype= np.int16)
for segm in segments:
  p1, p2 = segm
  if p1.x == p2.x:
    y1, y2 = sorted((p1.y, p2.y))
    B[p1.x, y1:y2+1] += 1
  elif p1.y == p2.y:
    x1, x2 = sorted((p1.x, p2.x))
    B[x1:x2+1, p1.y] += 1
  else: # 2nd task only
    if p2.x < p1.x: # sort on x
      p1, p2 = (p2, p1)
    slope = 1 if p2.y > p1.y else -1

    for x, y in zip(range(p1.x, p2.x+1), range(p1.y, p2.y+slope, slope)):
      B[x,y] += 1  

# print(B)
print((B > 1).sum())


