s = 'PAYPALISHIRING'
s1 = ''
n = 4
i = 0
x = len(s)

m = x // (2*n - 2)  #完整的组数
k = x - m * (2*n - 2)  #最后一组的个数

# 第一行单独操作
if k == 0:
    for z in range(0, m):
        s1 = s1 + s[z * (2*n - 2)]
else :
    for z in range(0, m+1):
        s1 = s1 + s[z * (2*n - 2)]
print(s1)

# 第2~(n-1)行
for j in range(2, n):
    if 0 <= k <= n:
        i = 1 if k >= j else 0
    if k > n:
        i = 1 if j <= 2*n - k -1 else 2
    for q in range(0, m):
        s1 = s1 + s[(j - 1) + q * (2*n - 2)] + s[(2 * n - 1 - j) + q * (2*n - 2)]
    if i == 1:
        s1 = s1 + s[(j - 1) + m * (2*n - 2)]
    if i == 2:
        s1 = s1 + s[(j - 1) + m * (2 * n - 2)] + s[(2 * n - 1 - j) + m * (2 * n - 2)]

# 第n行单独操作
if k < n:
    for z in range(0, m):
        s1 = s1 + s[(n- 1) + (2*n -2) * z]
else:
    for z in range(0, m + 1):
        s1 = s1 + s[(n- 1) + (2*n -2) * z]

print(s1)

