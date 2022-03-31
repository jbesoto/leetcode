/**
 * @file    268_Missing_Number.cpp
 * @author  Juan Diego Becerra
 * @brief   https://leetcode.com/problems/missing-number/
 * @date    2021-11-20
 * 
 * Key:     Compute expected and actual sum, return difference. No need to sort the
 *          array with this approach.
 */


#include <vector>
using namespace std;

class Solution {
public:

    // Time: O(n) | Space: O(1)
    int missingNumber(vector<int>& nums) {
        int n, expected_sum, actual_sum;
        actual_sum = 0;
        n = nums.size();
        expected_sum = (n * (n + 1)) / 2;  // sum from [1, n]

        for (int num : nums) {
            actual_sum += num;
        }        
        return expected_sum - actual_sum;
    }
};