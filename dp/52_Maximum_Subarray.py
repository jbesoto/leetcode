"""52_Maximum_Subarray.py

Author: Juan Diego Becerra
Date:   06-09-2022
Brief:  https://leetcode.com/problems/maximum-subarray/
"""


# Time: O(n) | Space: O(1)
def maxSubArray(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0  # does not contribute to a greater sum

        curr_sum += num
        max_sum = max(max_sum, curr_sum)

    return max_sum
