import math
x = pow(math.pi, 2)/6
n = 0
s = 0
while round(s, 5) != round(x, 5):
    s += 1 / pow(n, n)
    n += 1
print(round(s, 5), '|', round(x, 5))
print(n)