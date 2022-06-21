"""169_Majority_Element.py

Author: Juan Diego Becerra
Date:   06-21-2022
Brief:  https://leetcode.com/problems/majority-element/
"""


# Time: O(n) | Space: O(1)
def majorityElement(nums: list[int]) -> int:
    count, res = 0, nums[0]

    for num in nums:
        if count == 0:
            res = num
        count += (1 if num == res else -1)

    return res


# =============================================================================
# BOYER-MOORE VOTING ALGORIRITHM
# =============================================================================
# This algorithm is used to find the majority element among the given elements
# that have more than N/2 occurrences. This algorithm works on the fact that if
# an element occurs more than N/2 times, then the rest of the elements occur
# less than N/2 times.
