# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

"""
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
    Input: [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
    (1) 1 <= prices.length <= 3 * 10 ^ 4
    (2) 0 <= prices[i] <= 10 ^ 4
"""

class Solution:
    def maxProfit(self, prices): # maxProfit(self, prices: List[int]) -> int
        have_share = 0
        total_profit = 0
        profit = 0

        if len(prices) == 1:
            return 0

        new_prices = []
        for i in range(1,len(prices)):
            if prices[i-1] != prices[i]:
                new_prices.append(prices[i-1])
        new_prices.append(prices[-1])

        # print(new_prices)
        if len(new_prices) == 1:
            return 0

        if new_prices[0] < new_prices[1]:
            have_share = 1
            profit = new_prices[0]
            
        for i in range(1, len(new_prices)-1):
            if have_share and new_prices[i-1] < new_prices[i] > new_prices[i+1]:
                have_share = 0
                total_profit += abs(profit - new_prices[i])
                profit = 0
            elif not have_share and new_prices[i-1] > new_prices[i] < new_prices[i+1]:
                have_share = 1
                profit = new_prices[i]

        if have_share and new_prices[-1] > profit:
            total_profit += abs(profit - new_prices[-1])

        return total_profit

        """ 
        ================ Alternate method =====================
        profits = 0
        for i in range(len(prices)-1):
            profits += max(prices[i+1]-prices[i], 0)
        return profits
        ================ Alternate method =====================
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))
        """

inputs = [
    [1],
    [2,2,2,2,2],
    [7,1,5,3,6,4],
    [1,2,3,4,5],
    [7,6,4,3,1],
    [4,4,5,6,6,3], # [4,5,6,3]
    [4,4,2,6,6,3] # [4,2,6,3] 
]
outputs = [0,0,7,4,0,2,4]

S = Solution()
for i in range(len(inputs)):
    print(f'Case {i+1}: {S.maxProfit(inputs[i]) == outputs[i]} [{S.maxProfit(inputs[i])}]')
    # print(f'Case {i}: {S.maxProfit(inputs[i])}\n===============')