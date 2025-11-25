max_num = 0
count = 0
n = int(input())
while n != 0:
    if n > max_num:
        max_num = n
        count = 1
    elif n == max_num:
        count += 1
    n = int(input())
print(count)