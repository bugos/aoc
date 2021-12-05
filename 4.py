from itertools import islice, chain
import numpy as np

GRID_LEN = 5

fin = open('4.txt')
nums = list(map(int, next(fin).split(',')))
boards = []
for newln in fin:
  assert newln == '\n'
  boards.append(np.array([[int(n) for n in l.split()] for l in islice(fin, GRID_LEN)]))

# print(boards, boards[0].shape)

def isWinner(board, drawn: set):
  for row in chain(board, board.transpose()):
    unmarked = [n for n in row if n not in drawn]
    if not unmarked:
      return True
  return None

def playUntilFirstWins(boards, nums, checkedNums = 0):
  drawn = set()
  for i in range(0, len(nums)):
    drawn.add(nums[i])
    for b, board in enumerate(boards):
      if isWinner(board, drawn):
        return (b, drawn)

def playUntilLastWins(boards, nums):
  drawn = []
  while True:
    b, drawn = playUntilFirstWins(boards, nums, len(drawn))
    if (len(boards) == 1):
      return (b, drawn)
    print(len(drawn))
    boards.pop(b) # remove winning board
    print(len(boards))

def sumUnmarked(board, drawn):
  # return sum(sum(n for n in row if n not in drawn) for row in board)
  s = 0
  for row in board:
    unmarked = [n for n in row if n not in drawn]
    s += sum(unmarked)
  return s

def getScore(boards, b, drawn):
  return drawn[-1] * sumUnmarked(boards[b], drawn)
  
print(getScore(boards, *playUntilFirstWins(boards, nums)))
print(getScore(boards, *playUntilLastWins(boards, nums)))