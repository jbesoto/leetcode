/**
 * @file    448_Find_All_Numbers_Disappeared_in_an_Array.cpp
 * @author  Juan Diego Becerra
 * @brief   https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
 * @date    2022-03-22
 * 
 * Key:     Use negative marking technique. Indices [0, n-1] are used to map out numbers
 *          from [1, n]. If number n exists, map it out by marking position n-1. Return
 *          numbers i+1 at unmarked positions i.
 * 
 */


#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:

    // Time: O(n) | Space: O(1)
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (int num : nums) {
            int i = abs(num) - 1;  // associate number n to index n-1
            nums[i] = -1 * abs(nums[i]);  // mark index n-1 to hint that number n exists
        }

        vector<int> ans;
        for (int i = 0; i < nums.size(); ++i) {

            // unmarked index i means that number i+1 is missing
            if (nums[i] > 0) {  
                ans.push_back(i + 1);
            }
        }
        return ans;
    }
};