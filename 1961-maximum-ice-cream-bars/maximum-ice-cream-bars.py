class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cur_total = 0
        for i in range(len(costs)):
            cur_total += costs[i]
            if cur_total > coins:
                return i
        return len(costs)
        