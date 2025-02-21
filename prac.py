
n, k = map(int, input().split())

l = list()
y = list()

for i in range(n):
    l.append(i + 1)

cur = 0

while True:
    for i in range(1,k):
        cur = (cur+1) % len(l)
    y.append(l[cur])
    l.remove(l[cur])
    if len(l) == 0:
        break

print("<" + ", ".join(map(str, y)) + ">")