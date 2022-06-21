"""1_Two_Sum.py

Author: Juan Diego Becerra
Date:   06-08-2022
Brief:  https://leetcode.com/problems/two-sum
"""


# Time: O(n) | Space: O(n)
def twoSum(nums, target: int):
    values = dict()

    for i, elem in enumerate(nums):
        comp = target - elem

        if comp in values:
            return [values[comp], i]
        values[elem] = i

    return []
