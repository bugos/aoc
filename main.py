from timeit import default_timer as timer
import numpy as np

for i in range(1, 1 + 25):
  print(f"========= Day {i} ==========")
  start = timer()
  try:
    __import__(str(i))
  except ModuleNotFoundError:
    print("Not found")
    break
  end = timer()
  print("(", "Runtime:", end - start, ")")

