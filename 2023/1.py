SLIDING_WIND_LEN = 3

from string import digits

def firstDigit(s):
    for c in s:
        if c in digits:
            return c


s = 0
for line in TASK_1:
  s += firstDigit(line) * 10 + firstDigit(reversed(line))
print (s)


print(nPositiveDiff)

TASK_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""