oct = [[int(c) for c in l.strip()] for l in open('11.txt')]
FLASH_ENERGY = 10

def adjacent(i, j):
  return {(i+k, j+l)
    for k in range(-1, 2)
    for l in range(-1, 2)
    if k or l
    if i+k >= 0 and j+l >= 0
    and i+k < 10 and j+l < 10
  }

def flash(i, j, flashed):
  assert((i, j) not in flashed)
  flashed.add((i,j))
  oct[i][j] = 0

  for adj in adjacent(i, j):
    incEnergy(*adj, flashed)

def incEnergy(i, j, flashed):
  if ((i, j) in flashed):
    return

  assert(oct[i][j] < FLASH_ENERGY)
  oct[i][j] += 1

  if (oct[i][j]) == FLASH_ENERGY:
    flash(i, j, flashed)


nFlashes = 0
for gen in range(1, 1000 + 1):
  flashed = set()
  for i in range(len(oct)):
    for j in range(len(oct[i])):
      incEnergy(i, j, flashed)
  nFlashes += len(flashed)
  if len(flashed) == 100:
    print("synced", gen)
    break
  if gen == 100:
    print(nFlashes)