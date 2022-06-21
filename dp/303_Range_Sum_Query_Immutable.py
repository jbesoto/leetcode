"""303_Range_Sum_Query_Immutable.py

Author: Juan Diego Becerra
Date:   06-10-2022
Brief:  https://leetcode.com/problems/range-sum-query-immutable/
"""


class NumArray:

    # Time: O(n) | Space: O(n)
    def __init__(self, nums: list[int]):
        self.prefix_sum = [0]

        for i in range(len(nums)):
            self.prefix_sum.append(self.prefix_sum[i] + nums[i])

    # Time: O(1) | Space: O(1)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
