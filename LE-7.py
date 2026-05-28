n = 1534236469
i = 1
res = 0
s1 = ''
if n < 0:
    i = -1
if n < 2**32 or n > 2**32 - 1:
    print(0)
n = abs(n)
s = str(n)
#print(s)
m = len(s)
#print(m)
for k in range(m):
    s1 = s1 + s[m - 1 - k]
#print(s1)
print(i)
if i == 1:
    res = int(s1)
else:
    res = -int(s1)
print(res)