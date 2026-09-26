import random
import time
import requests
import numpy as np
import pandas as pd

# from декораторы import time_run, null, in_out

# l = random.sample(range(0, 1000000), 1000000)
# ll = l.copy()
#
# @time_run
# def r1():
#     res1 = list(map(str, l))
#     print(res1[:5])
#
# @time_run
# def r2():
#     res2 = [str(i) for i in ll]
#     print(res2[:5])
#
#
# r1()
# r2()

# @time_run
# def etalon(n, m, x):
#     print('START')
#     time.sleep(n+m)
#     print(x)
#
# # etalon(3, 1, x=10)
# @in_out
# def summer(x, y):
#     return x + y
#
# res = summer(random.randint(1, 100),
#              random.randint(1, 100)) / 3.45 ** 3
# print(res)

from dataclasses import dataclass
#
# d = {'key1': {'key1':'info1',
#               'key2':'info2'}
#      }
#
# print(d['key1'].get('key3'))

# try:
#     res = requests.get(
#         "http://127.0.0.1:8000/items/78?q='text'" )
#     res.raise_for_status()
#     res = res.json()
#     print(res.get('first_response'))
#     print(res.get('q'))
# except Exception as e:
#     print(f' {e}')
d = {}
for i in open('ice-cream.csv', encoding='utf-8'):
    # toppings = i.strip().split(';')
    for topping in set(i.strip().split(';')):
        d[topping] = d.get(topping, 0) + 1
# print(max(d.items(), key=lambda x: x[1])[0])
# mx = 0
# name = ''
# for k, v in d.items():
#     if v > mx:
#         mx = v
#         name = k
# print(list(d.items()))

# print(kv_max[0])


# про numpy

def power(n):
    return n ** 2


l = [ 2, 4, 3, 5]
arr = np.array(l)
l = l * 2
arr = arr * 2
print(l)
print(arr)
print(power(arr))
print(list(map(power, l)))
print(arr.shape)
# arr.shape = 2,2
arr1 = arr.reshape(-1, 2)
print(arr)
print(arr1)
arr1[0, 1] = 80
print(arr)
print(arr1)

sr = pd.Series(arr, index=['a', 'b', 'c', 'd'])
print(sr)
print(sr.b)
df = pd.DataFrame(arr1, index=['a', 'b'], columns=['first', 'second'])
print(df)

df = pd.read_csv('ice-cream.csv', sep=';')

print(df)