from time import perf_counter
from random import randint

def difference_set(list1: list, list2: list) -> list:
    t1 = perf_counter()
    set_list2 = set(list2)
    res = [item for item in list1 if item not in set_list2]
    t2 = perf_counter()
    return t2 - t1

def difference_list(list1: list, list2: list) -> list:
    t1 = perf_counter()
    res = [item for item in list1 if item not in list2]
    t2 = perf_counter()
    return t2 - t1

n = 10000
lst1 = [randint(0, n) for i in range(n)]
lst2 = [randint(0, n) for i in range(n)]

print(f" SET: {difference_set(lst1, lst2):3e}")
print(f"LIST: {difference_list(lst1, lst2):3e}")