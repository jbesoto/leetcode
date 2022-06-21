"""9_Palindrome_Number.py

Author: Juan Diego Becerra
Date:   06-08-2022
Brief:  https://leetcode.com/problems/palindrome-number
"""


# Time: O(n) | Space: O(1)
def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    # Reverse right half of number
    right = 0
    while x > right:
        right = right * 10 + x % 10
        x //= 10

    # Check if number is a palindrome
    return x == right or x == right // 10
