A = int(input())
B = int(input())
C = int(input())

D = str(A * B * C)


for i in range(0, 9):
    print(D.count(str(i)))