# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3499/

"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
    Input: k = 2, prices = [2,4,1]
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
    Input: k = 2, prices = [3,2,6,5,0,3]
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
    (1) 0 <= k <= 10^9
    (2) 0 <= prices.length <= 10^4
    (3) 0 <= prices[i] <= 1000
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        if k > n//2:
            profit = 0
            for i in range(1, n):
                if prices[i] - prices[i-1] > 0:
                    profit += prices[i] - prices[i-1]
            return profit
        
        dp = [[0 for i in range(n)] for j in range(k+1)]
        for i in range(1, k+1):
            max_profit = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], max_profit + prices[j])
                max_profit = max(max_profit, -prices[j] + dp[i-1][j])
        
        return dp[-1][-1]