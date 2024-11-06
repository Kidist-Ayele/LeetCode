class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        def check(mid):
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / mid)
            return total <= h

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
                ans = min(ans, mid)
            else:
                left = mid + 1
        return ans

        