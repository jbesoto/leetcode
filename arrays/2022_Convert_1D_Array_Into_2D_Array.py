"""2022_Convert_1D_Array_Into_2D_Array.py

Author: Juan Diego Becerra
Date:   06-30-2022
Brief:  https://leetcode.com/problems/convert-1d-array-into-2d-array/
"""


# Time: O(n) | Space: O(n)
def construct2DArray(original: list[int], m: int, n: int) -> list[list[int]]:
    offset, start = 1, 0
    new = []

    if m * n != len(original):
        return []
    
    for i in range(m):
        row = [original[j] for j in range(start, n * offset)]
        new.append(row)
        start = n * offset
        offset += 1
    
    return new

