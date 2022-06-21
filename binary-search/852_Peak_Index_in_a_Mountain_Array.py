"""852_Peak_Index_in_a_Mountain_Array.py

Author: Juan Diego Becerra
Date:   06-15-2022
Brief:  https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""


# Time: O(log n) | Space: O(1)
def peakIndexInMountainArray(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (right + left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        elif arr[mid] < arr[mid - 1]:
            right = mid - 1
        else:  #  arr[mid - 1] < arr[mid] > arr[mid + 1]
            break

    return mid
