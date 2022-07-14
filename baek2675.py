case = int(input())

for i in case:
    mul, txt = map(input().split())
    rst = ""
    
    for k in txt:
        rst += k * int(mul)
        
    print(rst)
