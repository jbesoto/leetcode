"""977_Squares_of_a_Sorted_Array.py

Author: Juan Diego Becerra
Date:   06-17-2022
Brief:  https://leetcode.com/problems/squares-of-a-sorted-array/
"""


# Time: O(n) | Space: O(n)
def sortedSquares(nums: list[int]) -> list[int]:
    left, right = 0, len(nums) - 1
    ans = [0] * len(nums)
    i = len(nums) - 1

    while left <= right:
        if abs(nums[left]) <= abs(nums[right]):
            ans[i] = nums[right] ** 2
            right -= 1
        else:  # abs(nums[left]) > abs(nums[right])
            ans[i] = nums[left] ** 2
            left += 1
        i -= 1

    return ans
