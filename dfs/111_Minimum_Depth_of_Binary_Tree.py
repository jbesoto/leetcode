"""111_Minimum_Depth_of_Binary_Tree.py

Author: Juan Diego Becerra
Date:   06-16-2022
Brief:  https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n) | Space: O(h)  h: tree height
def minDepth_dfs(root: TreeNode) -> int:
    if not root:
        return 0

    if not root.left and not root.right:  # is a leaf?
        return 1

    if not root.left:
        return minDepth_dfs(root.right) + 1

    if not root.right:
        return minDepth_dfs(root.left) + 1

    return min(minDepth_dfs(root.left), minDepth_dfs(root.right)) + 1


# Time: O(n) | Space: O(m)  m: max nodes at any level
def minDepth_bfs(root: TreeNode) -> int:
    if not root:
        return 0

    queue = deque([(root, 1)])  # (node, depth)

    while len(queue):
        node, depth = queue.popleft()

        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))

        if node.right:
            queue.append((node.right, depth + 1))
