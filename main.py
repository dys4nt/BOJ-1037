n = int(input())
li = list(map(int,input().split()))


min = 1000001
max = 1
for i in range(n):
    if li[i] < min:
        min = li[i]
    if li[i] > max:
        max = li[i]

print(min*max)