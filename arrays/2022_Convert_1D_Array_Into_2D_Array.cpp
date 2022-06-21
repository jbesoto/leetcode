/**
 * @file    2022_Convert_1D_Array_Into_2D_Array.cpp
 *
 * @author  Juan Diego Becerra
 * @date    2022-03-17
 * @brief   https://leetcode.com/problems/convert-1d-array-into-2d-array/
 *
 */

#include <vector>
#include <iostream>
using namespace std;

// Time: O(n) | Space: O(n)
vector<vector<int>> construct2DArray(vector<int> &original, int m, int n)
{
    vector<vector<int>> ans;

    if (m * n == original.size())
    { // check if valid 2d array
        int itr = 1;
        int i = 0;

        // m iterations, for each iteration pick n elements
        for (int itr = 1; itr <= m; ++itr)
        {

            // for each row pick elements from index [i, itr * n)
            vector<int> aRow;
            while (i < itr * n)
            {
                aRow.push_back(original[i]);
                ++i;
            }
            ans.push_back(aRow);
        }
    }
    return ans;
}