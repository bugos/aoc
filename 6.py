DAYS = 256
REPRODUCTION_INTVL = 6
CHILDHOOD_INTVL = 2

fishes = list(map(int, next(open("6.txt")).split(',')))
fishCounts = [fishes.count(i) for i in range(REPRODUCTION_INTVL + CHILDHOOD_INTVL + 1)]

for day in range(DAYS):
  births = fishCounts[0]
  for i in range(len(fishCounts) - 1):
    fishCounts[i] = fishCounts[i + 1]
  fishCounts[REPRODUCTION_INTVL] += births
  fishCounts[REPRODUCTION_INTVL + CHILDHOOD_INTVL] = births

print(sum(fishCounts))


def _evolve(fishes): # Naive
  for i in range(len(fishes)):
    if (fishes[i] == 0):
      fishes.append(CHILDHOOD_INTVL + REPRODUCTION_INTVL)
      fishes[i] = REPRODUCTION_INTVL
    else:
      fishes[i] -= 1