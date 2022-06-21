/**
 * @file    271_Contains_Duplicate.cpp
 *
 * @author  Juan Diego Becerra
 * @date    2022-03-06
 * @brief   https://leetcode.com/problems/contains-duplicate/
 *
 */

#include <vector>
using namespace std;

// Time: O(n) | Space: O(1)
bool containsDuplicate(vector<int> &nums)
{
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = i + 1; j < nums.size(); j++)
        {
            if (j == nums.size())
                return false;
            else if (nums[i] == nums[j])
                return true;
        }
    }
    return false;
}