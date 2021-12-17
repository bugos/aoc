#15:20 - 15:38
from collections import Counter, defaultdict
GEN = 40

_templ, _rules = open('14.txt').read().split('\n\n')
templ = _templ.strip()
rules = dict(l.split(' -> ') for l in _rules.split('\n'))

mem = {(pair, 1): Counter(c) for pair, c in rules.items()}
def applyRules(pair, gen = GEN):
  if not mem.get((pair, gen)):
    newChar = rules[pair]
    mem[pair, gen] = applyRules(pair[0] + newChar, gen - 1) \
                   + Counter(newChar) \
                   + applyRules(newChar + pair[1], gen - 1)
  return mem[pair, gen]

pairFreq = (applyRules(templ[i:i+2]) for i in range(len(templ) - 1))
charFreq = sum(pairFreq, start = Counter(templ)).most_common()
print(charFreq[0][1] - charFreq[-1][1]) # 8336623059567

