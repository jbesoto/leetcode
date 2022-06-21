"""637_Average_of_Levels_in_a_Binary_Tree.py

Author: Juan Diego Becerra
Date:   06-15-2022
Brief:  https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n) | Space: O(m)  m: max nodes at any level
class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        res = []
        queue = [root]

        while len(queue) > 0:
            total, count = 0, 0
            tmp = []

            while len(queue) > 0:
                node = queue.pop()
                total += node.val
                count += 1
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            queue = tmp
            res.append(total / count)

        return res


# ==================================================================
# BREADTH-FIRST SEARCH (BFS)
# =================================================================
# Use a queue to keep track of the nodes in the current level and
# a temporary list to keep track of the nodes in the next level.
