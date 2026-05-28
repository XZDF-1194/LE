s = 'abcabcbb'
x = 0
y = 1
max = 1
n = len(s)
# print(n)
while y < n:
    s_sub = s[x:y+1]
    if len(s_sub) == len(set(s_sub)):
        max = y + 1 -x
        y = y + 1
    else :
        x = x + 1
        y = y + 1
print(max)
# jjjj