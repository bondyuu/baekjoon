x = int(input())

i=1
sum=0
while sum < x:
    sum += i
    i += 1

k = sum - x + 1

if i%2==1:   
    print(i-k,"/",k,sep="")
else:
    print(k,"/",i-k,sep="")