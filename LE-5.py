s = 'iptmykvjanwiihepqhzupneckpzomgvzmyoybzfynybpfybngttozprjbupciuinpzryritfmyxyppxigitnemanreexcpwscvcwddnfjswgprabdggbgcillisyoskdodzlpbltefiz'
n = len(s)
max1 = 1  # 当前最长回文长度
L = R = n // 2  # 初始左右边界（至少一个字符）

for i in range(0, n // 2):
    if n - 2 * i <= max1:
        break
    else:
        for j in range(1, (n - 1) // 2 + 1):
            left = n // 2 + i - j
            right = n // 2 + i + j

            # 边界检查（Python 必须显式写）
            if left < 0 or right >= n:
                break

            if s[left] == s[right] and max1 >= 2 * j + 1:
                continue
            elif s[left] == s[right] and max1 < 2 * j + 1:
                max1 = 2 * j + 1
                L = left
                R = right
            else:
                break

for i in range(1, n // 2 + 1):
    center = n // 2 - i

    # 剪枝：理论最大长度不可能超过当前 max1
    if 2 * center + 1 <= max1:
        break

    for j in range(1, n):
        left = center - j
        right = center + j

        if left < 0 or right >= n:
            break

        if s[left] == s[right]:
            if 2 * j + 1 > max1:
                max1 = 2 * j + 1
                L = left
                R = right
        else:
            break

for i in range(0, n // 2):
    left_center = n // 2 + i
    right_center = left_center + 1

    if right_center >= n:
        break

    if 2 * n - 2 * right_center < max1:
        break

    j = 0
    while True:
        left = left_center - j
        right = right_center + j

        if left < 0 or right >= n:
            break

        if s[left] == s[right]:
            curr_len = 2 * (j + 1)
            if curr_len > max1:
                max1 = curr_len
                L = left
                R = right
            j += 1
        else:
            break

for i in range(1, n // 2 + 1):
    right_center = n // 2 - i + 1
    left_center = right_center - 1

    if left_center < 0:
        break

    # 剪枝
    if 2 * (left_center + 1) < max1:
        break

    j = 0
    while True:
        left = left_center - j
        right = right_center + j

        if left < 0 or right >= n:
            break

        if s[left] == s[right]:
            curr_len = 2 * (j + 1)
            if curr_len > max1:
                max1 = curr_len
                L = left
                R = right
            j += 1
        else:
            break
print(s[L:R + 1])
