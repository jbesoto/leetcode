"""104_Maximum_Depth_of_Binary_Tree.py

Author: Juan Diego Becerra
Date:   06-30-2022
Brief:  https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(h) | Space: O(1)
def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))