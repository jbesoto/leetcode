/**
 * @file    287_Find_the_Duplicate_Number.cpp
 *
 * @author  Juan Diego Becerra
 * @date    2022-03-28
 * @brief   https://leetcode.com/problems/find-the-duplicate-number/
 *
 */

#include <vector>
using namespace std;

int findDuplicate(vector<int> &nums)
{
    int n = nums.size() - 1;
    // [1, n], some k withing range is repeated

    int expected_sum = (n * (n + 1)) / 2;
    int real_sum = 0;

    for (int num : nums)
    {
        real_sum += num;
    }
    return real_sum - expected_sum;
}