class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        a1 = max(nums)
        an = a1 + (k - 1)
        sn = (k * (a1 + an)) // 2
        return sn


        