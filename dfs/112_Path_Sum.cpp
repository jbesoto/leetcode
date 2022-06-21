/**
 * @file    112_Path_Sum.cpp
 *
 * @author  Juan Diego Becerra
 * @date    2021-11-01
 * @brief   https://leetcode.com/problems/path-sum/
 *
 */

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    bool hasPathSum(TreeNode *root, int targetSum)
    {
        if (root)
        {
            targetSum -= root->val;

            if (!root->left && !root->right)
            {
                return targetSum == 0;
            }
            return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
        }
        return false;
    }
};