"""338_Counting_Bits.py

Author: Juan Diego Becerra
Date:   06-10-2022
Brief:  https://leetcode.com/problems/counting-bits/
"""


# Time: O(n) | Space: O(1)
def countBits(n: int) -> list[int]:
    ans = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if 2 * offset == i:
            offset *= 2
        ans[i] = 1 + ans[i - offset]

    return ans


# =================================================================
# SIGNIFICANT BITS
# =================================================================
# Binary numbers  follow a pattern. One significant bit is added
# for every power of 2.
#
# E.g.
# 1 = 0001, 2 = 0010, 4 = 0100, 8 = 1000
#
# Then, to represent the number 5 we add 1 significant bit and the
# number of bits in the binary representation of 1 (i. 5 minus the
# previous power of 2).
#
# 5 = 0101
# 1 + 4 = 0001 + 0100
