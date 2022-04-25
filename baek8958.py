N = int(input())

for i in range(0, N):
    s = 0
    rpt = list(input().split("X"))
     
    for j in range(0, len(rpt)):
        p = len(rpt[j])*(len(rpt[j])+1)/2
        s = s + p
    
    print(int(s))