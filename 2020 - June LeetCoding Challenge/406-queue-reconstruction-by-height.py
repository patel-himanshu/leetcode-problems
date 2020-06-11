# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/

"""
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the number of people in front of this person
 who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note: The number of people is less than 1,100.

Example
    Input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    Output: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

from collections import Counter
from operator import itemgetter

class Solution:
    def reconstructQueue(self, people): # reconstructQueue(self, people: List[List[int]]) -> List[List[int]]
        length = len(people)
        ans = []
        
        new_order = sorted(people, key=itemgetter(1))
        new_order = sorted(new_order, key=itemgetter(0), reverse=True)
        for i in range(length):
            if i==0:
                ans.append(new_order[i])
                continue
            ans.insert(new_order[i][1], new_order[i])
            print(ans)

        return ans

inputs = [
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
    [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
]

outputs = [
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]],
    [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]
]

S = Solution()
for i in range(len(inputs)):
    print(S.reconstructQueue(inputs[i]))