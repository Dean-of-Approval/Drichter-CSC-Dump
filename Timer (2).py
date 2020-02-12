from timeit import Timer
import random

list_timer = Timer("test_list(x, i)",
                "from __main__ import test_list, x, i")
dict_timer = Timer("test_dict(d, i)",
               "from __main__ import test_dict, d, i")

print("\tlist \t  dict")

def test_list(x, i):
  rand = random.randint(0, i)
  if rand in x:
    pass

def test_dict(d, i):
  rand = random.randint(0, i)
  if rand in d:
    pass

for i in range(100000,1000001,100000):
    x = list(range(i))
    lt = list_timer.timeit(number=1000)
    d = dict.fromkeys(x, 1)
    dt = dict_timer.timeit(number=1000)
    print("%15.5f, %15.5f" %(lt, dt))