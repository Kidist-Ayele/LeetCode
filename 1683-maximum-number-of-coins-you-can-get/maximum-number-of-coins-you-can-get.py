class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, reverse = True)
        res = 0
        for i in range(1, 2 * (len(piles) // 3), 2):
            res += piles[i]
        return res

        