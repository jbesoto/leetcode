"""744_Find_Smallest_Letter_Greater_Than_Target.py

Author: Juan Diego Becerra
Date:   06-15-2022
Brief:  https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""


import bisect


# Time: O(log n) | Space: O(1)
def nextGreatestLetter(letters: list[str], target: str) -> str:
    i = bisect.bisect(letters, target)
    return letters[i % len(letters)]
