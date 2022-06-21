"""268_Missing_Number.py

Author: Juan Diego Becerra
Date:   06-08-2022
Brief:  https://leetcode.com/problems/missing-number/
"""


# Time: O(n) | Space: O(1)
def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2  # sum of consecutive numbers from 0 to n
    real_sum = 0

    for num in nums:
        real_sum += num

    return expected_sum - real_sum
