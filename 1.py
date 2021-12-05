SLIDING_WIND_LEN = 3

nums = [int(n) for n in open('1.txt')] # input
nPositiveDiff = 0 # output

for i in range(SLIDING_WIND_LEN, len(nums)):
  if (nums[i] > nums[i - SLIDING_WIND_LEN]):
    nPositiveDiff += 1

print(nPositiveDiff)
