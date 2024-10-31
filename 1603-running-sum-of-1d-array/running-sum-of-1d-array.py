class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            ans.append(prefix_sum)
        return ans
        