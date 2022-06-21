/**
 * @file    136_Single_Number.cpp
 * @author  Juan Diego Becerra
 * @brief   https://leetcode.com/problems/single-number/
 * @date    2022-03-14
 * 
 * Key:     Use XOR to eliminates pairs. XOR operator is commutative, hence
 *          order in which elements are evaluated is irrelevant.
 * 
 */


#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:

    // Time: O(n) | Space: O(1)
    int singleNumber(vector<int>& nums) {
        int ans = 0;  // 0 ^ A = A

        for (int num : nums) {
            ans ^= num;
        }
        return ans;
    }
};

int main() {
    vector<int> ls = {1, 1, 3, 4, 4};
    Solution s;
    cout << s.singleNumber(ls) << endl;
}