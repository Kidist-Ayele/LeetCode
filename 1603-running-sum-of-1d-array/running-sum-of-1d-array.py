class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if ans:
                ans.append(ans[-1] + num)
            else:
                ans.append(num)
           
        return ans
        