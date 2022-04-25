C = int(input())

for i in range(0,C):
    s = list(map(int, input().split()))    
    m = (sum(s) - s[0]) / s[0]
    n = 0
    
    for j in range(1, len(s)):
        if s[j] > m:
            n += 1
    
    print(str(format(n/(len(s)-1)*100, ".3f")) + "%")
    