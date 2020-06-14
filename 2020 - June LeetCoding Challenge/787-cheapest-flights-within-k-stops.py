# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3360/

"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
    Input: 
        n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0, dst = 2, k = 1
    Output: 200
    Explanation: The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
    Input: 
        n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0, dst = 2, k = 0
    Output: 500
    Explanation: The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Constraints:
    (1) The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
    (2) The size of flights will be in range [0, n * (n - 1) / 2].
    (3) The format of each flight will be (src, dst, price).
    (4) The price of each flight will be in the range [1, 10000].
    (5) k is in the range of [0, n - 1].
    (6) There will not be any duplicated flights or self cycles.
"""

from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        
        adj = defaultdict(list)
        total_costs = defaultdict(lambda: float('inf'))
        
        for a,b,price in flights:
            adj[a] += [(b, price)]
            
        q = [(src, -1, 0)] # Each element of queue corresponds to (node, k, cost) at that node
        
        while q:
            node, k, cost = q.pop(0)
            if node == dst or k == K:
                continue
            for neighbour, price in adj[node]:
                if cost+price >= total_costs[neighbour]:
                    continue
                else:
                    total_costs[neighbour] = cost+price
                    q += [(neighbour, k+1, cost+price)]
        
        return total_costs[dst] if total_costs[dst] < float('inf') else -1                    