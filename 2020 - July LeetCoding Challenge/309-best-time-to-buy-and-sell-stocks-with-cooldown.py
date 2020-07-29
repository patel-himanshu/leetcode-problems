# Question: https://leetcode.com/explore/featured/card/july-leetcoding-challenge/548/week-5-july-29th-july-31st/3405/

"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share
of the stock multiple times) with the following restrictions:
    (1) You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    (2) After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
    Input: [1,2,3,0,2]
    Output: 3 
    Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown, sell, hold = 0, 0, -float('inf')
        
        for stock in prices:
            prev_cooldown, prev_sell, prev_hold = cooldown, sell, hold
            cooldown = max(prev_cooldown, prev_sell)
            sell = prev_hold + stock
            hold = max(prev_hold, prev_cooldown - stock)
            
        return max(sell, cooldown)