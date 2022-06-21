"""844_Backspace_String_Compare.py

Author: Juan Diego Becerra
Date:   06-21-2022
Brief:  https://leetcode.com/problems/backspace-string-compare/
"""


# Time: O(m + n) | Space: O(m + n)
def backspaceCompare(s: str, t: str) -> bool:
    return remove(s) == remove(t)


# Time: O(n) | Space: O(n)
def remove(s: str) -> str:
    """Remove all backspaces from a given string."""

    skip = 0
    res = []

    for char in reversed(s):
        if char == "#":
            skip += 1
        elif skip:
            skip -= 1
        else:
            res.append(char)

    return "".join(res)
