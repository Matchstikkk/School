first = 0
second = 0
n = int(input())
while n != 0:
    if n > first:
        second = first
        first = n
    elif n > second:
        second = n
    n = int(input())
print(second)