a = [int(x) for x in input().split()]

a.append(0)

rec,count = 0, 0
x = 0 

while a[x] != 0: 
    if a[x] + 1 == a[x + 1]:
        rec += 1
        if  count < rec:
            count = rec
    else:
        rec = 0  
    x += 1 

print(count  + 1)