from collections import namedtuple
import numpy as np

Point = namedtuple('Point', ['x', 'y'])
Segment = namedtuple('Segment', ['A', 'B'])

segments = [Segment(*[Point( \
  *map(int, segm.split(','))) \
  for segm in l.split(' -> ')]) \
  for l in open('50.txt')]
dim = max(c for s in segments for p in s for c in p) + 1

def markSegments(segments, includeDiag=False):
  B = np.zeros(shape=(dim,dim), dtype= np.int16)
  for p1, p2 in segments:
    if p1.x == p2.x:
      y1, y2 = sorted((p1.y, p2.y))
      B[p1.x, y1:y2+1] += 1
    elif p1.y == p2.y:
      x1, x2 = sorted((p1.x, p2.x))
      B[x1:x2+1, p1.y] += 1
    elif not includeDiag:
      if p2.x < p1.x: # sort on x
        p1, p2 = (p2, p1)
      slope = 1 if p2.y > p1.y else -1

      for x, y in zip(range(p1.x, p2.x+1), range(p1.y, p2.y+slope, slope)):
        B[x,y] += 1
  return (B > 1).sum()

print(markSegments(segments))
print(markSegments(segments, True))