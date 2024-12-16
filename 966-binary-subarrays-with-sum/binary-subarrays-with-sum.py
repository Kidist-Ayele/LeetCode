class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prfx = defaultdict(int)
        pirefixsum = 0
        count = 0
        prfx[0] = 1
        for i in range(len(nums)):
            pirefixsum += nums[i]
            check = pirefixsum - goal
            if check in prfx:
                count += prfx[check]
            prfx[pirefixsum] += 1
        return count
        