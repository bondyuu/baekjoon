H, M = map(int, input().split())
D = int(input())

AM = (M + D) % 60
AH = int(H + ((M + D) / 60))

if AH < 24:
    print(AH, AM)
elif AH >23:
    AH -= 24
    print(AH, AM)

