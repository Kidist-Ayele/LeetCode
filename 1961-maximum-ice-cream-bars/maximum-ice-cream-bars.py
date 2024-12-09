class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        arr = [0] * (max(costs) + 1)
        for i in range(len(costs)):
            arr[costs[i]] += 1
        result = []
        for i in range(len(arr)):
            result.extend([i] * arr[i])

       
        total = 0
        
        for right in range(len(result)):
            total += result[right]
            if total > coins:
                return right
        return len(result)
        

