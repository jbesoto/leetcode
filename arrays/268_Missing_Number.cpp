/**
 * @file    268_Missing_Number.cpp
 *
 * @author  Juan Diego Becerra
 * @date    2021-11-20
 * @brief   https://leetcode.com/problems/missing-number/
 *
 */

#include <vector>
using namespace std;

// Time: O(n) | Space: O(1)
int missingNumber(vector<int> &nums)
{
    int n, expected_sum, actual_sum;
    actual_sum = 0;
    n = nums.size();
    expected_sum = (n * (n + 1)) / 2; // sum from [1, n]

    for (int num : nums)
    {
        actual_sum += num;
    }
    return expected_sum - actual_sum;
}