from statistics import median
import numpy as np

pos = list(map(int, next(open('6.txt')).split(',')))
mu = round(median(pos))

pos = np.array(pos)

def sumAbsDist(x, offset):
  return np.sum(np.absolute(x - offset))

print(sumAbsDist(pos, mu), mu)

# d*(d+1)/2 = (d**2 + d) / 2
def sumAbsDistKernel(x, offset):
  d = np.absolute(x - offset)
  dist = (d**2 + d) / 2
  return np.sum(np.absolute(dist))

prev_best = sumAbsDistKernel(pos, mu)
print("prev_best", prev_best, mu)
for i in range(mu): # TODO, this is arbitrary
  minus =sumAbsDistKernel(pos, mu - i)
  plus = sumAbsDistKernel(pos, mu + i)
  sign = 1
  best = min(plus, minus)
  # assert(plus != minus)
  sign = 1 if plus == best else -1
  # print(plus,minus)
  if(best > prev_best):
    print("found ", prev_best, best, sign * i, sign * i + mu)
    break
  else:
    prev_best = best
    

