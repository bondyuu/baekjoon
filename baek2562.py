num_list = list(map(int, input().split()))
i = 0

while True:
    if num_list[i] == max(num_list):
        print(i+1)
        break
    
    i +=1