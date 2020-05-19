# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3334/

'''
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) 
for which the price of the stock was less than or equal to today's price.
For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:
    Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
    Output: [null,1,1,1,2,1,4,6]
    Explanation: 
        First, S = StockSpanner() is initialized.  Then:
        S.next(100) is called and returns 1,
        S.next(80) is called and returns 1,
        S.next(60) is called and returns 1,
        S.next(70) is called and returns 2,
        S.next(60) is called and returns 1,
        S.next(75) is called and returns 4,
        S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

Note:
    (1) Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
    (2) There will be at most 10000 calls to StockSpanner.next per test case.
    (3) There will be at most 150000 calls to StockSpanner.next across all test cases.
    (4) The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
'''

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = []
        self.prices = []
        self.index = -1        

    def next(self, price):  # next(self, price: int) -> int:
        self.index += 1
        self.prices.append(price)
        
        if self.index == 0:
            self.stack.append(0)
            self.span.append(1)
            
        else:
            while self.stack and self.prices[self.stack[-1]] <= self.prices[self.index]:
                self.stack.pop()
            
            if not self.stack:
                self.span.append(self.index+1)
            else:
                self.span.append(self.index - self.stack[-1])
            
            self.stack.append(self.index)
    
        return self.span[-1]

        


instructions = ["StockSpanner","next","next","next","next","next","next","next"]
prices = [[],[100],[80],[60],[70],[60],[75],[85]]

for i in range(len(instructions)):
    if instructions[i] == 'StockSpanner':
        S = StockSpanner()
        print('None', end=' ')
    else:
        print(S.next(prices[i]), end=' ')
    print()