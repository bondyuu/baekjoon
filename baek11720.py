n = int(input())
a = input()
sum = 0

for i in range(n):
    sum += int(str(a)[i])
    
print(sum)