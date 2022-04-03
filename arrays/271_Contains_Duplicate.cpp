/**
 * @file    271_Contains_Duplicate.cpp
 * @author  Juan Diego Becerra
 * @brief   https://leetcode.com/problems/contains-duplicate/
 * @date    2022-03-06
 * 
 */


#include <vector>
using namespace std;

class Solution {
public:

    // Time: O(n) | Space: O(1)
    bool containsDuplicate(vector<int>& nums) {
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
};