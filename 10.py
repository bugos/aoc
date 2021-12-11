from collections import Counter
from functools import reduce
from statistics import median

lines = [l.strip() for l in open('10.txt')]

pairs = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}
pairCost = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}
pairCost2 = dict(zip(pairs, range(1, 5)))

def parseLine(line, corrupt):
  opened = []
  for c in line:
    if c in pairs:
      opened.append(c)
    elif c != pairs[opened.pop()]:
      corrupt[c] += 1
      return []
  return opened

corrupt = Counter()

scores2 = [reduce(
    lambda score, c: score * 5 + pairCost2[c], 
    reversed(parseLine(line, corrupt)),
    0)
  for line in lines]

print(sum(corrupt[c] * pairCost[c] for c in pairCost)) # part1
print(median(s for s in scores2 if s != 0))

