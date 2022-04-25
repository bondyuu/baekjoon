N = int(input())
A, B, C = map(int, input().split())

M = max(A, B, C)

print(round((A+B+C)/3 * 100 / M,2))