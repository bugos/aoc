from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

_lines = open('13.txt').readlines()
_space = _lines.index('\n')
points = {Point(*map(int, l.strip().split(','))) for l in _lines[:_space]}
folds = [l.strip().split('fold along ')[1].split('=') for l in _lines[_space + 1:]]
folds = [(axis, int(a)) for axis, a in folds]

def foldPoint(p, axis, axisPos):
  if (a := getattr(p, axis)) > axisPos:
    return p._replace(**{axis: 2 * axisPos - a})
  return p

def foldPoints(points, fold):
  return {foldPoint(p, *fold) for p in points}

def printPoints(points):
  N = max(x for x, y in points)
  M = max(y for x, y in points)
  for y in range(M + 1):
    print(''.join('#' if Point(x, y) in points else ' ' for x in range(N + 1)))

print(len(foldPoints(points, folds[0]))) # 747

for fold in folds:
  points = foldPoints(points, fold)
printPoints(points)

 ##  ###  #  # #### ###   ##  #  # #  #
#  # #  # #  #    # #  # #  # #  # #  #
#  # #  # ####   #  #  # #    #  # ####
#### ###  #  #  #   ###  #    #  # #  #
#  # # #  #  # #    #    #  # #  # #  #
#  # #  # #  # #### #     ##   ##  #  #
