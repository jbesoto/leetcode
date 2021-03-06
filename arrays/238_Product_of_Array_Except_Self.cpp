/**
 * @file    238_Product_of_Array_Except_Self.cpp
 *
 * @author  Juan Diego Becerra
 * @date    2021-11-06
 * @brief   https://leetcode.com/problems/product-of-array-except-self/
 *
 */

#include <vector>
using namespace std;

// Time: (n) | Space: O(1)
vector<int> productExceptSelf(vector<int> &nums)
{
    // product except self = product left of self * product right of self

    int n = nums.size();
    int left = 1;
    int right = 1;
    vector<int> ans(n, 0);

    // compute products to left of self
    for (int i = 0; i < n; ++i)
    {
        if (i - 1 >= 0)
        {
            left *= nums[i - 1];
        }
        ans[i] = left;
    }

    for (int i = n - 1; i >= 0; --i)
    {
        if (i + 1 < n)
        {
            right *= nums[i + 1]; // compute products to right of self
        }
        ans[i] *= right; // compute products except self
    }

    return ans;
}