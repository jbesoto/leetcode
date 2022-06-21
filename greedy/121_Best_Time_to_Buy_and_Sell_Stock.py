"""121_Best_Time_to_Buy_and_Sell_Stock.py

Author: Juan Diego Becerra
Date:   06-09-2022
Brief:  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


# Time: O(n) | Space: O(1)
def maxProfit(prices: list[int]) -> int:
    i = 0
    j = i + 1
    max_profit = 0

    while j < len(prices):

        buy = prices[i]
        sell = prices[j]

        if buy > sell:  # not profitable
            i = j
        else:
            profit = sell - buy
            max_profit = max(max_profit, profit)

        j += 1  # look for potential greater profit

    return max_profit
