from itertools import islice, chain
import numpy as np

GRID_LEN = 5

fin = open('40.txt')
nums = list(map(int, next(fin).split(',')))
boards = []
for newln in fin:
  assert newln == '\n'
  boards.append(np.array([[int(n) for n in l.split()] for l in islice(fin, GRID_LEN)]))

# print(boards, boards[0].shape)

def isWinner(board, drawn: dict):
  # isin = np.isin(board, list(drawn))
  # return np.any(np.all(isin, axis = 0)) or np.any(np.all(isin, axis = 1))
  return any(all(n in drawn for n in row) \
    for row in chain(board, board.transpose()))

def playUntilFirstWins(boards, nums, drawn = dict()):
  lastDrawnIdx = max(0, len(drawn) - 1)
  for i in range(lastDrawnIdx, len(nums)):
    drawn[nums[i]] = True
    for b, board in enumerate(boards):
      if isWinner(board, drawn):
        return (b, drawn)

def playUntilLastWins(boards, nums):
  drawn = dict()
  while True:
    b, drawn = playUntilFirstWins(boards, nums, drawn)
    if (len(boards) == 1):
      return (b, drawn)
    boards.pop(b) # remove winning board
    # print(len(boards), len(drawn))

def sumUnmarked(board, drawn):
  # return sum(sum(n for n in row if n not in drawn) for row in board)
  s = 0
  for row in board:
    unmarked = [n for n in row if n not in drawn]
    s += sum(unmarked)
  return s

def getScore(boards, b, drawn):
  return list(drawn)[-1] * sumUnmarked(boards[b], drawn)
  
print(getScore(boards, *playUntilFirstWins(boards, nums)))
# print(getScore(boards, *playUntilLastWins(boards, nums)))