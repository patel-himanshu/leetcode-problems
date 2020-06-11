# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/

"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Example 1:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Note:
    (1) The length of num is less than 10002 and will be ≥ k.
    (2) The given num does not contain any leading zero.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        total = len(num)

        if k >= total:
            return '0'
        else:
            stack = []
            for i in range(total):
                while k and stack:
                    if num[i] < stack[-1]:
                        stack.pop()
                        k -= 1
                    else:
                        break
                stack.append(num[i])
            while k:
                stack.pop()
                k -= 1
            return str(int(''.join(stack)))

s = Solution()
cases = [
    ['10', 2, '0'],
    ['10200', 1, '200'],
    ['1020345', 2, '345'],
    ['1020345', 3, '34'],
    ['112', 1, '11'],
    ['1432219', 3, '1219'],
    ['947326', 2, '4326'],
    ['947326', 3, '326'],
    ['947326', 4, '26'],
]

for i in range(len(cases)):
    # print(i, s.removeKdigits(nums[i], ks[i]) == ans[i])
    print(s.removeKdigits(cases[i][0], cases[i][1]))
    # print('=======')