# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/

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
    ['50206', 1, '206'],
    ['50206', 2, '2'],
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