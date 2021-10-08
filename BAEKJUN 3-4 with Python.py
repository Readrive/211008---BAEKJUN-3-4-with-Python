import sys

t = int(sys.stdin.readline())

i = 0

while i < t:
    a, b = map(int, sys.stdin.readline().split())

    c = a + b

    print(c)

    i += 1
