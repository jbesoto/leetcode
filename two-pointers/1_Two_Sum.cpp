/**
 * @file    1_Two_Sum.cpp
 * @author  Juan Diego Becerra
 * @brief   https://leetcode.com/problems/two-sum/
 * @date    2021-11-01
 * 
 */


#include <vector>
#include <unordered_map>
using namespace std;


class Solution {
public:

    // Time: O(n) | Space: O(n)
    vector<int> twoSum(vector<int>& nums, int target) {
        // target - nums[i] = nums[j]

        unordered_map<int, int> seen;  // value : index
        int i, j;

        for (i = 0; i < nums.size(); ++i) {
            auto found = seen.find(target - nums[i]);

            if (found == seen.end()) {
                seen[nums[i]] = i;
            }
            else {  // found != seen.end()
                j = found->second;
                break;
            }
        }
        return {i, j}; 
    }
};