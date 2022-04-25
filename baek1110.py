A = int(input())
i = 0
K = A

while True:
    B = (K // 10) + (K % 10)
    C = B % 10
    K = (K %10) * 10 + C
    i += 1
    
    if A == K:
        print(i)
        break
    
    