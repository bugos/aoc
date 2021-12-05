nums = [n.strip() for n in open('3.txt')]

def find_most_common(nums: 'list[str]'):
  ones = [0] * len(nums[0])
  for n in nums:
    for i, c in enumerate(n):
      if c == '1':
        ones[i] += 1

  return "".join('1' if o >= len(nums) / 2 else '0' for o in ones)

most_common = find_most_common(nums)
gamma_rate = int(most_common, 2)
epsilon_rate = gamma_rate ^ (2 ** len(nums[0]) - 1)
print(gamma_rate * epsilon_rate)

def find_rating(nums:'list[str]', least_common=False):
  matches = nums
  for i in range(len(nums[0])):
    most_common = find_most_common(matches)
    if least_common:
      most_common = "".join("1" if c == "0" else "0" for c in most_common) # '0' <-> '1'
    matches = list(filter(lambda s: s[i] == most_common[i], matches))
    if len(matches) == 1:
      return int(matches[0], 2)

print(find_rating(nums) * find_rating(nums, least_common=True))
