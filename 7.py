from collections import namedtuple

Reading = namedtuple('Reading', ['patterns', 'outVals'])

parseReading = lambda s: list(map(lambda s: ''.join(sorted(s.strip())), s.split()))
readings = [Reading(*map(parseReading, l.split('|'))) for l in open('7.txt')]

# part 1
print(sum(len(outVal) in [2, 4, 3, 7] for _, outVals in readings for outVal in outVals))

# part 2
# TODO: We can look only on known digits [2, 4, 3, 7]
letters = {*map(chr, range(ord('a'), ord('g')+1))}
digits = {*range(10)}
digitLetters = {
  0 : letters - {'d'},
  1 : {'c', 'f'},
  2:  letters - set('bf'),
  3:  letters - set('be'),
  4:  letters - set('aeg'),
  5:  letters - set('ce'),
  6:  letters - set('c'),
  7 : {'a', 'c', 'f'},
  8 : letters,
  9 : letters - set('e'),
}

def getLetterBij(PATTERNS):
  lenMatch = lambda replDigitS: lambda d: len(digitLetters[d]) == len(replDigitS)
  digitBijection = {
    replaced : {*filter(lenMatch(PATTERNS[replaced]), digits)}
    for replaced in digits
  }

  # check letters must exist/not exist in at least one of the bijected digits
  letterBij = lambda replLettter: lambda letter: \
    all(any((letter in letters) == (replLettter in PATTERNS[replD]) \
      for replD, orig in digitBijection.items() if digitWithLetter in orig) \
    for digitWithLetter, letters in digitLetters.items())
  letterBijection = {
    replaced : {*filter(letterBij(replaced), letters)}
    for replaced in letters
  }

  # remove letters that are already determined
  for _ in range(1): # 1 happens to be enough
    determOrigLetters = {next(iter(orig)) for repl, orig in letterBijection.items() if len(orig) == 1}
    for repl, orig in letterBijection.items():
      if len(orig) != 1:
        orig -= determOrigLetters
  
  # print(sum(len(orig) for repl, orig in letterBijection.items()))
  return letterBijection


def decryptWord(letterBijection, word):
  decr = {next(iter(letterBijection[l])) for l in word}
  return next(digit for digit, letters in digitLetters.items() if decr == letters)

s = 0
for patterns, outVals in readings: # TODO
  letterBijection = getLetterBij(patterns)

  for i, outVal in enumerate(outVals):
    digit = decryptWord(letterBijection, outVal)
    s += digit * (10 ** (3-i))
    # print(i, digit, s)
  # print("-------")
  # break

print(s)