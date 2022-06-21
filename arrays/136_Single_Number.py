"""136_Single_Number.py

Author: Juan Diego Becerra
Date:   06-08-2022
Brief:  https://leetcode.com/problems/single-number/
"""


# Time: O(n) | Space: O(1)
def singleNumber(nums: list[int]) -> int:
    single_num = 0

    for num in nums:
        single_num ^= num

    return single_num
