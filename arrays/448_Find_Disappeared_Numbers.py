"""448_Find_Disappeared_Numbers.py

Author: Juan Diego Becerra
Date:   06-08-2022
Brief:  https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


# Time: O(n) | Space: O(1)
def findDisappearedNumbers(nums: list[int]) -> list[int]:
    res = []

    for num in nums:
        i = abs(num) - 1
        nums[i] = abs(nums[i]) * -1  # negative marking

    for i, num in enumerate(nums):
        if num > 0:
            res.append(i + 1)

    return res


# =================================================================
# PIGEONHOLE PRINCIPLE
# =================================================================
# Suppose there are n hole for n+1 pigeons. Hence, there must be
# more than one pigeon in a single hole.
#
# In this case, there are n indeces (holes) for n numbers (pigeons)
# ranging from 1 to n+1. The index number is used to determine the
# dissapeared numbers.
