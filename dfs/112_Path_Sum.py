"""112_Path_Sum.py

Author: Juan Diego Becerra
Date:   06-30-2022
Brief:  https://leetcode.com/problems/path-sum/
"""


# Time: O(h) | Space: O(1)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(h) | Space: O(1)
def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False

    if not (root.left or root.right):
        return targetSum - root.val == 0

    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)