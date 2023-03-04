n = input().split()
m = n[1]

s = []
t = []
dup = 0
count = 0

for i in range(int(n[0])):
    s.append(input())

for i in range(int(m)):
    t.append(input())

for i in range(len(t)):
    if t.count(t[i]) > 1:
        # dup += 1
        t[i] = "####"

for i in range(int(n[0])):
    for j in range(int(m)):
        if s[i].endswith(t[j]):
            count += 1

print(count)
        