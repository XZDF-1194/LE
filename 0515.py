def count_words(words):
    # 在这里写代码
    n = len(words)
    d = {}

    for i in range(n):
        if words[i] in d:
            d[words[i]] += 1
        else:
             d[words[i]] = 1

    for k, word in enumerate(d):
        print (word, d[word])


words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count_words(words)



def two_sum(nums, target):
    n = len(nums)
    d = {}
    for k in range(n):
        need = target - nums[k]
        if need in d:
            return d[need], k
        else:
            d[nums[k]] = k

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))



def find_max(nums):
    n = len(nums)
    nums2 = sorted(nums)
    return nums2[n-1]

nums = [3, 1, 7, 2, 9, 4]
print (find_max(nums))

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

import torch
import torch.nn.functional as F 
