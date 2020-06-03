# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/

"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:
    Input: [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation: 
        The first person goes to city A for a cost of 10.
        The second person goes to city A for a cost of 30.
        The third person goes to city B for a cost of 50.
        The fourth person goes to city B for a cost of 20.
        The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Note:
    (1) 1 <= costs.length <= 100
    (2) It is guaranteed that costs.length is even.
    (3) 1 <= costs[i][0], costs[i][1] <= 1000
"""

class Solution:
    def twoCitySchedCost(self, costs): # twoCitySchedCost(self, costs: List[List[int]]) -> int
        total_cost = 0
        cityA, cityB = [], []

        for index, cost in enumerate(costs):
            if cost[0] < cost[1]:
                total_cost += cost[0]
                cityA.append(index)
            else:
                total_cost += cost[1]
                cityB.append(index)
        
        if len(cityA) == len(cityB):
            return total_cost
   
        # Difference between people going to each city
        if len(cityA) > len(cityB):
            diff = len(costs)//2 - len(cityB)
        else:
            diff = len(costs)//2 - len(cityA)
        cost_diff = []
        
        if len(cityA) > len(cityB):
            for a_index in range(len(cityA)):
                index = cityA[a_index] # Index of person in "costs" list 
                cost_diff.append(costs[index][1] - costs[index][0])
        else:
            for b_index in range(len(cityB)):
                index = cityB[b_index]
                cost_diff.append(costs[index][0] - costs[index][1])

        print(diff, cost_diff)
        cost_diff.sort()
        for i in range(diff):
            total_cost += cost_diff[i]
        return total_cost

inputs = [
    [[10,20],[30,200],[400,50],[30,20]],
    [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]],
    [[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]
]

outputs = [110, 1859, 3671]

S = Solution()
for i in range(len(outputs)):
    print(S.twoCitySchedCost(inputs[i]))
    # print(f'Case {i+1}: {S.twoCitySchedCost(inputs[i]) == outputs[i]}')