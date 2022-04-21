import sys

test_case = int(input())

for i in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #1:", a+b)