a1 = int(input()) % 42
a2 = int(input()) % 42
a3 = int(input()) % 42
a4 = int(input()) % 42
a5 = int(input()) % 42
a6 = int(input()) % 42
a7 = int(input()) % 42
a8 = int(input()) % 42
a9 = int(input()) % 42
a10 = int(input()) % 42

a = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
dn = 0

for i in range(0,41):
    check = a.count(i)
    
    if check == 0:
        continue
    
    dn += 1

print(dn)



