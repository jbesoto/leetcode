"""70_Climbing_Stairs.py

Author: Juan Diego Becerra
Date:   06-09-2022
Brief:  https://leetcode.com/problems/climbing-stairs/
"""


# Time: O(2^n) | Space: O(1)
def climbStairs(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1

    return climbStairs(n - 1) + climbStairs(n - 2)
