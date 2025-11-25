prev = int(input())
count = 0
n = int(input())
while n != 0:
    if n > prev:
        count += 1
    prev = n
    n = int(input())
print(count)