# 22:02
from math import copysign
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
sign = lambda x: math.copysign(1, x)

target = tuple(map(lambda s: tuple(map(int, s.split('=')[1].split('..'))), next(open('170.txt')).split(',')))

print(target)

def inTarget(p):
  return target[0][0] <= p.x <= target[0][1] \
    and target[1][0] <= p.y <= target[1][1]

def getPos(u0, t, p0 = Point(0, 0)):
  t_ux_0 = u0.x + 1
  ux_sign = lambda v: copysign(v, u0.x)
  drag_sat = lambda f_t, t: f_t(t) if t < t_ux_0 else f_t(t_ux_0) 
  # ux = drag_sat(lambda t: u0.x - ux_drag(t), t) 
  # uy = u0.y - (t-1)

  drag = t * (t-1) / 2
  px = drag_sat(lambda t: u0.x * t - ux_sign(drag), t)
  py = u0.y * t - drag

  # px = u0.x * t - drag if t < t_ux_0
  # py = u0.y * t - drag
  return Point(px, py)

M = min(target[1])
uy_min, uy_max = (M, -M - 1) # to reach target
x_min = int((target[0][0] / 2 + 1) **  0.5 - 1)
assert(getPos(Point(0, uy_max), -2 * M).y == M)
p_in_target = 0
for ux in range(x_min, target[0][1] + 1):
  t_ux_0 = ux + 1 # optim
  x_final = (ux ** 2 + ux) / 2 # optim
  for uy in range(uy_min, uy_max + 1):
    t_min = 2 * uy + 2 if uy > 0 else 0 #optimization
    for t in range(t_min, 300):
      # p = getPos(Point(ux, uy), t)

      drag = t * (t-1) / 2 # optim
      p = Point(
        ux * t - drag if t < t_ux_0 else x_final,
        uy * t - drag
      )
      if inTarget(p):
        p_in_target += 1
        break
      if p.x > target[0][1] or p.y < target[1][0]:
        break
print(p_in_target)

