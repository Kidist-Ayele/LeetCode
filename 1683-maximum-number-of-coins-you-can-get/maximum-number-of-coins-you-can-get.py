class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        alice = me = bob = 0
        piles.sort()
        # print(piles)
        for i in range(len(piles) // 3, len(piles), 2):
            me += piles[i]
           
        return me

        