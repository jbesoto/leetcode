/**
 * @file    136_Single_Number.cpp
 *
 * @author  Juan Diego Becerra
 * @date    2022-03-14
 * @brief   https://leetcode.com/problems/single-number/
 *
 */

#include <vector>
#include <iostream>
using namespace std;

// Time: O(n) | Space: O(1)
int singleNumber(vector<int> &nums)
{
    int ans = 0; // 0 ^ A = A

    for (int num : nums)
    {
        ans ^= num;
    }
    return ans;
}