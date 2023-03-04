s = input()
s = list(s)

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp = list(alp)

ans = []
count = 0

for i in range(len(s)):
    for j in range(len(alp)):
        if s[i] == alp[j]:
            ans.append(j)

for l in range(len(ans)):
    count += (pow(26,l)*int(ans[len(ans)-1-l]+1))

print(count)
