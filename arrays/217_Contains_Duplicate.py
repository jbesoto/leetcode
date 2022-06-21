"""217_Contains_Duplicate.py

Author: Juan Diego Becerra
Date:   06-08-2022
Brief:  https://leetcode.com/problems/contains-duplicate/
"""


# Time: O(n) | Space: O(n)
def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False
