"""100_Same_Tree.py

Author: Juan Diego Becerra
Date:   06-16-2022
Brief:  https://leetcode.com/problems/same-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n) | Space: O(n) / O(log n)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif p and q:
            return (
                p.val == q.val
                and isSameTree(p.left, q.left)
                and isSameTree(p.right, q.right)
            )
        else:
            return False
