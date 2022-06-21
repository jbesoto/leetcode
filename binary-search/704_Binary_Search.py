"""704_Binary_Search.py

Author: Juan Diego Becerra
Date:   06-14-2022
Brief:  https://leetcode.com/problems/binary-search/
"""


# Time: O(log n) | Space: O(1)
def search(self, nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = right - left

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:  # nums[mid] > target
            right = mid - 1

    return -1
