import math
def hash(x, i):
    return (x**2 - math.floor(1.5 * x) + i) % 10

arr = [67, 90, 93, 87, 51, 3, 37]
d = { i: [] for i in range(10) }
for i in range(len(arr)):
    h = hash(arr[i], i)
    d[h].append(arr[i])

print(d)
