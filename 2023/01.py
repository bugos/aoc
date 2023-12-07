EXAMPLE_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".splitlines()
PUZZLE_INPUT = open(__file__.replace(".py", ".txt"))

def firstDigit(s: [str]) -> int:
    # return int(next(filter(str.isdigit, s)))
    for c in s:
        if c.isdigit():
           return int(c)
    raise

def task1(lines: [str]) -> int:
  decode = lambda line: firstDigit(line) * 10 + firstDigit(reversed(line))
  return sum(decode(line) for line in lines)

assert task1(EXAMPLE_INPUT) == 142
assert task1(PUZZLE_INPUT) == 57346
