from itertools import islice, chain
import numpy as np

GRID = 5

fin = open('40.txt')
nums = list(map(int, next(fin).split(',')))
boards = [np.array([list(map(int, l.split())) \
  for l in islice(fin, GRID)], dtype=np.int8) \
  for _newln in fin]

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
  b, drawn = playUntilFirstWins(boards, nums)
  while len(boards) != 1:
    boards.pop(b) # remove winning board
    b, drawn = playUntilFirstWins(boards, nums, drawn)
  return (b, drawn)

def getScore(boards, b, drawn):
  sumUnmarked = sum(n for row in boards[b] for n in row if n not in drawn)
  return list(drawn)[-1] * sumUnmarked
  
print(getScore(boards, *playUntilFirstWins(boards, nums)))
print(getScore(boards, *playUntilLastWins(boards, nums)))